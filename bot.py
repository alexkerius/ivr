import telebot
#Создание  бота с помощью API
bot = telebot.TeleBot("5748444681:AAEfGrg8agiJalbqt15po3t8MItOGNrl2A4",parse_mode = "HTML")
#Бот прослушивает чат на наличие команды start
@bot.message_handler(commands = ["start"])
#Функция по обработке команды
def say_hello(message):
    bot.send_message(message.chat.id,"<b>Hello, Telebot!</b>")
#Бот бесконечно работает
bot.infinity_polling(none_stop = True)