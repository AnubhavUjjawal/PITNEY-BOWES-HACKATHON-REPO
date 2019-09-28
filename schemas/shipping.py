shipping_schema = {
  'id': {
    'type': 'integer',
    'required': True,
    'unique': True
  },
  'planId': {
    'type': 'integer',
    'required': True,
  },
  'notes': {
    'type': 'string',
  },
  'from_city': {
    'type': 'string',
    'required': True,
  },
  'to_city': {
    'type': 'string',
    'required': True,
  },
  'from_state': {
    'type': 'string',
    'required': True,
  },
  'to_state': {
    'type': 'string',
    'required': True,
  },
  'from_zip': {
    'type': 'string',
    'required': True,
  },
  'to_zip': {
    'type': 'string',
    'required': True,
  },
  'from_street': {
    'type': 'string',
    'required': True,
  },
  'to_street': {
    'type': 'string',
    'required': True,
  },
  'to_phone': {
    'type': 'integer',
    'required': True,
  },
  'from_phone': {
    'type': 'integer',
    'required': True,
  },
  'delivery_date': {
    'type': 'datetime',
    'required': True,
  },
  'status': {
    'type': 'string',
  }
}
