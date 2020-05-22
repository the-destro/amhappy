# -*- coding: utf-8 -*-
from cornice.resource import resource, view
from amhappy.utility.happ_finder import fetch_happs
from amhappy.utility.happ_finder import get_happ_configuration


import logging
logger=logging.getLogger('api')

@resource(collection_path='/applications',
          path='/applications/{application}',
          cors_enabled=True,
          cors_origins=('*',))
class Application(object):
    """
    Base application class that holds the default configuration of a
    docker-compose project. Not much during initially but will be expanded upon
    """


    def __init__(self, request):
        """
        Endpoint for the list of happs.

        Args:
            request:
        """
        self.request = request
        settings = self.request.registry.settings
        self.happs = fetch_happs(
            settings['happ_repo_root'],
            settings['happ_config_filename']) # Generally docker_compose.yml

    def collection_get(self):
        applications = self.happs.keys()
        logger.info("Applications %s", applications)
        return self.happs.keys()

    @view(renderer='json')
    def get(self):
        application_name = self.request.matchdict['application']
        config = get_happ_configuration(self.happs[application_name])
        return config
