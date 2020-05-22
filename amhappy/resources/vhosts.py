# -*- coding: utf-8 -*-
import json
from cornice.resource import resource, view
from amhappy.utility.happinstance_db import HappinstanceDB

import logging
logger=logging.getLogger('api')

@resource(collection_path='/vhosts', path='/vhosts/{application}',
          cors_enabled=True, cors_origins=('*',))
class Vhosts(object):
    """
    Endpoint to get Vhosts and create new ones
    """
    def __init__(self, request):
        self.request = request
        self.happinstancedb = HappinstanceDB(request)

    def collection_get(self):
        """
        return a list of all vhosts across all apps
        :return:
        :rtype:
        """
        applications = self.happinstancedb.fetch_happ_names()
        vhosts = {application: self.happinstancedb[application].get('vhosts')
                  for application in applications}
        return vhosts

    @view(renderer='json')
    def get(self):
        """
        Get the Vhost config for a particular application
        :return:
        :rtype:
        """
        vhosts = self._get_application_vhosts()
        logger.info(vhosts)
        # remove the _rev and _id fields
        vhosts.pop('_id')
        vhosts.pop('_rev')
        return vhosts

    @view(renderer='json')
    def post(self):
        """
        create a new vhost
        :return:
        :rtype:
        """
        vhosts = self._get_application_vhosts()
        new_vhost = json.loads(self.request.body)
        vhosts[new_vhost['name']] = False
        self._save_vhosts(vhosts)

    def allocate_vhost(self, vhost_name):
        """
        Allocate a particular vhost.
        TODO:: Maybe instead of T/F have it be the name of the happinstance?

        Args:
            vhost_name: 

        Returns:

        """
        vhosts = self._get_application_vhosts()
        vhosts[vhost_name] = True
        self._save_vhosts(vhosts)

    def _get_application_vhosts(self):
        application_name = self.request.matchdict['application']
        if application_name in self.happinstancedb:
            return self.happinstancedb[application_name].get('vhosts', {})
        else:
            # Created new app store
            self.happinstancedb.happinstance_json_server.create(application_name)
            return {}

    def _save_vhosts(self, vhosts):
        """

        Args:
            vhosts:

        Returns:

        """
        application_name = self.request.matchdict['application']
        self.happinstancedb[application_name]['vhosts'] = vhosts

