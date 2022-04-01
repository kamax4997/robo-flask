# app/__init__.py

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restplus import Api
from flask import Blueprint

from .api.controller.invoice import api as invoice_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
  title='Robolabs REST API',
  version='1.0',
  description='A flask rest project for Robolabs.lt API service'
)

api.add_namespace(invoice_ns, path='/invoice')
