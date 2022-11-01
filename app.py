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

def parse_message(msg):
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
	
@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		msg = request.get_json()
		chatid,txt = parse_message(msg)
		if txt in ('HI','Hi','hi','Hello','HELLO'):
			tel_send_message(chatid,'Hello!!')
		elif txt in ('hola','Hola','HOLA','HolA'):
			tel_send_message(chatid,"Hola!!")
		else:
			tel_send_message(chatid,'from webhook')
		return Response('ok', status=200)
	else:
		return "<h1>Bienvenido</h1>"



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

