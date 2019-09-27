from schemas import service, plans, shipping
# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# # Skip this block if your db has no auth. But it really should.
# MONGO_USERNAME = '<your username>'
# MONGO_PASSWORD = '<your password>'
# # Name of the database on which the user can be authenticated,
# # needed if --auth mode is enabled.
# MONGO_AUTH_SOURCE = '<dbname>'

MONGO_DBNAME = 'pitney-bowes'

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
  'resource_methods': ['GET', 'POST'],

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
  'resource_methods': ['GET', 'POST'],

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
  'resource_methods': ['GET', 'POST'],

  'schema': shipping.shipping_schema
}

DOMAIN = {'services': services, 'plans': plans, 'shipping': shippings}
