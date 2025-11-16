# EDIFACT version changes

## VERSION 1 → VERSION 2 (1988 → 1990)

### Changes
* `UNA` segment (Service String Advice) added as **optional**.
* `UNB` / `UNZ` envelope refined and formally specified.
* Defined syntax separators as a set (component, element, decimal mark).
* Character Set Level A established as baseline (basic ASCII).
* Rules for numeric values added (decimal mark only, no grouping).

❗No message or group envelopes yet.

No `UNH`/`UNT`, no `UNG`/`UNE`.


## VERSION 2 → VERSION 3 (1990 → 1992)

### Additions:

* UNH / UNT message envelope introduced.
    → Mandatory at message level.
* `UNG` / `UNE` functional group envelope introduced.
* `UNS` segment introduced for separating logical sections of a message.
*  **Release character** defined (escape character).
*  Defined rules for empty elements and truncation (trailing components may be omitted).

### Envelope changes:

* UNB got **syntax identification** fields (syntax ID & syntax version number).
* Improved error-handling definitions (service error messages).


## VERSION 3 → VERSION 4 (1992 → 1998/2002)

### New capabilities:

* **Repetition separator** added ("+…:……?…’" and "" as repetition).
* Support for **repeating simple data elements**.
* Support for Character Set Levels A, B, plus `UNOB`/`UNOY`/`UNOW` character sets (through code tables):
  * `UNOW` = UTF-8 / UCS (ISO 10646) (only legal with Syntax Version 4).
* Extended UNA definitions for V4 (optional announcement of repetition separator).

### Envelope enhancements:

* UNB.1 (syntax identifier group) expanded to:
  * Syntax identifier
  * Syntax version number ("4")
  * Syntax release number ("1" for 2002 edition)
  * Character set / encoding code

### Service message changes:

* Updated `CONTRL` syntax in Part 4 for V4.
* AUT / ATN segments for authentication and secure interchange (Parts 5–10).

### Security and advanced features (V4 parts):

* Digital signatures
* Acknowledgements
* Security key management
* Cryptographic service instructions (Parts 5–10)