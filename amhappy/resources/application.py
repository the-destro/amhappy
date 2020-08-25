# -*- coding: utf-8 -*-
from cornice.resource import resource, view
from amhappy.utility.config_parser import find_configs
from amhappy.utility.config_parser import get_config

@resource(collection_path='/applications', path='/applications/{application}',
          cors_enabled=True, cors_origins=('*',))
class Application(object):
    """
    Base application class that holds the default configuration of a
    docker-compose project. Not much during initially but will be expanded upon
    """
    def __init__(self, request):
        self.request = request
        config_root = self.request.registry.settings['config_root']
        config_file = self.request.registry.settings['config_file']
        self.configs = find_configs(config_root, config_file)

    def collection_get(self):
        return self.configs.keys()

    @view(renderer='json')
    def get(self):
        application_name = self.request.matchdict['application']
        config = get_config(self.configs[application_name])
        return config
