import sys
import os
import zipfile
from xml.etree import ElementTree
from pathlib import Path
import re

from pydifact.generator.base import UntidBaseParser
from pydifact.generator.edsd import EDSDParser
from pydifact.generator.edcd import EDCDParser
from pydifact.generator.eded import EDEDParser
from pydifact.generator.uncl import UNCLParser
from pydifact.generator.edmd import EDMDParser
from pydifact.generator.unsl import UNSLParser

from os import PathLike


V4_RELEASE_NUMBER = "40219"


def xml_adopt(root: ElementTree.Element, new: ElementTree.Element) -> None:
    """
    Recursively adopt a new XML element into a root element.

    Args:
        root: The parent element to adopt into
        new: The new element to be adopted
    """
    # Create new child node
    node = ElementTree.SubElement(root, new.tag)
    node.text = new.text

    # Copy attributes
    for attr, value in new.attrib.items():
        node.set(attr, value)

    # Recursively copy children
    for child in new:
        xml_adopt(node, child)


def _expand_zip(
    zip_path: PathLike[str] | str,
    extract_to: PathLike[str] | str,
    members: list[str] | str | None = None,
) -> bool:
    """Internal work function to expand a ZIP file."""
    try:
        if isinstance(members, str):
            members = [members]
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(path=extract_to, members=members or None)
        return True
    except Exception as e:
        print(f"ERROR: Failed to extract {zip_path}: {e}")
        return False


def expand_zip(
    zip_path: PathLike[str] | str,
    extract_to: PathLike[str] | str,
    members: list[str] | str | None = None,
):
    """Extract a ZIP file to a directory.

    Prints status messages and errors if it fails.

    Args:
        zip_path: The path to the ZIP file
        extract_to: The path to the directory where the ZIP file should be extracted
        members: An optional list of file names to extract
            (must be a subset of the zip file's contents)
    """
    print(f"Extracting '{zip_path}'...", end="")
    if _expand_zip(zip_path, extract_to, members):
        print("OK")
    else:
        sys.exit(1)


def uppercase_files(directory: PathLike[str] | str) -> None:
    """Rename all files in directory to uppercase."""
    if not os.path.exists(directory):
        return

    for name in os.listdir(directory):
        if name in [".", ".."]:
            continue

        old_path = os.path.join(directory, name)
        new_name = name.upper()
        new_path = os.path.join(directory, new_name)

        if old_path != new_path and os.path.exists(old_path):
            try:
                os.rename(old_path, new_path)
            except OSError:
                pass  # File might already exist with an uppercase name


def extract_data(parser: UntidBaseParser, output_file: str, release: str) -> None:
    # Parse UNSL (service elements)
    print(f"Parsing {parser.name}... for {release}")
    try:

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(parser.get_xml())

        if parser.has_warnings():
            print(f"{parser.name} parser warnings:")
            for warning in parser.get_warnings():
                print(f"  WARNING: {warning}")

        if parser.has_errors():
            print(f"{parser.name} parser errors:")
            for error in parser.get_errors():
                print(f"  ERROR: {error}")

        print(f"{parser.name} parsing completed successfully")
    except Exception as e:
        # print(f"CRITICAL ERROR in {parser_class.name} parsing: {e}")
        # error_xml = f'<?xml version="1.0" encoding="utf-8" standalone="yes"?><error>{e}</error>'
        # with open(f"{generated_dir}/service_segments.xml", "w") as f:
        #     f.write(error_xml)
        raise e


