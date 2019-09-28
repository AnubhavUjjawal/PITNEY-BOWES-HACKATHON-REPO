import logging
import sys
import pprint
from eve import Eve
from flask import Flask, escape, request

app = Eve()

@app.route('/dialogflow', methods=['POST'])
def  handle_dialoglow():
  app.logger.warning(pprint.pformat(request.json))
  return f'Success'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)