import sys
import os
import zipfile
from xml.etree import ElementTree
from pathlib import Path
import re

from pydifact.generator.edsd import EDSDParser
from pydifact.generator.edcd import EDCDParser
from pydifact.generator.eded import EDEDParser
from pydifact.generator.uncl import UNCLParser
from pydifact.generator.edmd import EDMDParser
from pydifact.generator.unsl import UNSLParser

from os import PathLike


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


def extract_zip(zip_path: PathLike[str] | str, extract_to: PathLike[str] | str) -> bool:
    """Extract a ZIP file to a directory."""
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)
        return True
    except Exception as e:
        print(f"ERROR: Failed to extract {zip_path}: {e}")
        return False


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

    # Create the necessary directories
    extracted_dir = f"extracted/{release}"
    generated_dir = f"generated/{release}"
    services_dir = f"generated/services/v{syntax_version}"
    messages_dir = f"{generated_dir}/messages"

    os.makedirs(extracted_dir, exist_ok=True)
    os.makedirs(generated_dir, exist_ok=True)
    os.makedirs(messages_dir, exist_ok=True)
    os.makedirs(os.path.join(services_dir), exist_ok=True)

    # Check if ZIP file exists
    zips_directory = Path(".") / "zips"
    release_zip_file = zips_directory / f"{release.lower()}.zip"
    if not os.path.exists(release_zip_file):
        print(f"ERROR: ZIP file not found: {release_zip_file}")
        print("Available ZIP files:")
        for available_zip in Path(".").glob("*.zip"):
            print(f"  - {available_zip}")
        sys.exit(1)

    unsl_zip_file = ""
    match syntax_version:
        case "4":
            unsl_zip_file = zips_directory / "sl40219.zip"
        case "3":
            unsl_zip_file = zips_directory / f"unsl{edi_directory.lower()}.zip"
        case "2":
            unsl_zip_file = zips_directory / "-.zip"  # FIXME
        case "1":
            unsl_zip_file = zips_directory / "-.zip"  # FIXME
        case _:
            print(f"ERROR: Unsupported syntax version: {syntax_version}")
            sys.exit(1)

    if not os.path.exists(unsl_zip_file):
        print(f"ERROR: UNSL ZIP file not found: {unsl_zip_file}")
        sys.exit(1)

    # Extract the main ZIP file
    print(f"Extracting release zip: {release_zip_file}...")
    if extract_zip(release_zip_file, extracted_dir):
        print("Extraction completed successfully")
    else:
        print(f"ERROR: Failed to open ZIP file: {release_zip_file}")
        sys.exit(1)

    # extract the UNSL ZIP file
    print(f"Extracting UNSL zip: {unsl_zip_file}...")
    if extract_zip(unsl_zip_file, extracted_dir):
        print("Extraction completed successfully")
    else:
        print(f"ERROR: Failed to open UNSL ZIP file: {unsl_zip_file}")
        sys.exit(1)

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

            # EDSD - segments (TRSD)
            # EDCD - composite data elements (TRCD)
            # EDED - data elements (TRED)
            # UNCL - codes list
            # EDMD - messages (TRMD)

            if re.search(r"(idmd|edmd|trmd)\.zip", file.lower()):
                extract_zip(zip_path, edmd_dir)
            else:
                extract_zip(zip_path, extracted_dir)
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
    print("Parsing UNCL... (User codes directory)")
    try:
        p = UNCLParser(f"{extracted_dir}/UNCL.{edi_directory}")

        with open(f"{generated_dir}/codes.xml", "w", encoding="utf-8") as f:
            f.write(p.get_xml())

        if p.has_warnings():
            print("UNCL Parser Warnings:")
            for warning in p.get_warnings():
                print(f"  WARNING: {warning}")

        if p.has_errors():
            print("UNCL Parser Errors:")
            for error in p.get_errors():
                print(f"  ERROR: {error}")

        codes = p.msg_xml
        print("UNCL parsing completed successfully")
    except Exception as e:
        print(f"CRITICAL ERROR in UNCL parsing: {e}")
        error_xml = f'<?xml version="1.0" encoding="utf-8" standalone="yes"?><data_elements><error>{e}</error></data_elements>'
        with open(f"{generated_dir}/codes.xml", "w") as f:
            f.write(error_xml)
        sys.exit(1)

    # Parse EDED (data elements)
    print("Parsing EDED... (Data elements directory)")
    try:
        p = EDEDParser(f"{extracted_dir}/EDED.{edi_directory}", codes=codes)

        with open(f"{generated_dir}/data_elements.xml", "w", encoding="utf-8") as f:
            f.write(p.get_xml())

        if p.has_warnings():
            print("EDED Parser Warnings:")
            for warning in p.get_warnings():
                print(f"  WARNING: {warning}")

        if p.has_errors():
            print("EDED Parser Errors:")
            for error in p.get_errors():
                print(f"  ERROR: {error}")

        data_elements = p.msg_xml
        print("EDED parsing completed successfully")
    except Exception as e:
        print(f"CRITICAL ERROR in EDED parsing: {e}")
        error_xml = f'<?xml version="1.0" encoding="utf-8" standalone="yes"?><data_elements><error>{e}</error></data_elements>'
        with open(f"{generated_dir}/data_elements.xml", "w") as f:
            f.write(error_xml)
        sys.exit(1)

    # Parse EDCD (composite data elements)
    print("Parsing EDCD... (Composite data elements directory)")
    try:
        p = EDCDParser(
            f"{extracted_dir}/EDCD.{edi_directory}", data_elements=data_elements
        )

        with open(
            f"{generated_dir}/composite_data_elements.xml", "w", encoding="utf-8"
        ) as f:
            f.write(p.get_xml())

        if p.has_warnings():
            print("EDCD Parser Warnings:")
            for warning in p.get_warnings():
                print(f"  WARNING: {warning}")

        if p.has_errors():
            print("EDCD Parser Errors:")
            for error in p.get_errors():
                print(f"  ERROR: {error}")

        print("EDCD parsing completed successfully")
    except Exception as e:
        print(f"CRITICAL ERROR in EDCD parsing: {e}")
        error_xml = f'<?xml version="1.0" encoding="utf-8" standalone="yes"?><composite_data_elements><error>{e}</error></composite_data_elements>'
        with open(f"{generated_dir}/composite_data_elements.xml", "w") as f:
            f.write(error_xml)
        sys.exit(1)

    # Parse EDSD (segments)
    print("Parsing EDSD... (Segments directory)")
    try:
        p = EDSDParser(edsd_file)

        # Write a simple (flat) segments file first; we'll enrich it after parsing EDCD/EDED
        with open(f"{generated_dir}/simple_segments.xml", "w", encoding="utf-8") as f:
            f.write(p.get_xml())

        if p.has_warnings():
            print("EDSD Parser Warnings:")
            for warning in p.get_warnings():
                print(f"  WARNING: {warning}")

        if p.has_errors():
            print("EDSD Parser Errors:")
            for error in p.get_errors():
                print(f"  ERROR: {error}")

        print("EDSD parsing completed successfully")
    except Exception as e:
        print(f"CRITICAL ERROR in EDSD parsing: {e}")
        error_xml = f'<?xml version="1.0" encoding="utf-8" standalone="yes"?><segments><error>{e}</error></segments>'
        with open(f"{generated_dir}/simple_segments.xml", "w") as f:
            f.write(error_xml)
        sys.exit(1)

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
            print(f"CRITICAL ERROR in EDMD parsing for {file}: {e}")
            error_xml = f'<?xml version="1.0" encoding="utf-8" standalone="yes"?><message><error>{e}</error></message>'
            with open(f"{messages_dir}/{name.lower()}.xml", "w") as f:
                f.write(error_xml)
            message_parse_errors += 1

    print("EDMD parsing completed")

    # Parse UNSL (service elements)
    print("Parsing UNSL... (Service elements directory)")
    try:

        p = UNSLParser(f"{extracted_dir}/UNSL.{edi_directory}")

        with open(f"{services_dir}/data_elements.xml", "w", encoding="utf-8") as f:
            f.write(p.get_xml())

        if p.has_warnings():
            print("UNSL Parser Warnings:")
            for warning in p.get_warnings():
                print(f"  WARNING: {warning}")

        if p.has_errors():
            print("UNSL Parser Errors:")
            for error in p.get_errors():
                print(f"  ERROR: {error}")

        print("UNSL parsing completed successfully")
    except Exception as e:
        print(f"CRITICAL ERROR in UNSL parsing: {e}")
        error_xml = f'<?xml version="1.0" encoding="utf-8" standalone="yes"?><data_elements><error>{e}</error></data_elements>'
        with open(f"{generated_dir}/service_segments.xml", "w") as f:
            f.write(error_xml)
        sys.exit(1)

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


if __name__ == "__main__":
    main()
