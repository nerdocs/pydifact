class PluginMount(type):
    """Generic plugin mount point for pydifact plugins"""

    # thanks to Marty Alchin!

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, "plugins"):
            cls.plugins = []
        else:
            if not hasattr(cls, "__omitted__"):
                cls.plugins.append(cls)


class EDISyntaxError(Exception):
    """A Syntax error within the parsed EDIFACT file was found."""
