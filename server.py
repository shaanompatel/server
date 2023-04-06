from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import json
import os
from os import environ
from Bard import Chatbot
token = 'VAietGsq4ZPagdjVWnHT8ts3l7ocT7BJmdhy-a8aNHBvA2t5Mp1XIhBH85QrVWJ6s71NAg.'
token = 'VAgxd4MZoUNzZ3GolhYaQ2l1QqgmftLxdBdXLUltRO8rSYmT2kezHZnQMCKB66Sl8CyFmw.'
chatbot = Chatbot(token)


app = Flask(__name__)
CORS(app)

resp = "Nothing"

@app.route('/', methods=['POST', 'GET'])
def hello():
    global resp
    data = request.data

    if data != bytearray([]):
         data = json.loads(data.decode('utf-8'))
         print(data)
         resp = gen_response(data['body'])
    return jsonify({'resp' : resp})


def gen_response(question):
    raw = chatbot.ask(question)
    return(raw['content'])

