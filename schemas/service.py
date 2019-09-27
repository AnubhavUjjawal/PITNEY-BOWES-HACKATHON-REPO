service_schema = {
  'name': {
    'type': 'string',
    'required': True,
    'unique': True
  },
  'id': {
    'type': 'string',
    'required': True,
    'unique': True
  },
  'description': {
    'type': 'string'
  },
  'img': {
    'type': 'string',
    'required': True,
    'unique': True
  },
  'plans': {
    'type': 'list',
    'schema': {
      'type': 'integer'
    }
  }
}
