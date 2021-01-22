import pyowm
import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Portuguese
owm = OWM('your-api-key', config_dict)

owm = pyowm.OWM('62c2980e8419f3fad2f1c8f805589918')

bot = telebot.TeleBot("1403684371:AAHsIRXpBDZ2Oq1ZKJmpF1Cr3UX-hx44iy4", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr = owm.weather_manager()
    observation = mgr( message.text )
#.weather_at_place
    w = observation.weather
    temp=w.temperature('celsius')["temp"]
    answer='В городе '  + ' сейчас ' + w.detailed_status+"/n"
    #+ place
    answer+=  'Температура  сейчас около' + str(temp)  +"/n/n"
    if temp < 20:
        answer+=('Сейчас очень холодно , одевай дубленку!')
    elif temp < 10:
        answer+=('Сейчас прохладно , одевай кожанку!')
    else:
#temp > 20:
        answer+=('Сейчас жарко, гуляй смело!')
# moscow


    bot.send_message(message.chat.id, message.text)
bot.polling(none_stop=True)

	
