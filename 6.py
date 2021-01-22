import pyowm
import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Portuguese
owm = OWM('your-api-key', config_dict)

owm = pyowm.OWM('62c2980e8419f3fad2f1c8f805589918')
#, language = "ru"
bot = telebot.TeleBot("1542012807:AAGfcUNZoV9xDP9N9rZbAM6H3InfuLSSZGU")
#, parse_mode=None
@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place( message.text )
#
    w = observation.weather
    temp=w.temperature('celsius')["temp"]
    answer=' В городе ' +message.text + ' сейчас ' + w.detailed_status+"."
    #+"/n"
    #+ place
    answer+=  'Температура  сейчас = ' + str(temp)  +"."
    if temp < -20:
        answer+=(' Сейчас очень холодно , одевай дубленку!')
    elif temp < -10:
        answer+=(' Сейчас прохладно , одевай кожанку!')
    else:
#temp > 0:
        answer+=(' Сейчас жарко, гуляй смело!')
# moscow


    bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True)

	
