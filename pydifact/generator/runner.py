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
from pydifact.generator.constants import (
    directories_urls,
    V3_SERVICE_CODE_LISTS,
    V4_SERVICE_CODE_LISTS,
    services_map,
    renames,
)
from pydifact.generator.utils import is_prehistoric, download_file

from os import PathLike


V4_RELEASE_NUMBER = "40219"
zips_directory = Path(".") / "zips"


def print_usage() -> None:
    print(
        """
Usage: python edifact_generator.py  ( release | "service" syntax-version ) 
Options:
    release             EDIFACT Directory release, e.g. 'd24a', 'D21B', '90-1', 'service'
    service-release     If release is 'service', you have to provide a service release 
                        or syntax version like
                            '1', '2'          (for syntax v1+2)
                            '19A', '21A'      (for syntax v3)
                            '40100', '40219'  (for syntax v4)
Examples:
    pydifact-generator d24a
    pydifact-generator 90-1
    pydifact-generator service 19A
    pydifact-generator service 40219
    pydifact-generator service 1
"""
    )


def xml_adopt(root: ElementTree.Element, new: ElementTree.Element) -> None:
    """
    Recursively adopt a new XML element into a root element.

    Args:
        root: The parent element to adopt into
        new: The new element to be adopted
    """
    # Create a new child node
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
    """Internal worker function to expand a ZIP file."""
    try:
        if isinstance(members, str):
            members = [members]
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(path=extract_to, members=members or None)
        return True
    except Exception as e:
        print(f"ERROR: Failed to extract {zip_path}: {e}")
        return False


def extract_zip(
    zip_path: PathLike[str] | str,
    extract_to: PathLike[str] | str,
    members: list[str] | str | None = None,
) -> None:
    """Extract a ZIP file to a directory.

    Prints status messages and errors if it fails. If the `zip_path` is a non-zip file,
    it is copied as-is.

    Args:
        zip_path: The path to the ZIP file
        extract_to: The path to the directory where the ZIP file should be extracted
        members: An optional list of file names to extract
            (must be a subset of the zip file's contents)
    """
    if not zip_path or not extract_to:
        print("ERROR: Missing input paths for extracting.")
        return

    if not str(zip_path).lower().endswith(".zip"):
        print(f"Copying '{zip_path}' to {extract_to}...")
        try:
            os.symlink(zip_path, extract_to)
        except FileExistsError:
            pass
        return

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


def extract_edifact_data(
    parser: UntidBaseParser, output_file: str, release: str
) -> None:
    """
    Parse EDIFACT data using the provided parser and write the XML output to a file.

    Args:
        parser: An instance of UntidBaseParser or its subclass that will parse the
            EDIFACT data and generate XML output. The input file is passed to the
            parser.
        output_file: The file path where the generated XML output should be written.
            The file will be created or overwritten with UTF-8 encoding.
        release: The EDIFACT release identifier (e.g., 'D24A', 'service') used for
            logging and status messages during the parsing process.

    Returns:
        None

    Raises:
        Exception: Re-raises any exception that occurs during parsing or file writing.
    """
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
        # with open(f"{generated_data_dir}/service_segments.xml", "w") as f:
        #     f.write(error_xml)
        raise e


