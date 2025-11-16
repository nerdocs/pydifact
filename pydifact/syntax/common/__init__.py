"""
This file contains commonly used classes described in the EDIFACT syntax.

There are multiple versions (1-4) of the EDIFACT standard, and they differ slightly.
As one project will probably never use more than one syntax version simultaneously,
it is split into 4 different python files, each of which could be imported using

```python
from pydifact.syntax.v[1..4] import ...
```

All of them provide the same structure.
"""

# from typing import Optional
#
# from pydifact.constants import EDI_DEFAULT_DIRECTORY
# from pydifact.exceptions import ValidationError
# from pydifact.syntax.common.types import DataElement
# from pydifact.syntax.registry import SyntaxRegistry
#
#
# # TODO: DataElementFactory is not used ATM
# class DataElementFactory:
#     """A factory for creating DataElement instances."""
#
#     @staticmethod
#     def create_data_element(
#         code: str,
#         value: Optional[str] = None,
#         validate: bool = True,
#         directory: str = EDI_DEFAULT_DIRECTORY,
#     ) -> DataElement:
#         """Create a new instance of a DataElement
#
#         Parameters:
#             code: The code of the DataElement
#             value: The data for this segment
#             validate: bool if True, the created element should be validated
#                 before return
#             version: The version of the EDI standard this element is based on
#                 (default: 4)
#         """
#         ElementClass = SyntaxRegistry.get_data_element(directory, code)
#         if ElementClass:
#             s = ElementClass(value or "")
#         else:
#             # we don't support this kind of EDIFACT DataElement (yet), so
#             # just create a generic DataElement()
#             s = DataElement(value or "")
#             s.code = "0000"  # unknown code. TODO: maybe find something better as code
#
#         if validate:
#             try:
#                 s.validate()
#             except ValidationError as e:
#                 raise ValueError(
#                     f"DataElement ({code}) `{value}` is not valid: {str(e)}"
#                 )
#         return s
