import logging
import sys
import pprint
import copy
from eve import Eve
from flask import Flask, escape, request
from flask_cors import CORS
from pymongo import MongoClient


client = MongoClient('mongodb+srv://admin:qazwsxedc@pitney-bowes-wgqbw.gcp.mongodb.net/test?retryWrites=true&w=majority')
app = Eve()
CORS(app)

fullfillment_res = {
      "fulfillmentText": "This is a text response",
      "source": "anuragintern.appspot.com",
      "payload": {
        "google": {
          "expectUserResponse": True,
          "richResponse": {
            "items": [
              {
                "simpleResponse": {
                  "textToSpeech": "this is a simple response"
                }
              }
            ]
          }
        },
      }
    }

@app.route('/dialogflow', methods=['POST'])
def  handle_dialoglow():
  app.logger.warning(pprint.pformat(request.json))
  x = request.json['queryResult']['intent']['displayName']
  res_string = ""

  if x == 'Order':
    o_no = int(request.json['queryResult']['parameters']['OrderNumber'])
    shipping_order = client.test['shipping'].find_one({'id': o_no})
    # print(shipping_order)
    res_string = f'Your Order with id {shipping_order["id"]} shipped to {shipping_order["to_street"]}, {shipping_order["to_city"]}, {shipping_order["to_state"]} scheduled to be delivered on {shipping_order["delivery_date"].strftime("%d %B %Y")}'
  elif x == 'ListServices':
    services = client.test['services'].find()
    res_string = f'The services offered by us are: '
    for service in services:
      res_string += service["name"] + ", "
  elif x == 'PaymentService':
    payment = client.test['services'].find_one({"id": "tracking"})
    res_string = f'Here is a brief decription about our Payment Service: {payment["description"]}'
  elif x == 'ShippingService':
    shipping = client.test['services'].find_one({"id": "shipping"})
    res_string = f'Let me give you a brief description about our Shipping service: {shipping["description"]}'
  elif x == 'TrackingService':
    tracking = client.test['services'].find_one({"id": "tracking"})
    res_string = f'An introduction to our Tracking service: {tracking["description"]}'

  res = copy.deepcopy(fullfillment_res)
  res['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech'] = res_string
  res['fulfillmentText'] = res_string
  return res


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)