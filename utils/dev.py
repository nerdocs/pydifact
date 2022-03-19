import warnings

from functools import wraps


def deprecation_warning(func):
    """Decorator to apply warn of function deprecation

    This decorator is used to mark functions and methods, which will be
    deprecated. To avoid errors and code breaks, apply a warning but
    execute implementation.

    ..automethod:: deprecation_warning(func):

    Args:
        func (function): which will be deprecated in a further release
    """

    @wraps(func)
    def fc(*args, **kwargs):
        """Call decorated funtion with given arguments and return it's value.

        ..automethod:: fc(inputs_decorated):

        Returns:
            _type_: _description_
        """
        warnings.warn(
            "This method: {} is deprecated.".format(func.__name__),
            DeprecationWarning,
            stacklevel=2,
        )
        return func(*args, **kwargs)

    return fc
