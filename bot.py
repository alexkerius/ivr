import telebot
from telebot import types
#Создание  бота с помощью API
bot = telebot.TeleBot("5748444681:AAEfGrg8agiJalbqt15po3t8MItOGNrl2A4",parse_mode = "HTML")
#Бот прослушивает чат на наличие команды start
@bot.message_handler(commands = ["start"])
#Функция по обработке команды
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Ввести")
    markup.add(button)
    bot.send_message(message.chat.id,f'''<b>Привет, {message.from_user.username}!</b>\nВ этом боте вы можете обменивать <b>Биток</b> на рубли!\nВведите кол-во рублей,на которые хотите приобрести биткоин:''',reply_markup=markup)

@bot.message_handler(content_types=["text"])
def reaction(message):
    if message.text == "Ввести":
        bot.send_message(message.chat.id,"Введите в формате (число) RUB")
    
#Бот бесконечно работает
bot.infinity_polling(none_stop = True)
