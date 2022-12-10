"""The main functionality of `image_to_excel`."""

import logging


class BaseClass:
    """Everything in the project comes back to here."""

    def __init__(self, log_level: int = logging.INFO):
        """Initialises the base class for `image_to_excel` by loading the config and setting up a logger.

        Args:
            log_level (str): The level to use for package logs.
        """
        self.logger = logging.getLogger(__name__).getChild(self.__class__.__qualname__)

        package_logger = logging.getLogger("image_to_excel")
        package_logger.setLevel(log_level)
