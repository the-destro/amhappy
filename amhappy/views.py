""" Cornice services.
"""
import os
from cornice import Service
from amhappy.utility.config_parser import get_real_path


config_info = Service(name='config_info', path='/config_options',
                      cors_enabled=True, cors_origins=('*',))


@config_info.get()
def get_info(request):
    settings = request.registry.settings
    code_dirs = _get_code_dirs(settings['code_root'])
    return {'code_dirs': code_dirs}

def _get_code_dirs(root_directory):
    real_root = get_real_path(root_directory)
    return os.listdir(real_root)


