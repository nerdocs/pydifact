import typing


if typing.TYPE_CHECKING:
    from pydifact.segments import Segment
    from pydifact.syntax.common import DataElement


class SyntaxRegistry:
    """
    Registry for managing EDI syntax elements including segments and data elements.

    This class provides a centralized registry for storing and retrieving segment
    and data element definitions organized by EDI directory versions.
    """

    base_package = "pydifact.syntax"
    # Caches to store loaded EDI directories and their segments/data elements.
    _segment_cache: dict[str, dict[str, type["Segment"]]] = {}
    _data_element_cache: dict[str, dict[str, type["DataElement"]]] = {}

    @classmethod
    def register_segment(cls, segment: type["Segment"], directory: str):
        """
        Register a segment type for a specific EDI directory.

        Args:
            segment: The segment class to register. Must be a subclass of Segment.
            directory: The EDI directory version identifier (e.g., 'd96a', 'd01b').

        Raises:
            AssertionError: If the segment is not a valid Segment subclass.
        """
        from pydifact.segments import Segment

        directory = directory.upper()
        if directory not in cls._segment_cache:
            cls._segment_cache[directory] = {}
        assert issubclass(
            segment, Segment
        ), f"Cannot register Segment of invalid type: {segment.__class__.__name__}"

        cls._segment_cache[directory][segment.tag] = segment

    @classmethod
    def register_data_element(cls, element: type["DataElement"], edi_directory: str):
        """
        Register a data element type for a specific EDI directory.

        Args:
            element: The data element class to register. Must be a subclass of DataElement.
            edi_directory: The EDI directory version identifier (e.g., 'd96a', 'd01b').

        Raises:
            AssertionError: If the element is not a valid DataElement subclass.
        """
        from pydifact.syntax.common import DataElement

        edi_directory = edi_directory.upper()
        if edi_directory not in cls._data_element_cache:
            cls._data_element_cache[edi_directory] = {}
        assert issubclass(
            element, DataElement
        ), f"Cannot register DataElement of invalid type: {element.__class__.__name__}"

        cls._data_element_cache[edi_directory][element.code] = element

    @classmethod
    def get_segment(cls, directory: str, tag: str) -> type["Segment"] | None:
        """
        Retrieve a registered segment type by directory and tag.

        Args:
            directory: The EDI directory version identifier.
            tag: The segment tag identifier (e.g., 'UNH', 'BGM').

        Returns:
            The registered segment class if found, None otherwise.
        """
        directory = directory.upper()
        if (
            directory not in cls._segment_cache
            or tag not in cls._segment_cache[directory]
        ):
            return None

        return cls._segment_cache[directory][tag]

    @classmethod
    def get_data_element(cls, directory: str, code: str) -> type["DataElement"] | None:
        """
        Retrieve a registered data element type by directory and code.

        Args:
            directory: The EDI directory version identifier.
            code: The data element code identifier (e.g., '0001', '0002').

        Returns:
            The registered data element class if found, None otherwise.
        """
        directory = directory.upper()
        if (
            directory not in cls._data_element_cache
            or code not in cls._data_element_cache[directory]
        ):
            return None

        return cls._data_element_cache[directory][code]
