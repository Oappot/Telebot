import telebot
from math import sqrt

token = ''
bot = telebot.TeleBot(token)

//блок с вызываемыми функциями

//для факторала
def factorial2(message):
    
    a = int(message.text)
    i = 1
    answer = 1
    while i <= a:
        answer *= i
        i += 1
    bot.send_message(str(a) + "! = " + str(answer))
//для queq
def queq2(message):
    
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        x1 = (- b + sqrt(d)) / (2 * a)
        x2 = (- b - sqrt(d)) / (2 * a)
        bot.send_message(message.chat.id, text = "Discriminant = " + str(d) + ". x1 = " + str(x1) + "   x2 = " + str(x2))
    elif d == 0:
        x = (- b) / (2 * a)
        bot.send_message(message.chat.id, text = "Discriminant = 0. x1 = x2 = " + str(x))
    else:
        bot.send_message(message.chat.id, text = "Discriminant = " + str(d) + ".")
//для biqueq
def biqueq2(message):
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        y1 = (- b + sqrt(d)) / (2 * a)
        y2 = (- b - sqrt(d)) / (2 * a) 
        x1 = sqrt(y1)
        x2 = sqrt(y2)
        bot.send_message(message.chat.id, text = "Discriminant = " + str(d) + ". x1 = " + str(x1) + "   x2 = " + str(x2))
    elif d == 0:
        y = (- b) / (2 * a)
        x = sqrt(y)
        bot.send_message(message.chat.id, text = "Discriminant = 0. x1 = x2 = " + str(x))
    else:
        bot.send_message(message.chat.id, text = "Discriminant = " + str(d) + ".")


@bot.message_handler(commands = ['factorial'])
def factorial(message):
    
    bot.send_message(message.chat.id, text = "Your number?")
    factorial2(message.text)
    
@bot.message_handler(commands = ['queq'])
def queq1(message):
    
    bot.send_message(message.chat.id, text = "Put coefficient a")
    a = int(message.text)
    bot.send_message(message.chat.id, text = "Put coefficient b")
    b = int(message.text)
    bot.send_message(message.chat.id, text = "Put coefficient c")
    c = int(message.text)
    queq2(message.text)

@bot.message_handler(commands = ['biqueq'])
def biqueq1(message):
    
    bot.send_message(message.chat.id, text = "Put coefficient a")
    a = int(message.text)
    bot.send_message(message.chat.id, text = "Put coefficient b")
    b = int(message.text)
    bot.send_message(message.chat.id, text = "Put coefficient c")
    c = int(message.text)
    biqueq2(message.text)


while True:
    try:
        bot.polling(none_stop=True)