def get_syntax_version(argv: list) -> tuple[str, str, str]:
    """Parses service/syntax_version foo_release from command line argument"""
    if len(argv) > 1:
        if len(sys.argv) != 3:
            print("ERROR: if you specify 'service', you must provide a syntax version")
            print_usage()
            sys.exit(1)

        syntax_version: str = argv[2].upper()

        match syntax_version:
            case "1":
                syntax_version = service_subrelease = "1"
                extended_syntax_version = "100"
            case "2":
                syntax_version = service_subrelease = "2"
                extended_syntax_version = "200"
            case "3":
                syntax_version = "3"
                # use latest supported v3 syntax release
                service_subrelease = list(V3_SERVICE_CODE_LISTS.keys())[-1]
                extended_syntax_version = "300"
            case "4":
                syntax_version = "3"
                # use latest supported v4 syntax release
                service_subrelease = list(V4_SERVICE_CODE_LISTS.keys())[-1]
                extended_syntax_version = "402"
            case _:
                # maybe a very certain syntax is provided, then derive syntax
                # version from it
                service_subrelease = syntax_version
                if service_subrelease in V3_SERVICE_CODE_LISTS:
                    syntax_version = "3"
                    extended_syntax_version = "300"
                elif service_subrelease in V4_SERVICE_CODE_LISTS:
                    syntax_version = "4"
                    extended_syntax_version = service_subrelease[:3]
                else:
                    print(f"ERROR: Unsupported service release: {service_subrelease}.")
                    print("Could not determine syntax version")
                    print_usage()
                    sys.exit(1)

        return syntax_version, extended_syntax_version, service_subrelease

    print_usage()
    sys.exit(1)


def parse_messages(source_dir, target_dir) -> None:
    # Parse EDMD (messages)
    print("Parsing EDMD... (Messages directory)")
    message_parse_errors = 0
    message_parse_warnings = 0

    for file in os.listdir(source_dir):
        if file in [".", ".."]:
            continue

        name = file[:6]
        if name in ["EDMDI1", "EDMDI2"]:
            continue

        try:
            p = EDMDParser(os.path.join(source_dir, file))
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

            with open(f"{target_dir}/{name.lower()}.xml", "w", encoding="utf-8") as f:
                f.write(data)
        except Exception as e:
            # print(f"CRITICAL ERROR in EDMD parsing for {file}: {e}")
            # error_xml = f'<?xml version="1.0" encoding="utf-8" standalone="yes"?><message><error>{e}</error></message>'
            # with open(f"{messages_dir}/{name.lower()}.xml", "w") as f:
            #     f.write(error_xml)
            message_parse_errors += 1
            raise e

    if message_parse_errors > 0:
        print(f" with {message_parse_errors} error(s)")
    else:
        print("")

    if message_parse_warnings > 0:
        print(f"Warnings: {message_parse_warnings}")


def generate_service_codes(
    syntax_version: str, extended_syntax_version: str, service_subrelease: str
):

    specific_release = service_subrelease.lower()
    version_dir = f"v{specific_release}"
    generator_base_dir = Path(__file__).parent
    target_dir = generator_base_dir.parent / "syntax"
    extracted_dir = generator_base_dir / "extracted" / "service" / version_dir
    generated_data_dir = target_dir / "service" / version_dir / "data"
    extracted_messages_dir = f"{extracted_dir}/messages"
    generated_messages_dir = f"{generated_data_dir}/messages"
    syntax_specific_config: dict = services_map[extended_syntax_version]

    print(
        f"Preparing EDIFACT service file download for syntax version:"
        f" {syntax_version} (release {specific_release})"
    )
    os.makedirs(extracted_dir, exist_ok=True)
    os.makedirs(generated_data_dir, exist_ok=True)
    os.makedirs(extracted_messages_dir, exist_ok=True)
    os.makedirs(generated_messages_dir, exist_ok=True)

    # ----------------- SERVICE ZIP FILES -----------------
    for element in ["e", "c", "s"]:  # data element, composite, segment
        url = syntax_specific_config[element]["url"]
        filename = url.split("/")[-1]
        if filename:
            download_file(
                syntax_specific_config[element]["url"], zips_directory / filename
            )
            extract_zip(
                zips_directory / filename,
                extracted_dir,
                syntax_specific_config[element].get("extract", None),
            )
            for src, dst in syntax_specific_config[element].get("rename", {}).items():
                os.rename(
                    f"{extracted_dir}/{src}",
                    f"{extracted_dir}/{dst}",
                )
    # messages in a different directory
    filename = syntax_specific_config["m"]["url"].split("/")[-1]
    if filename:
        download_file(syntax_specific_config["m"]["url"], zips_directory / filename)
        extract_zip(
            zips_directory / syntax_specific_config["m"]["url"].split("/")[-1],
            extracted_messages_dir,
            syntax_specific_config["m"].get("extract", None),
        )
        for src, dst in syntax_specific_config["m"].get("rename", {}).items():
            os.rename(
                f"{extracted_dir}/{src}",
                f"{extracted_dir}/{dst}",
            )

    # ----------------- SUB-RELEASE SPECIFIC UNSL SERVICE ZIP FILES -----------------
    # UNSL service codes are specific to syntax subversion
    unsl_config = syntax_specific_config["unsl"]
    url = unsl_config["url"].format(release=specific_release)
    if url:
        unsl_zip_file = zips_directory / url.split("/")[-1]

        download_file(url, unsl_zip_file)

        # extract the UNSL codes ZIP file
        extract: str = unsl_config.get("extract", None)
        if extract:
            extract = extract.format(release=specific_release)
        extract_zip(unsl_zip_file, extracted_dir, extract)

        for old, new in unsl_config.get("rename", {}).items():
            old = Path(f"{extracted_dir}/{old}".format(release=specific_release))
            new = Path(f"{extracted_dir}/{new}".format(release=specific_release))
            if old.exists():
                os.rename(old, new)

        extract_edifact_data(
            UNSLParser(f"{extracted_dir}/UNSL.{specific_release}"),
            f"{generated_data_dir}/data_elements.xml",
            service_subrelease,
        )

    parse_messages(extracted_messages_dir, generated_messages_dir)


