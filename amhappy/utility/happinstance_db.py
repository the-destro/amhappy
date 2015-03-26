# -*- coding: utf-8 -*-
from pycouchdb import Server
from pycouchdb.exceptions import NotFound


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
        try:
            return self.server.database(application_name)
        except NotFound:
            return self.server.create(application_name)

    def get_application_db_names(self):

        # the result is a tuple with the body being the second element
        dbs = self.server.resource.get('_all_dbs')[1]
        return [db for db in dbs if not db.startswith('_')]

    def __json__(self, requesst):
        dbs = self.get_application_db_names()
        all_happinstances = {}
        for db_name in dbs:
            all_happinstances[db_name] = self[db_name].all(as_list=True)
        return all_happinstances
