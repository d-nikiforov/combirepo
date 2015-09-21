#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os
import sys
import errno
import subprocess
import logging
import strings


def command_exists(command):
    """
    Checks whether the command exists in the given PATH evironment and exits
    the program in the case of failure.

    @param command  The command.
    @return         True if command exists,
                    False if file exists but is not executable,
                    exits otherwise.
    """
    logging.debug("Checking command \"{0}\"".format(command))
    try:
        DEV_NULL = open(os.devnull, 'w')
        subprocess.call([command], stdout=DEV_NULL, stderr=DEV_NULL)
    except OSError as error:
        if os.path.isfile(command):
            logging.error("File {0} cannot be executed.".format(command))
            return False
        elif error.errno == errno.ENOENT:
            logging.error("\"{0}\" command is not available. Try to "
                          "install it!".format(command))
        else:
            logging.error("Unknown error happened during checking the "
                          "command \"{0}\"!".format(command))
        sys.exit("Error.")
    return True


def directory_exists(directory_path):
    """
    Checks whether the directory exists and aborts the program in the case of
    failure.

    @param directory_path   The path to the directory.
    """
    if directory_path is None:
        raise Exception("Argument {0} is None!".format(directory_path))
    if not os.path.isdir(directory_path):
        logging.error("Directory {0} does not exist!".format(directory_path))
        sys.exit("Error.")


def file_exists(file_path):
    """
    Checks whether the file exists and aborts the program in the case of
    failure.

    @param file_path        The path to the file.
    """
    if file_path is None:
        raise Exception("Argument {0} is None!".format(file_path))
    if not os.path.isfile(file_path):
        logging.error("File {0} does not exist!".format(file_path))
        sys.exit("Error.")


def valid_identifier(string):
    """
    Checks whether the given string is a valid identifier and aborts the
    program in the case of failure.

    @param string       The string to be checked.
    """
    if string is None:
        raise Exception("Argument {0} is None!".format(string))
    if not strings.is_valid_identifier(string):
        logging.error("String {0} is not a valid identifier!".format(string))
        sys.exit("Error.")


def valid_ascii_string(string):
    """
    Checks whether the given string is a valid ASCII string and aborts the
    program in the case of failure.

    @param string       Teh string to be checked.
    """
    if string is None:
        raise Exception("Argument {0} is None!".format(string))
    if not strings.is_ascii_string(string):
        logging.error("String {0} is not an ASCII string!".format(string))
        sys.exit("Error.")
