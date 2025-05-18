from flask import Blueprint, request, jsonify
from openai import AzureOpenAI
import os, redis, json
from .cards import dete_card_type
from .prompt_buider import build_prompt

bp = Blueprint("api",__name__)
#rdb = redis.from_url(os.getenv("REDIS_URL","redis://localhost:6379"))

client = AzureOpenAI(api_version="2024-12-01-preview")

@bp.route("/chat",methods=['POST'])
def chat():
    msg = request.get_json(force=True)['message']
    hist = [] #rdb.lrange("chat",0,-1)
    card = dete_card_type(msg)
    prompt = build_prompt(card, hist, msg)
    response = client.chat.completions.create(messages=prompt,
                                              model="gpt-4o-mini", temperature=0.2)
    assistant_res = response.choices[0].message.content
    #rdb.rpush("chat",msg,assistant_res)
    return jsonify({"answer":assistant_res})