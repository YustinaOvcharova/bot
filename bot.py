import telebot
from telebot import types
bot = telebot.TeleBot('631459005:AAEfDu6UItyzj-d3PoLP6Ctm5NdkABJTmZk')

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Hi, how can I help u?")
    elif message.text == "/help":\
        bot.send_message(message.from_user.id, "Say hi")
    else:
        bot.send_message(message.from_user.id, "I do not understand u. Type /help.")


bot.polling(none_stop=True, interval=0)

name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "What is ur name?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Type /reg')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'What is ur surname?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message('How old r u?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0:
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Numbers, please')
      keyboard = types.InlineKeyboardMarkup()
      key_yes = types.InlineKeyboardButton(text='Yep', callback_data='yes')

      keyboard.add(key_yes) #добавляем кнопку в клавиатуру
      key_no= types.InlineKeyboardButton(text='Nope', callback_data='no')
      keyboard.add(key_no)
      question = 'You are '+str(age)+' years old, your name is '+name+' '+surname+'?'
      bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        ...
        bot.send_message(call.message.chat.id, 'I will remember)')
    elif call.data == "no":
         ...
