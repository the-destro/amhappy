# -*- coding: utf-8 -*-
import json
from couchdb import Server


class HappinstanceDB(object):

    def __init__(self, request=None):
        """
        Will eventually allow login logic that pulls from the ini
        :param request:
        :type request:
        :return:
        :rtype:
        """
        self.server = Server()

    def __getitem__(self, application_name):
        return self.server[application_name]

    def __contains__(self, name):
        return name in self.server

    def get_application_db_names(self):
        # the result is a tuple with the body being the third element
        body_string = self.server.resource.get('_all_dbs')[2].read()
        dbs = json.loads(body_string)
        return [db for db in dbs if not db.startswith('_')]

    def __json__(self, request):
        dbs = self.get_application_db_names()
        all_happinstances = {}
        for db_name in dbs:
            all_happinstances[db_name] = []
            for result in self[db_name].view('_all_docs', include_docs=True):
                # remove the special vhosts entry as it is not an application
                if result.id != 'vhosts':
                    all_happinstances[db_name].append(result.doc)
        return all_happinstances