def generate_directory_release(release_upper: str):
    # EDIFACT Message/Directory releases
    release_upper = release_upper.upper().replace(".", "").replace("-", "")

    if release_upper.startswith("D"):
        # remove "D" prefix
        release_upper = release_upper[1:]

    if is_prehistoric(release_upper):
        folder = "../pre99B/"  # TODO

    # Determine folder based on version
    directory_release = f"d{release_upper.lower()}"

    print(f"Preparing EDIFACT download for directory release {directory_release}...")
    # Create the necessary directories
    target_dir = Path(__file__).parent.parent / "syntax"
    extracted_dir = Path(f"extracted/{directory_release}")
    generated_data_dir = target_dir / directory_release / "data"
    extracted_messages_dir = f"{extracted_dir}/MESSAGES"
    generated_messages_dir = f"{generated_data_dir}/messages"

    os.makedirs(extracted_dir, exist_ok=True)
    os.makedirs(generated_data_dir, exist_ok=True)
    os.makedirs(extracted_messages_dir, exist_ok=True)
    os.makedirs(generated_messages_dir, exist_ok=True)

    # NOTES ON RELEASES
    # 15B, 16A, 16B: zip contains a single folder
    # 15A: zip contains zip archives, each one containing a single folder
    # 03A: zips inside a Edifact/Directory/Files tree
    # 06A: zips inside a Edifact/Directory/Files tree and one folder per zip
    # 99B: zips inside EDIFACT/DIRECTOR
    # 97A: zips inside EDIFACT/D97ADISK, each zip contains EDIFACT/DIRECTOR folders
    # 96B: zips inside /EDIFACT/DIRECTOR/ARCHIVES/96B/DISK-ASC/
    # <=96B: FORMAT CHECK

    # ----------------- RELEASE ZIP FILES -----------------
    release_zip_file = (
        zips_directory / directories_urls[directory_release].split("/")[-1]
    )
    download_file(directories_urls[directory_release], release_zip_file)
    if not os.path.exists(release_zip_file):
        print(f"ERROR: ZIP file not found: {release_zip_file}")
        print("Available ZIP files:")
        for available_zip in Path(".").glob("*.zip"):
            print(f"  - {available_zip}")
        sys.exit(1)

    # Extract the release ZIP file
    extract_zip(release_zip_file, extracted_dir)
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
                extract_zip(zip_path, extracted_messages_dir)
            else:
                extract_zip(zip_path, extracted_dir)

    # Convert all filenames to uppercase
    uppercase_files(extracted_dir)
    uppercase_files(extracted_messages_dir)

    # Rename TR* files and ED?D-{release}.ASC to ED?D.{release} files

    for old_path, new_path in renames:
        if Path(extracted_dir / old_path.format(release=release_upper)).exists():
            os.rename(
                extracted_dir / old_path.format(release=release_upper),
                extracted_dir / new_path.format(release=release_upper),
            )

    # Verify EDSD file exists
    edsd_file = f"{extracted_dir}/EDSD.{release_upper.upper()}"
    if not os.path.exists(edsd_file):
        print(f"ERROR: No EDSD file found in {directory_release} extraction")
        print(f"Available files in {extracted_dir}:")
        for file in os.listdir(extracted_dir):
            if file not in [".", ".."]:
                print(f"  - {file}")
        sys.exit(1)

    # Parse UNCL (code list)
    uncl_filename = extracted_dir / f"UNCL.{release_upper}"
    uncl_parser = None
    if uncl_filename.exists():
        extract_edifact_data(
            uncl_parser := UNCLParser(uncl_filename, is_prehistoric(release_upper)),
            f"{generated_data_dir}/codes.xml",
            directory_release,
        )
    else:
        print(f"No UNCL file found in {directory_release} extraction")
        print(f"Available files in {extracted_dir}:")
        for file in os.listdir(extracted_dir):
            if file not in [".", ".."]:
                print(f"  - {file}")

    # Parse EDED (data elements)
    extract_edifact_data(
        data_elements_parser := EDEDParser(
            f"{extracted_dir}/EDED.{release_upper}",
            codes=uncl_parser.msg_xml if uncl_parser else None,
            is_prehistoric=is_prehistoric(release_upper),
            service=False,
        ),
        f"{generated_data_dir}/data_elements.xml",
        directory_release,
    )

    # Parse EDCD (composite data elements)
    extract_edifact_data(
        EDCDParser(
            f"{extracted_dir}/EDCD.{release_upper}",
            data_elements=data_elements_parser.msg_xml,
        ),
        f"{generated_data_dir}/composite_data_elements.xml",
        directory_release,
    )

    # Parse EDSD (segments)
    extract_edifact_data(
        EDSDParser(edsd_file, is_prehistoric(release_upper)),
        f"{generated_data_dir}/simple_segments.xml",
        directory_release,
    )

    parse_messages(extracted_messages_dir, generated_messages_dir)

    # Merge: enrich simple segments with composite and data element details
    try:
        print("Starting XML merge process...")

        # Load XML files
        seg_tree = ElementTree.parse(f"{generated_data_dir}/simple_segments.xml")
        segment_root = seg_tree.getroot()

        data_element_tree = ElementTree.parse(f"{generated_data_dir}/data_elements.xml")
        data_element_root = data_element_tree.getroot()

        composite_tree = ElementTree.parse(
            f"{generated_data_dir}/composite_data_elements.xml"
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
        merged_path = f"{generated_data_dir}/segments.xml"
        # Pretty print the XML
        ElementTree.indent(seg_tree, space="  ")
        seg_tree.write(merged_path, encoding="utf-8", xml_declaration=True)
        # Remove simple_segments.xml to match PHP runner behavior
        try:
            os.remove(f"{generated_data_dir}/simple_segments.xml")
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
                f"{generated_data_dir}/simple_segments.xml", "r", encoding="utf-8"
            ) as src:
                data = src.read()
            with open(
                f"{generated_data_dir}/segments.xml", "w", encoding="utf-8"
            ) as dst:
                dst.write(data)
        except Exception:
            pass
        raise e


if __name__ == "__main__":
    # check if we are in "service codes" generating mode, or directory releases
    if sys.argv[1].upper() == "SERVICE":
        generate_service_codes(*get_syntax_version(sys.argv))
    else:
        generate_directory_release(sys.argv[1])
