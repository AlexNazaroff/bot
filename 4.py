import telebot

bot = telebot.TeleBot("1403684371:AAHsIRXpBDZ2Oq1ZKJmpF1Cr3UX-hx44iy4", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, message.text)
bot.polling(none_stop=True)

	
