# -*- coding: utf-8 -*-
import json
from pyramid.httpexceptions import HTTPBadRequest


class GeneralError(HTTPBadRequest):
    def __init__(self, errors=''):
        error = dict(code=400, status='error', message=unicode(errors))
        HTTPBadRequest.__init__(self, body=json.dumps(error))
