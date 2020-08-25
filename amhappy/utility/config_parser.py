# -*- coding: utf-8 -*-
import yaml
import copy
import os
from os.path import expanduser, expandvars, abspath


def find_configs(config_root, config_file):
    """
    given a config root and a file name, walk the root to collect all of the
    config paths
    :param config_root: Path to a root containing folders with a config_file
    :type config_root: str
    :param config_file: The name of the config file(fig.yml, compose.yml etc)
    :type config_file: str
    :return: Paths to the config files
    :rtype: str
    """
    # expand out any vars
    real_root = get_real_path(config_root)
    configs = {}
    for root, dirs, files in os.walk(real_root):
        # don't walk the git directory
        if '.git' in dirs:
            dirs.remove('.git')
        if config_file in files:
            # get the name that the conf is for. it is the last element
            # (the parent dir)
            conf_name = os.path.split(root)[-1]
            configs[conf_name] = os.path.join(root, config_file)
    return configs


def get_config(file_name):
    config = parse_config_file(file_name)
    # unpack the environment variables
    new_config = objectify_values(config, 'environment', '=')
    return new_config


def parse_config_file(file_name):
    with open(file_name, 'r') as fh:
        config = yaml.safe_load(fh)
    return config


def objectify_values(config, config_key, delimiter):
    """
    Take a config and a key to process and take the string and turn it into a
    key value pair
    :param config:
    :type config:
    :return:
    :rtype:
    """
    # Don't mutate the original config
    new_config = copy.deepcopy(config)

    def field_dictifier(value):
        if isinstance(value, dict):
            return value
        temp_value = value.split(delimiter)
        if len(temp_value) == 2:
            return {temp_value[0]: temp_value[1]}
        else:
            return {value: None}

    for service, values in config.items():
        field = values.get(config_key)
        # not every service will have the field we are looking for
        if field is not None and isinstance(field, list):
            # convert the field entries to dicts if they are not
            new_field = {}
            map(new_field.update, (field_dictifier(item) for item in field))
            new_config[service][config_key] = new_field
    return new_config


def get_real_path(path):
    """
    given a path that may be relative, reference home or have env vars, expand
    :param path: path to expand
    :type path: str
    :return: expanded path
    :rtype: str
    """
    expanded_path = expandvars(expanduser(path))
    return abspath(expanded_path)
