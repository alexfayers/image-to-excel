"""CLI functionality of `image_to_excel`."""

import logging
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from . import BaseClass


def cli_main() -> None:
    """CLI entrypoint for `image_to_excel`. Uses `BaseClass`."""
    argparser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    argparser.add_argument("-v", "--verbose", help="Enable verbose logging", action="store_true")
    argparser

    args = argparser.parse_args()
    verbose_logging: bool = args.verbose

    if verbose_logging:
        level = logging.DEBUG
    else:
        level = logging.INFO

    app = BaseClass(log_level=level)
    app.logger.debug("We're in debug mode!")
