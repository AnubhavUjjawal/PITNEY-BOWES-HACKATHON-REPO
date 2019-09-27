shipping_schema = {
  'id': {
    'type': 'integer',
    'required': True,
    'unique': True
  },
  'planId': {
    'type': 'integer',
    'required': True,
    'unique': True
  },
  'notes': {
    'type': 'string',
  },
  'from_city': {
    'type': 'string',
    'required': True,
    'unique': True
  },
  'to_city': {
    'type': 'string',
    'required': True,
    'unique': True
  },
  'from_state': {
    'type': 'string',
    'required': True,
    'unique': True
  },
  'to_state': {
    'type': 'string',
    'required': True,
    'unique': True
  },
  'from_zip': {
    'type': 'string',
    'required': True,
    'unique': True
  },
  'to_zip': {
    'type': 'string',
    'required': True,
    'unique': True
  },
  'from_street': {
    'type': 'string',
    'required': True,
    'unique': True
  },
  'to_street': {
    'type': 'string',
    'required': True,
    'unique': True
  },
  'to_phone': {
    'type': 'integer',
    'required': True,
    'unique': True
  },
  'from_phone': {
    'type': 'integer',
    'required': True,
    'unique': True
  },
}
