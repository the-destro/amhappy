""" Cornice services.
"""
import os
from cornice import Service
from amhappy.utility.config_parser import get_real_path
from amhappy.utility.validators import validator_factory


config_info = Service(name='config_info', path='/config_options',
                      cors_enabled=True, cors_origins=('*',))


port_info = Service(name='port_info', path='/port_info/{application}/{name}')


@config_info.get()
def get_info(request):
    settings = request.registry.settings
    code_dirs = _get_code_dirs(settings['code_root'])
    return {'code_dirs': code_dirs}


def _get_code_dirs(root_directory):
    real_root = get_real_path(root_directory)
    return os.listdir(real_root)


@port_info.get(validators=validator_factory('exists'))
def get_ports(request):
    project = request.validated['project']
    return {container.name: container.human_readable_ports
            for container in project.containers()}

def _get_code_dirs(source_code_root):
    """
    We're returning a list of ALL folders here assuming that each one
    is the source code root of one of happ components.
    Args:
        happ_root:

    Returns:

    """
    real_root = get_real_path(source_code_root)
    return os.listdir(real_root)


