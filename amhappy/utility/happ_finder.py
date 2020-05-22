# -*- coding: utf-8 -*-
import yaml
import copy
import os
from os.path import expanduser, expandvars, abspath

import logging

logger = logging.getLogger('utility')


def fetch_happs(happ_root, happ_config_file):
    """
    Given a config root and a file name, walk the root to collect all of the
    config paths.

    Args:
        happ_root: Path to a root containing folders with a config_file
        happ_config_file: The name of the config file(fig.yml, compose.yml etc)

    Returns:
        Paths to the config files

    """
    real_root = get_real_path(happ_root)
    happs = {}
    for root, dirs, files in os.walk(real_root):
        # Don't walk a git directory
        if '.git' in dirs:
            dirs.remove('.git')
        if happ_config_file in files:
            # Use the parent dir as the happ_config name.
            happ_config_name = os.path.split(root)[-1]
            happs[happ_config_name] = os.path.join(root, happ_config_file)
    logger.info("Fetched Happs: %s", happs)
    return happs


def get_happ_configuration(happ_config_file):
    """
    Given the happ_config_file, return the full happ configuration
    Args:
        happ_config_file:

    Returns:

    """
    config = load_happ_file(happ_config_file)
    # unpack the environment variables
    new_config = objectify_values(config, 'environment', '=')
    return new_config


def load_happ_file(happ_config_file):
    """
    Read the happ config file (yaml) and return the safely loaded data.

    Args:
        happ_config_file:

    Returns:
        The result of a yaml.safe_load.
    """
    with open(happ_config_file, 'r') as fh:
        happ_configuration = yaml.safe_load(fh)
    return happ_configuration


def objectify_values(happ_configuration, key, delimiter):
    """
    Take a config and a key to process and take the string and turn it into a
    key value pair

    Args:
        happ_configuration:
        key:
        delimiter:

    Returns:
        Collection merging
    """
    # Don't mutate the original config
    new_config = copy.deepcopy(happ_configuration)

    def field_dictifier(value):
        if isinstance(value, dict):
            return value
        temp_value = value.split(delimiter)
        if len(temp_value) == 2:
            return {temp_value[0]: temp_value[1]}
        else:
            return {value: None}

    for service, values in happ_configuration.items():
        field = values.get(key)
        # Not every service will have the field we are looking for
        if field is not None and isinstance(field, list):
            # Convert the field entries to dicts if they are not
            new_field = {}
            map(new_field.update, (field_dictifier(item) for item in field))
            new_config[service][key] = new_field
    return new_config


def get_real_path(path):
    """
    Given a path that may be relative, reference home or have env vars, expand

    Args:
        path: path to expand

    Returns:
        expanded path
    """
    expanded_path = expandvars(expanduser(path))
    return abspath(expanded_path)
