from flask import *
from flask_cors import CORS
import json
import os
from os import environ
from Bard import Chatbot as bard
from EdgeGPT import Chatbot, ConversationStyle
import asyncio
import nest_asyncio
nest_asyncio.apply()

token = 'VAietGsq4ZPagdjVWnHT8ts3l7ocT7BJmdhy-a8aNHBvA2t5Mp1XIhBH85QrVWJ6s71NAg.'
token = 'VAgxd4MZoUNzZ3GolhYaQ2l1QqgmftLxdBdXLUltRO8rSYmT2kezHZnQMCKB66Sl8CyFmw.'

chatbot = bard(token)
bingBot = Chatbot(cookiePath='./cookies.json')

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['POST'])
async def send():
    data = request.json
    loop = asyncio.get_event_loop()
    resp = await loop.run_in_executor(asyncio.run(gen_response_bing(data['body'])))
    return jsonify({'resp' : resp})

async def gen_response(question):
    raw = await chatbot.ask(question)
    return(raw['content'])

async def gen_response_bing(question):
    out = await bingBot.ask(prompt=question, conversation_style=ConversationStyle.creative, wss_link="wss://sydney.bing.com/sydney/ChatHub")
    return(out['item']['messages'][1]['text'])
