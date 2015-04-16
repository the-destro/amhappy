# -*- coding: utf-8 -*-
from cornice.resource import resource, view
from amhappy.utility.validators import validator_factory
from amhappy.utility.happinstance_db import HappinstanceDB


@resource(collection_path='/happinstances',
          path='/happinstances/{application}/{name}',
          cors_enabled=True, cors_origins=('*',))
class Happinstance(object):
    """
    A happinstance is an instance of an application that is read to run. This
    is a REST endpoint
    It named for being a Happy Instance
    """
    def __init__(self, request):
        """
        Basic init method that also sets up the instance variables for some of
        the endpoints
        :param request: The pyramid request
        :type request: Request
        """
        self.request = request
        self.happinstancedb = HappinstanceDB(request)
        self.name = ''
        self.application = ''
        self.project = None
        self.config = ''

    def collection_get(self):
        """
        Get the current happinstances, running or not
        :return: Dictionary of the happinstances
        :rtype: dict
        """
        # cast the storage as a dict and return it
        return {'happinstances': self.happinstancedb}

    @view(renderer='json', validators=validator_factory('exists'))
    def get(self):
        """
        Get the detail for a particular happinstance
        """
        self._get_valid_objects()
        return self.happinstancedb[self.application].get(self.name)

    @view(renderer='json', validators=[validator_factory('unique'),
                                       validator_factory('valid_config')])
    def post(self):
        """
        Take a unique and valid config and create a new happinstance and start
        it up. a POST endpoint
        """
        self._get_valid_objects()
        # a happinstance is defined by its config and status and keyed on its
        # name
        happinstance = {'_id': self.name,
                        'config': self.config, 'status': 'on'}
        self.project.up()
        self.happinstancedb[self.application].save(happinstance)
        return {'status': 'ok'}

    @view(renderer='json', validators=validator_factory('exists'))
    def delete(self):
        """
        If the happinstance exists, stop it and remove the containers and the
        entry in the db.
        """
        self._get_valid_objects()
        self.project.stop()
        self.project.remove_stopped()
        del self.happinstancedb[self.application][self.name]

    @view(renderer='json', validators=[validator_factory('exists'),
                                       validator_factory('valid_action')])
    def put(self):
        """
        take a validated action and either start or stop a happinstance
        """
        self._get_valid_objects()
        action = self.request.validated['action']
        happinstance = self.happinstancedb[self.application].get(self.name)
        if action == 'on':
            self.project.start()
        else:
            self.project.stop()
        happinstance['status'] = action
        self.happinstancedb[self.application].save(happinstance)

    def _get_valid_objects(self):
        """
        Pull the validated values and put them into instance vars
        """
        self.name = self.request.validated['name']
        self.application = self.request.validated['application']
        self.project = self.request.validated['project']
        self.config = self.request.validated['config']


