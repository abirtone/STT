# -*- coding: utf-8 -*-

"""
This file contains API calls and Data
"""

import six

from sys import version_info
from termcolor import colored

from .data import *

__version__ = "1.0.0"
__all__ = ["run_console", "run", "GlobalParameters"]


# --------------------------------------------------------------------------
#
# Command line options
#
# --------------------------------------------------------------------------
def run_console(config):
    """
    :param config: GlobalParameters option instance
    :type config: `GlobalParameters`

    :raises: TypeError
    """

    if not isinstance(config, GlobalParameters):
        raise TypeError("Expected GlobalParameters, got '%s' instead" % type(config))

    six.print_(colored("[*]", "blue"), "Starting s{TOOL_NAME}% execution")  # TODO
    run(config)
    six.print_(colored("[*]", "blue"), "Done!")


# ----------------------------------------------------------------------
#
# API call
#
# ----------------------------------------------------------------------
def run(config):
    """
    :param config: GlobalParameters option instance
    :type config: `GlobalParameters`

    :raises: TypeError
    """
    if not isinstance(config, GlobalParameters):
        raise TypeError("Expected GlobalParameters, got '%s' instead" % type(config))

    # --------------------------------------------------------------------------
    # Checks Python version
    # if version_info < (2, 7):
    #     raise RuntimeError("You need Python 2.7 or higher to run s{TOOL_NAME}%")

    # --------------------------------------------------------------------------
    # INSERT YOUR CODE HERE  # TODO
    # --------------------------------------------------------------------------