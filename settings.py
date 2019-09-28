import os
from os.path import join, dirname
from schemas import service, plans, shipping
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGO_URI = os.getenv('MONGO_URI')

services = {
  'item_title': 'service',
  'additional_lookup': {
    'url': 'regex("[\w]+")',
    'field': 'id'
  },

  # We choose to override global cache-control directives for this resource.
  'cache_control': 'max-age=10,must-revalidate',
  'cache_expires': 10,

  # most global settings can be overridden at resource level
  'resource_methods': ['GET', 'POST', 'DELETE'],

  'schema': service.service_schema
}

plans = {
  'item_title': 'plans',
  'additional_lookup': {
    'url': 'regex("[0-9]+")',
    'field': 'id'
  },

  # We choose to override global cache-control directives for this resource.
  'cache_control': 'max-age=10,must-revalidate',
  'cache_expires': 10,

  # most global settings can be overridden at resource level
  'resource_methods': ['GET', 'POST', 'DELETE'],

  'schema': plans.plan_schema
}

shippings = {
  'item_title': 'shipping',
  'additional_lookup': {
    'url': 'regex("[0-9]+")',
    'field': 'id'
  },

  # We choose to override global cache-control directives for this resource.
  'cache_control': 'max-age=10,must-revalidate',
  'cache_expires': 10,

  # most global settings can be overridden at resource level
  'resource_methods': ['GET', 'POST', 'DELETE'],

  'schema': shipping.shipping_schema
}

DOMAIN = {'services': services, 'plans': plans, 'shipping': shippings}
