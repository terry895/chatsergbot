from flask import Flask
from flask import request
from flask import Response
import requests
import telegram
import re

global bot

Token = "5436833488:AAEySERdTwwKIqt-7gYDvZAEDnCJ9NWymgI"
URL = "https://chatbotsergio.herokuapp.com/"
bot = telegram.Bot(token=Token)

app = Flask(__name__)

def tel_parse_message(msg):
	print("msg:",msg)
	chat_id = msg['message']['chat']['id']
	text = msg['message']['text']
	print("chat_id", chat_id)
	print("text",text)
	return chat_id,text

def tel_send_message(chat_id,text):
	url = bot.sendMessage()
	print(url)
	pl = {
		"chat_id" : chat_id,
		"text" : text
		}
	re = requests.post(url,json=pl)
	print(re)
	return re
	
@app.route('/{}'.format(Token), methods=['GET','POST'])
def index():
	if request.method == 'POST':
		msg = request.get_json()
		try:
		    chat_id, txt = tel_parse_message(msg)
		    if txt == "hi":
		        tel_send_message(chat_id,"Hello, world!")
		    elif txt == "image":
		        tel_send_image(chat_id)
	 
		    else:
		        tel_send_message(chat_id, 'from webhook')
		except:
		    print("from index-->")
	 
		return Response('ok', status=200)
	else:
		return "<h1>Welcome!</h1>"

@app.route('/', methods=['GET','POST'])
def index():
	return "<h1>Welcome!</h1>"

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
   s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=Token))
   print(s)
   if s:
       return "webhook setup ok"
   else:
       return "webhook setup failed"	
		
if __name__ == '__main__':
   app.run(threaded=True)

