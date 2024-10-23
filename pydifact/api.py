class PluginMount(type):
    """Generic plugin mount point (= entry point) for pydifact plugins.

    .. note::
        Plugins that have an **__omitted__** attribute are not added to the list!
    """

    # thanks to Marty Alchin!

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, "plugins"):
            cls.plugins = []
        else:
            if not getattr(cls, "__omitted__", False):
                cls.plugins.append(cls)


class EDISyntaxError(SyntaxError):
    """A Syntax error within the parsed EDIFACT file was found."""
