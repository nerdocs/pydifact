Syntax Generator
================

The ``pydifact.generator`` package contains tools to download and convert
official UN/EDIFACT directory releases and service segment definitions into
the XML data files that pydifact uses for segment validation.

You only need to run the generator when you want to add support for a new
EDIFACT directory release or service syntax version. The generated XML files
are checked into the repository under ``pydifact/syntax/``, so most users
never need to run this.

.. note::
   The generator requires an internet connection. It downloads ZIP archives
   from the UNECE website (``service.unece.org``) and, for service segments,
   from ``service.gefeg.com``.


Directory releases
------------------

A *directory release* contains the complete set of message types, segments,
composite data elements, data elements, and code lists for a given EDIFACT
publication (e.g. ``D.24A``, ``D.21A``, …).

Usage::

    uv run python -m pydifact.generator.runner <release>

    # or simpler:
    make generate <release>

The ``<release>`` argument accepts several formats – all of the following
refer to the same release:

* ``24a``
* ``d24a``
* ``D24A``
* ``D.24A``

Examples::

    # Generate syntax data for D.24A (latest supported release)
    uv run python -m pydifact.generator.runner d24a

    # Generate syntax data for D.21A
    uv run python -m pydifact.generator.runner 21a

    # Generate syntax data for D.96B (historic release)
    uv run python -m pydifact.generator.runner 96b

After a successful run the generated XML files are written to::

    pydifact/syntax/<release>/data/
    ├── codes.xml                   # UNCL code list
    ├── data_elements.xml           # EDED data elements
    ├── composite_data_elements.xml # EDCD composite data elements
    ├── segments.xml                # EDSD segments (merged, enriched)
    └── messages/
        └── *.xml                   # EDMD message structure files

Intermediate download artefacts (ZIP archives and extracted text files) are
stored under ``pydifact/generator/zips/`` and
``pydifact/generator/extracted/`` respectively so they can be reused on
subsequent runs.

Supported directory releases (``d88`` through ``d24a``) are listed in
``pydifact/generator/constants.py``.


Service segments
----------------

*Service segments* (UNB, UNH, UNT, …) are defined separately from directory
releases and are versioned by EDIFACT *syntax version* (1–4).

Usage::

    uv run python -m pydifact.generator.runner service <syntax_version>

    or simpler:
    make generate-service <release>

The ``<syntax_version>`` argument accepts:

* ``1``, ``2``, ``3``, or ``4`` — generates the latest supported sub-release
  for that syntax version.
* A specific sub-release identifier such as ``21A`` (v3) or ``40219`` (v4).

Examples::

    # Generate service data for syntax version 4 (latest sub-release)
    uv run python -m pydifact.generator.runner service 4

    # Generate service data for a specific v3 sub-release
    uv run python -m pydifact.generator.runner service 21A

    # Generate service data for a specific v4 sub-release
    uv run python -m pydifact.generator.runner service 40219

Generated files are written to::

    pydifact/syntax/service/v<extended_version>/data/


Makefile targets
----------------

The root ``Makefile`` provides convenience targets that wrap the generator
invocations above.

Generate a specific directory release::

    make generate RELEASE=21a

Generate service segment data for a syntax version::

    make generate-service SYNTAX=4

Or with a specific sub-release::

    make generate-service SYNTAX=21A
