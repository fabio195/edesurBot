# Imports

import telebot
import requests
import json
import demjson

# Variables

TOKEN = ''
bot = telebot.TeleBot(TOKEN)
data = requests.get("https://www.enre.gov.ar/paginacorte/js/data_EDS.js?")
response = data.text
info = response.replace('var data = ', '')
jsonCortes = demjson.decode(info)

# Code

class Corte:
  partido = ''
  localidad = ''

@bot.message_handler(commands=['start'])
def start_handler(message):
  start = bot.send_message(message.chat.id, "Bienvenido a edesurBot, ingrese su partido:")
  bot.register_next_step_handler(start, set_partido)

def set_partido(message):
  partido = message.text.upper()
  Corte.partido = partido
  local = bot.send_message(message.chat.id, "Gracias! Ahora ingrese su localidad:")
  bot.register_next_step_handler(local, set_localidad)

def set_localidad(message):
  localidad = message.text.upper()
  Corte.localidad = localidad
  check_corte(message)

def check_corte(message):
  print(Corte.partido)
  print(Corte.localidad)
  for corte in jsonCortes['cortesServicioBaja']:
    if corte['partido'] == Corte.partido:
      if corte['localidad'] == Corte.localidad:
        bot.send_message(message.chat.id, "Hay corte de energía en tu zona")

for corte in jsonCortes['cortesServicioBaja']:
  if corte['partido'] == 'CAPITAL':
    print(corte)

bot.polling()
