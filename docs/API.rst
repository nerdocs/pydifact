API
===

SegmentCollection
------------------
.. automodule:: pydifact.segmentcollection
    :members:

Parser
------
.. automodule:: pydifact.parser
    :members:

Segments
--------
.. automodule:: pydifact.segments
    :members:

Token
-----
.. automodule:: pydifact.token
    :members:

Serializer
----------
.. automodule:: pydifact.serializer
    :members:

Tokenizer
---------
.. automodule:: pydifact.tokenizer
    :members:


Plugin API
----------


Pydifact provides a framework, where some classes can be extended via plugins. These basically follow Marty Alchin's `Simple Plugin Framework <http://martyalchin.com/2008/jan/10/simple-plugin-framework/>`_.

The base meta class is a PluginMount:

.. autoclass:: pydifact.api.PluginMount


Available entry points for plugins are:

.. autoclass:: pydifact.segments.SegmentProvider
    :members:

    .. automethod:: SegmentProvider.__str__

