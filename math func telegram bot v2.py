import telebot
from telebot import types
import math

BOT_TOKEN = "5073900951:AAGReIU3vFapYjn0D5FNDdAStUmd79kQ1rc"
file_name = 'new.txt'
bot = telebot.TeleBot(BOT_TOKEN)
print("bot is running now! ")


class Values(object):
    data = dict()
    his = dict()
    # in this dictionary ordered by this format { user_id : [square, square_root, prime, lcm, hcf] }
    help_message = "This bot made for some mathematics functions\nyou can get square of given value " \
                   "\nsquare root of given value  \nalso you can check prime numbers" \
                   " \nand you can get history by using /his command" \
                   "\n............................................................ \nThis bot made by yosh"


v = Values

temp = open(file_name, 'r')
all_lines = temp.readlines()
v.data = eval(all_lines[0])
v.his = eval(all_lines[1])
temp.close()


def is_prime_num(num):
    """Return boolean value of given number as a prime or not"""
    return not (bool(len([i for i in range(2, num) if num % i == 0])))


def least_common_mul(num_list: list) -> int:
    max_num = max(num_list)
    temp0 = 1
    temp_list = list()
    while True:
        num_list = [i for i in num_list if i != 1]
        if len(num_list) == 0:
            break
        for i in range(2, 1 + max_num):
            if num_list[0] % i == 0:
                temp0 *= i
                for j in num_list:
                    if j % i == 0:
                        temp_list.append(j // i)
                    else:
                        temp_list.append(j)
                num_list.clear()
                num_list = num_list + temp_list
                temp_list.clear()
    return temp0


def highest_common_fac(num_list: list) -> int:
    hcf = num_list[0]
    for i in range(1, len(num_list)):
        hcf = math.gcd(hcf, num_list[i])
    return hcf


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print('welcome message')
    bot.reply_to(message, f"Howdy {message.from_user.first_name}, how are you doing?")
    bot.send_message(message.chat.id, "if you need some help use /help command !")

    but_square = types.InlineKeyboardButton('Square', callback_data=f'squ {message.chat.id}')
    but_square_root = types.InlineKeyboardButton('Square Root', callback_data=f'squr {message.chat.id}')
    but_prime = types.InlineKeyboardButton('Prime', callback_data=f'prime {message.chat.id}')
    but_lcm = types.InlineKeyboardButton('Least Common Multiple', callback_data=f'lcm {message.chat.id}')
    but_hcf = types.InlineKeyboardButton('Highest Common Factor', callback_data=f'hcf {message.chat.id}')

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(but_square, but_square_root)
    keyboard.add(but_prime)
    keyboard.add(but_hcf)
    keyboard.add(but_lcm)
    bot.send_message(message.chat.id, text='Choose Option ', reply_markup=keyboard)

    if message.chat.id not in v.his.keys():
        v.his[message.chat.id] = []
    if message.chat.id not in v.data.keys():
        v.data[message.chat.id] = None


@bot.message_handler(commands=['help'])
def help_message(message):
    print('help')
    bot.reply_to(message, v.help_message)


@bot.message_handler(commands=['his'])
def his_message(message):
    temp0 = '\n'.join(v.his.get(message.chat.id))
    bot.reply_to(message, temp0)


@bot.message_handler(regexp='hi')
def hi_message(message):
    print(v.data)
    bot.send_message(message.chat.id, 'Did someone call for help?')


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(callback):
    print(callback.data)
    data = callback.data.split()[0]
    id0 = callback.data.split()[-1]
    if data == 'squ':
        v.data[int(id0)] = data
        bot.send_message(id0, 'function set to find square')
    elif data == 'squr':
        v.data[int(id0)] = data
        bot.send_message(id0, 'function set to find square root')
    elif data == 'prime':
        v.data[int(id0)] = data
        bot.send_message(id0, 'function set to find prime')
    elif data == 'lcm':
        v.data[int(id0)] = data
        bot.send_message(id0, 'function set to find LMC')
    elif data == 'hcf':
        v.data[int(id0)] = data
        bot.send_message(id0, 'function set to find HCF')


@bot.message_handler(regexp='get')
def get_val(message):
    bot.send_message(message.chat.id, f'Currently you are in {v.data.get(message.chat.id)}')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message.text)
    if Values.data.get(message.chat.id) == 'squ' and message.text.isdigit():
        out = str(int(message.text) ** 2)
        bot.reply_to(message, out)
        log = f'square of {message.text} is {out}'
        v.his[message.chat.id].append(log)
    elif Values.data.get(message.chat.id) == 'squr' and message.text.isdigit():
        out = str(int(message.text) ** 0.5)
        bot.reply_to(message, out)
        log = f'square root of {message.text} is {out}'
        v.his[message.chat.id].append(log)
    elif Values.data.get(message.chat.id) == 'prime' and message.text.isdigit():
        out = str(is_prime_num(int(message.text)))
        bot.reply_to(message, out)
        log = f'check {message.text} as a prime and given {out}'
        v.his[message.chat.id].append(log)
    elif v.data.get(message.chat.id) == 'lcm':
        num_list = list(map(int, message.text.split()))
        out = str(least_common_mul(num_list))
        bot.reply_to(message, out)
        log = f'find lcm of {message.text} and given {out}'
        v.his[message.chat.id].append(log)
    elif v.data.get(message.chat.id) == 'hcf':
        num_list = list(map(int, message.text.split()))
        out = str(highest_common_fac(num_list))
        bot.reply_to(message, out)
        log = f'find hcf of {message.text} and given {out}'
        v.his[message.chat.id].append(log)
    else:
        bot.send_message(message.chat.id, 'error')

    file = open(file_name, 'w')
    file.write(str(v.data))
    file.write('\n')
    file.write(str(v.his))
    file.close()


bot.infinity_polling()
