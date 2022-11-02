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
	url = f'https://api.telegram.org/bot{Token}/sendMessage'
	print(url)
	pl = {
		"chat_id" : chat_id,
		"text" : text
		}
	re = requests.post(url,json=pl)
	print(re)
	return re
	
@app.route('/{}'.format(Token), methods=['GET','POST'])
def respond():
	if request.method == 'POST':
		msg = request.get_json()
		try:
		    chat_id, txt = tel_parse_message(msg)
		    if txt in ("hi","Hi","Hello","HELLO","hello"):
		        tel_send_message(chat_id,"Hello, world!")
		    elif txt in ("hola","holis","Hola","HOLA"):
		        tel_send_message(chat_id,"Hola Mundo!")
		    elif txt in ("Sergio","sergio","serch","serchw"):
		        tel_send_message(chat_id,"Hola perrin!")
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
	
@app.route('/enviarmsg'.format(Token),methods=['GET','POST'])
def enviarMsg():
	url = f'https://api.telegram.org/bot{Token}/sendMessage'
	print(url)
	msg = {
		"chat_id" : "@channelLuis_B_Ramos_Terry",
		"text" : "Prueba"	
		}
	print(msg)
	re = requests.post(url,json=msg)
	print(re)
	
	url2 = f'https://api.telegram.org/bot{Token}/Message'
	print(url2)
	msg2 = {
		"from" : "@channelSergW_bot",
		"sender_chat" : "@channelSergW_bot",
		"text" : "Prueba"	
		}
	print(msg2)
	re2 = requests.post(url2,json=msg2)
	print(re2)
	return {'val':'ok','status':200}
	

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

