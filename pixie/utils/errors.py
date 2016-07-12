class PixieException(Exception):
    pass


class FailedHaste(PixieException):
    """
    Raised when utils.hastebin fails to create a haste.
    """
    pass
