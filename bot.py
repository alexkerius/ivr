import telebot
from telebot import types
import file_for_price
#Создание  бота с помощью API
bot = telebot.TeleBot("5748444681:AAEfGrg8agiJalbqt15po3t8MItOGNrl2A4",parse_mode = "HTML")
#Бот прослушивает чат на наличие команды start
@bot.message_handler(commands = ["start"])
#Функция по обработке команды
def start(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Ввести",callback_data="enter")
    markup.add(button)
    bot.send_message(message.chat.id,f'''<b>Привет, {message.from_user.username}!</b>\nВ этом боте вы можете обменивать <b>Биток</b> на рубли!\nВведите кол-во рублей,на которые хотите приобрести биткоин:''',
    reply_markup=markup)

@bot.message_handler(content_types=["text"])
def reaction(message):
    if message.text == "Ввести":
        bot.send_message(message.chat.id,"Введите в формате (число) RUB")
    elif isinstance(int(message.text),int) == True:
        user_price = int(message.text)/int(file_for_price.price())
        bot.send_message(message.chat.id,f"{user_price:.8f}")
        
@bot.callback_query_handler(func=lambda callback_data:True)
def cb_reaction(call):
    if call.data == "enter":
        bot.send_message(call.message.chat.id,"Введите в формате (число) RUB")
    
#Бот бесконечно работает
bot.infinity_polling(none_stop = True)
