# -*- coding: utf-8 -*-
import json
from amhappy.utility.happinstance_db import HappinstanceDB
from compose.cli.docker_client import docker_client
from compose.config import from_dictionary
from compose.project import Project, ConfigurationError
from compose.service import ConfigError
from amhappy.utility.error_response import GeneralError


def happinstance_exists(application, name, happinstance_db, request):
    """
    Validate whether a happinstance already exists. If it does, create the
    project and return the config
    :param application: Application Name
    :type application: str
    :param name: Happinstance Name
    :type name: str
    :param happinstance_db: DB object to look for the Happinstance in
    :type happinstance_db: dict-like
    :param request: the request to put the validated objects in
    :type request: Request
    """
    happinstance = _fetch_happinstance(application, name, happinstance_db)
    if happinstance is None:
        raise GeneralError("Happinstance Does Not Exist")
    request.validated['config'] = happinstance['config']
    request.validated['project'] = _fetch_project(name,
                                                  request.validated
                                                  ['config'])


def happinstance_unique(application, name, happinstance_db, request):
    """
    Validator to check for an existing Happinstance. If it exists, raise
    an error.
    :param application: Application Name
    :type application: str
    :param name: Happinstance Name
    :type name: str
    :param happinstance_db: DB object to look for the Happinstance in
    :type happinstance_db: dict-like
    :param request: Not Used but here for uniformity
    :type request: Request
    """
    happinstance = _fetch_happinstance(application, name, happinstance_db)
    if happinstance:
        raise GeneralError("Happinstance already exists")


def valid_happinstance(application, name, happinstance_db, request):
    """
    Check if a JSON response in a request body is a valid config. if it is,
    put the config and project in the validated objects
    :param application: Not used, here for API consistency
    :type application: str
    :param name: Name of the Happinstance
    :type name: str
    :param happinstance_db: Not used, here for API consistenc
    :type happinstance_db: dict-like
    :param request: the request to put the validated objects in
    :type request: Request
    """
    config = json.loads(request.body)
    try:
        if name == 'vhosts':
            raise GeneralError("vhosts is a reserved name")
        request.validated['project'] = _fetch_project(name, config)
        request.validated['config'] = config
    except (ConfigurationError, ConfigError), e:
        raise GeneralError(e.message)


def valid_action(application, name, happinstance_db, request):
    """
    Check if the json body contains a valid action
    """
    valid_actions = ['on', 'off']
    action = json.loads(request.body).get('action', '')
    if action.lower() in valid_actions:
        request.validated['action'] = action.lower()
    else:
        raise GeneralError('Invalid Action Requested')


def validator_factory(validator):

    validator_map = {'exists': happinstance_exists,
                     'unique': happinstance_unique,
                     'valid_config': valid_happinstance,
                     'valid_action': valid_action}

    def validate(request):
        application = request.matchdict['application']
        name = request.matchdict['name']
        happinstance_db = HappinstanceDB(request)
        validator_map[validator](application, name, happinstance_db, request)
        request.validated['application'] = application
        request.validated['name'] = name

    return validate


def _fetch_happinstance(application, name, happinstance_db):
    if application in happinstance_db:
        return happinstance_db[application].get(name)
    else:
        return None


def _fetch_project(name, config):
    """
    Wrap the call to Project.from_config as it has side effects
    :param name: name for the project
    :type name: str
    :param config: dictionary configuration
    :type config: dict
    :return: the docker-compose Project
    :rtype: Project
    """
    # get the Project Ready dictionary list. No Working Dir for us
    config_dicts = from_dictionary(config, working_dir='')
    return Project.from_dicts(name, config_dicts, docker_client())
