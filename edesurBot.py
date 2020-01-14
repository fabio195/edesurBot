# Imports

#import telebot
import requests
import json
import demjson

# Variables

#TOKEN = ''
#bot = telebot.telebot(TOKEN)
data = requests.get("https://www.enre.gov.ar/paginacorte/js/data_EDS.js?")
response = data.text
info = response.replace('var data = ', '')
jsonCortes = demjson.decode(info)

# Code

for corte in jsonCortes['cortesServicioBaja']:
  if corte['partido'] == 'CAPITAL':
    print(corte)
