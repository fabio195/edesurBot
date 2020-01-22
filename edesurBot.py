# Imports

import telebot
import requests
import json
import demjson

# Variables

TOKEN = ''
bot = telebot.TeleBot(TOKEN)
jsonCortes = requests.get("https://www.enre.gov.ar/paginacorte/js/data_EDS.js?").text
jsonCortes = jsonCortes.replace('var data = ', '')
jsonCortes = demjson.decode(jsonCortes)

class Corte:
  partido = ''
  localidad = ''

print("Bot iniciado")

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

  for corte in jsonCortes['cortesServicioBaja']:
    if corte['partido'] == Corte.partido and corte['localidad'] == Corte.localidad:
      existeLocalidadPartido = True
    else:
      existeLocalidadPartido = False

  if existeLocalidadPartido:
    bot.send_message(message.chat.id, "Hay cortes en tu zona")
  else:
    bot.send_message(message.chat.id, "No hay cortes en tu zona")

bot.polling()