def main():
    # Default version and edi directory
    syntax_version = "4"
    edi_directory = "24A"

    # Get version and edi_directory from command line argument
    if len(sys.argv) > 2:
        syntax_version = sys.argv[1]
        edi_directory = sys.argv[2].upper()
        if edi_directory.startswith("D"):
            edi_directory = edi_directory[1:]
    # Determine folder based on version
    folder = "../"
    if edi_directory == "99A" or (
        edi_directory[:2].isdigit() and 80 < int(edi_directory[:2]) < 99
    ):
        folder = "../pre99B/"

    release = f"D{edi_directory}"

    if syntax_version not in ["1", "2", "3", "4"]:
        print(f"ERROR: Unsupported syntax version: {syntax_version}")
        sys.exit(1)

    # Create the necessary directories
    extracted_dir = f"extracted/{release}"
    generated_dir = f"generated/{release}"
    services_dir = f"generated/services/v{syntax_version}"
    messages_dir = f"{generated_dir}/messages"

    os.makedirs(extracted_dir, exist_ok=True)
    os.makedirs(generated_dir, exist_ok=True)
    os.makedirs(messages_dir, exist_ok=True)
    os.makedirs(os.path.join(services_dir), exist_ok=True)

    # Check if ZIP files exists
    zips_directory = Path(".") / "zips"
    release_zip_file = zips_directory / f"{release.lower()}.zip"
    if not os.path.exists(release_zip_file):
        print(f"ERROR: ZIP file not found: {release_zip_file}")
        print("Available ZIP files:")
        for available_zip in Path(".").glob("*.zip"):
            print(f"  - {available_zip}")
        sys.exit(1)

    version_services_map = {
        "1": {},
        "2": {},
        "3": {
            "codes": (f"unsl{edi_directory.lower()}.zip", None),
            "elements": ("v3-sded.zip", "Sded.s3"),
            "composites": ("v3-sced.zip", "Sced.s3"),
            "segments": ("v3-ssed.zip", "Ssed.s3"),
            "messages": ("v3-smed.zip", "Smed.s3"),
        },
        "4": {
            "codes": (f"sl{V4_RELEASE_NUMBER}.zip", None),  #
            # as it is too complicated for now to match releases (e.g. 40219) with
            # directories (d24a), we just take the newest. This is not correct and
            # could lead to possible errors as some newer releases e.g. delete some
            # data elements.
            "elements": (
                f"sl{V4_RELEASE_NUMBER}.zip",
                f"sl{V4_RELEASE_NUMBER}.txt",
            ),
            "composites": "c40200.zip",
            "segments": "s40200.zip",
            "messages": "m40200.zip",
        },
    }

    release_map = version_services_map.get(syntax_version)

    # ----------------- SERVICE ZIP FILES -----------------

    unsl_zip_file, unsl_members = release_map["codes"]
    unsl_zip_file = zips_directory / unsl_zip_file
    # if not os.path.exists(unsl_zip_file):
    #     print(f"\nERROR: UNSL ZIP file not found: {unsl_zip_file}")
    #     sys.exit(1)

    # extract the UNSL codes ZIP file
    expand_zip(unsl_zip_file, extracted_dir, unsl_members)

    # service zip files
    expand_zip(
        zips_directory / release_map["elements"][0],
        extracted_dir,
        release_map["elements"][1],
    )

    extract_data(
        UNSLParser(f"{extracted_dir}/UNSL.{edi_directory}"),
        f"{services_dir}/data_elements.xml",
        release,
    )

    # ----------------- RELEASE ZIP FILES -----------------

    # Extract the release ZIP file
    expand_zip(release_zip_file, extracted_dir)

    # Create the EDMD directory
    edmd_dir = f"{extracted_dir}/MESSAGES"
    os.makedirs(edmd_dir, exist_ok=True)

    # NOTES ON RELEASES
    # 15B, 16A, 16B: zip contains a single folder
    # 15A: zip contains zip archives, each one containing a single folder
    # 03A: zips inside a Edifact/Directory/Files tree
    # 06A: zips inside a Edifact/Directory/Files tree and one folder per zip
    # 99B: zips inside EDIFACT/DIRECTOR
    # 97A: zips inside EDIFACT/D97ADISK, each zip contains EDIFACT/DIRECTOR folders
    # 96B: zips inside /EDIFACT/DIRECTOR/ARCHIVES/96B/DISK-ASC/
    # <=96B: FORMAT CHECK

    # Extract nested ZIP files
    for file in os.listdir(extracted_dir):
        if file.lower().endswith(".zip"):
            zip_path = os.path.join(extracted_dir, file)

            # EDSD/IDSD - segments (TRSD)
            # EDCD/IDCD - composite data elements (TRCD)
            # EDED      - data elements (TRED)
            # EDMD/IDMD - messages (TRMD)
            # UNCL      - codes list

            # TODO: evtl. move IDMD into separate directory?
            if re.search(r"(idmd|edmd|trmd)\.zip", file.lower()):
                expand_zip(zip_path, edmd_dir)
            else:
                expand_zip(zip_path, extracted_dir)

        else:
            if re.search(
                rf"(sl4\d{{4}}\.txt|unsl\.{edi_directory.lower()})", file.lower()
            ):
                os.rename(
                    f"{extracted_dir}/{file}",
                    f"{extracted_dir}/UNSL.{edi_directory}",
                )

    # Convert all filenames to uppercase
    uppercase_files(extracted_dir)
    uppercase_files(edmd_dir)

    # Rename TR* files to ED* files
    renames = [
        (
            f"{extracted_dir}/TRSD.{edi_directory}",
            f"{extracted_dir}/EDSD.{edi_directory}",
        ),
        (
            f"{extracted_dir}/TRCD.{edi_directory}",
            f"{extracted_dir}/EDCD.{edi_directory}",
        ),
        (
            f"{extracted_dir}/TRED.{edi_directory}",
            f"{extracted_dir}/EDED.{edi_directory}",
        ),
    ]

    for old_path, new_path in renames:
        if os.path.exists(old_path):
            os.rename(old_path, new_path)

    # Verify EDSD file exists
    edsd_file = f"{extracted_dir}/EDSD.{edi_directory}"
    if not os.path.exists(edsd_file):
        print(f"ERROR: No EDSD file found in {release} extraction")
        print(f"Available files in {extracted_dir}:")
        for file in os.listdir(extracted_dir):
            if file not in [".", ".."]:
                print(f"  - {file}")
        sys.exit(1)

    # Parse UNCL (code list)
    extract_data(
        uncl_parser := UNCLParser(f"{extracted_dir}/UNCL.{edi_directory}"),
        f"{generated_dir}/codes.xml",
        release,
    )

    # Parse EDED (data elements)
    extract_data(
        data_elements_parser := EDEDParser(
            f"{extracted_dir}/EDED.{edi_directory}", codes=uncl_parser.msg_xml
        ),
        f"{generated_dir}/data_elements.xml",
        release,
    )

    # Parse EDCD (composite data elements)
    extract_data(
        EDCDParser(
            f"{extracted_dir}/EDCD.{edi_directory}",
            data_elements=data_elements_parser.msg_xml,
        ),
        f"{generated_dir}/composite_data_elements.xml",
        release,
    )

    # Parse EDSD (segments)
    extract_data(EDSDParser(edsd_file), f"{generated_dir}/simple_segments.xml", release)

    # Parse EDMD (messages)
    print("Parsing EDMD... (Messages directory)")
    message_parse_errors = 0
    message_parse_warnings = 0

    for file in os.listdir(edmd_dir):
        if file in [".", ".."]:
            continue

        name = file[:6]
        if name in ["EDMDI1", "EDMDI2"]:
            continue

        try:
            p = EDMDParser(os.path.join(edmd_dir, file))
            data = p.get_xml()

            if p.has_warnings():
                print(f"EDMD Parser Warnings for {file}:")
                for warning in p.get_warnings():
                    print(f"  WARNING: {warning}")
                message_parse_warnings += 1

            if p.has_errors():
                print(f"EDMD Parser Errors for {file}:")
                for error in p.get_errors():
                    print(f"  ERROR: {error}")
                message_parse_errors += 1

            with open(f"{messages_dir}/{name.lower()}.xml", "w", encoding="utf-8") as f:
                f.write(data)
        except Exception as e:
            # print(f"CRITICAL ERROR in EDMD parsing for {file}: {e}")
            # error_xml = f'<?xml version="1.0" encoding="utf-8" standalone="yes"?><message><error>{e}</error></message>'
            # with open(f"{messages_dir}/{name.lower()}.xml", "w") as f:
            #     f.write(error_xml)
            message_parse_errors += 1
            raise e

    print("EDMD parsing completed")

    if message_parse_errors > 0:
        print(f" with {message_parse_errors} error(s)")
    else:
        print("")

    if message_parse_warnings > 0:
        print(f"Warnings: {message_parse_warnings}")

    print("All parsing completed.")

    # Merge: enrich simple segments with composite and data element details
    try:
        print("Starting XML merge process...")

        # Load XML files
        seg_tree = ElementTree.parse(f"{generated_dir}/simple_segments.xml")
        segment_root = seg_tree.getroot()

        data_element_tree = ElementTree.parse(f"{generated_dir}/data_elements.xml")
        data_element_root = data_element_tree.getroot()

        composite_tree = ElementTree.parse(
            f"{generated_dir}/composite_data_elements.xml"
        )
        composite_root = composite_tree.getroot()

        # Build lookup maps
        data_map = {}
        for element in list(data_element_root):
            element_id = element.get("id")
            if element_id:
                data_map[element_id] = element

        comp_map = {}
        for element in list(composite_root):
            element_id = element.get("id")
            if element_id:
                comp_map[element_id] = element

        merge_errors = 0

        # First pass: expand composite children under segments
        for seg in segment_root.findall("segment"):
            for child in list(seg):
                if child.tag == "composite_data_element":
                    cid = child.get("id")
                    comp_def = comp_map.get(cid)
                    if comp_def is None:
                        print(
                            f"WARNING: Composite data element {cid} not found in composite_data_elements.xml"
                        )
                        merge_errors += 1
                        continue
                    # copy attributes except id
                    for k, v in comp_def.attrib.items():
                        if k == "id":
                            continue
                        child.set(k, v)
                    # adopt children from composite definition
                    for orphan in list(comp_def):
                        xml_adopt(child, orphan)

        # Second pass: enrich data elements at segment level and inside composites
        for seg in segment_root.findall("segment"):
            for child in list(seg):
                if child.tag == "data_element":
                    did = child.get("id")
                    data_def = data_map.get(did)
                    if data_def is None:
                        print(
                            f"WARNING: Data element {did} not found in data_elements.xml"
                        )
                        merge_errors += 1
                        continue
                    for k, v in data_def.attrib.items():
                        if k == "id":
                            continue
                        child.set(k, v)
                    # adobt subitems, but except codes (directly in segments.xml)
                    for orphan in list(data_def):
                        if orphan.tag != "code":
                            xml_adopt(child, orphan)
                            print(f"adopting {orphan.tag} from data element {did}")

                if child.tag == "composite_data_element":
                    # enrich nested data elements inside composite with attributes
                    for child2 in list(child):
                        if child2.tag == "data_element":
                            did2 = child2.get("id")
                            data_def2 = data_map.get(did2)
                            if data_def2 is None:
                                print(
                                    f"WARNING: Data element {did2} not found in data_elements.xml during composite merge"
                                )
                                merge_errors += 1
                                continue
                            for k, v in data_def2.attrib.items():
                                if k == "id":
                                    continue
                                child2.set(k, v)

        # Write final merged segments.xml
        merged_path = f"{generated_dir}/segments.xml"
        # Pretty print the XML
        ElementTree.indent(seg_tree, space="  ")
        seg_tree.write(merged_path, encoding="utf-8", xml_declaration=True)
        # Remove simple_segments.xml to match PHP runner behavior
        try:
            os.remove(f"{generated_dir}/simple_segments.xml")
        except OSError:
            pass

        print("XML merge completed successfully")
        if merge_errors:
            print(f"Merge completed with {merge_errors} warning(s)")
    except Exception as e:
        print(f"CRITICAL ERROR during XML merge: {e}")
        # Fall back to copying simple_segments to segments.xml if merge fails
        try:
            with open(
                f"{generated_dir}/simple_segments.xml", "r", encoding="utf-8"
            ) as src:
                data = src.read()
            with open(f"{generated_dir}/segments.xml", "w", encoding="utf-8") as dst:
                dst.write(data)
        except Exception:
            pass
        raise e


if __name__ == "__main__":
    main()
