plan_schema = {
  'name': {
    'type': 'string',
    'required': True,
    'unique': True
  },
  'id': {
    'type': 'integer',
    'required': True,
    'unique': True
  },
  'description': {
    'type': 'string'
  },
  'recurring_payment': {
    'type': 'boolean',
    'required': True,
  },
  'recurring_span': {
    'type': 'string',
    'required': True,
  }
}
