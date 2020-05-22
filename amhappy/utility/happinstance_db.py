# -*- coding: utf-8 -*-
import json
from couchdb import Server as CouchServer

import logging

logger = logging.getLogger('utility')

"""
Live Happinstance data access class.

Instantiate the connection to the happinstance (json) database server and
provide api for connectivity.
 
"""


class HappinstanceDB(object):

    def __init__(self, request=None, server=CouchServer):
        """
        A "DB" which is acting as a collection of the happinstances.

        TODO: Allow login logic that pulls from the ini

        Args:
            request:
        """
        logger.info("CREATING HAPPINSTANCE DB")
        self.happinstance_json_server = server()

    def __getitem__(self, application_name):
        return self.happinstance_json_server[application_name]

    def __contains__(self, name):
        return name in self.happinstance_json_server

    def __json__(self, request):
        happ_names = self.fetch_happ_names()
        happinstances = {}
        for happ_name in happ_names:
            config = self.happinstance_config(happ_name)
            logger.info("HAPP NAME CONFIG FOR %s IS: %s", happ_name, config)
            happinstance = [result.doc for result in config if result.id != 'vhosts']
            happinstances[happ_name] = happinstance
        return happinstances

    def fetch_happ_names(self):
        # The result is a tuple with the body being the third element
        dbs_in_json = self.happinstance_json_server.resource.get('_all_dbs')[
            2].read()
        logger.info("Database JSON is: %s", dbs_in_json)
        dbs = json.loads(dbs_in_json)
        return [db for db in dbs if not db.startswith('_')]

    def happinstance_config(self, happinstance_name):
        return self[happinstance_name].view('_all_docs', include_docs=True)

