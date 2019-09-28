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
            ],
            "suggestions": [
              {
                "title": "List all your Services"
              },
              {
                "title": "Subscription Plans"
              },
              {
                "title": "My Shipped Orders"
              },
              {
                "title": "Shipping Service"
              }
            ]
          }
        },
      }
    }

plans_res = {
        "intent": "actions.intent.OPTION",
        "data": {
          "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
          "listSelect": {
            "title": "Plans Available",
            "items": []
          }
        }
      }

@app.route('/dialogflow', methods=['POST'])
def  handle_dialoglow():
  app.logger.warning(pprint.pformat(request.json))
  x = request.json['queryResult']['intent']['displayName']
  res_string = ""
  res = copy.deepcopy(fullfillment_res)

  if x == 'Order':
    o_no = int(request.json['queryResult']['parameters']['OrderNumber'])
    shipping_order = client.test['shipping'].find_one({'id': o_no})
    # print(shipping_order)
    res_string = f'Your Order with shipment ID {shipping_order["id"]}, shipped to {shipping_order["to_street"]}, {shipping_order["to_city"]}, {shipping_order["to_state"]} is scheduled to be delivered on {shipping_order["delivery_date"].strftime("%d %B %Y")}'
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
  elif x == 'Plans':
    plans = client.test['plans'].find()
    res_string = f'Please find the details of our Plans.'
    plans_json = copy.deepcopy(plans_res)
    for plan in plans:
      item = {"title": plan["name"], "description": plan["description"], "optionInfo": {"key": str(plan["id"]),"synonyms": []}}
      plans_json["data"]["listSelect"]["items"].append(item)
    res['payload']['google']['systemIntent'] = plans_json
  elif x == 'Shipping':
    shippings = client.test['shipping'].find()
    res_string = f'Here are your shipped orders and their status: '
    plans_json = copy.deepcopy(plans_res)
    plans_json["data"]["listSelect"]["title"] = "Your Shipped Orders"
    for ships in shippings:
      item = {"title": f'Order ID: {ships["id"]}', "description": f'Status: {ships["status"]}', "optionInfo": {"key": str(ships["id"]),"synonyms": []}}
      plans_json["data"]["listSelect"]["items"].append(item)
    res['payload']['google']['systemIntent'] = plans_json
  else:
    res_string = f'Sorry, I couldn\'t understand you. Please try again'

  res['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech'] = res_string
  res['fulfillmentText'] = res_string
  return res


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)