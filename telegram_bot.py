import telebot
from telebot import types

from DeliveryManager.DeliveryMan import DeliveryMan
from DeliveryManager.DeliveryManager import DeliveryManager

# Создать объект бота
bot = telebot.TeleBot('6283121546:AAEIneaKXB6x74vKw2T0-ocFVe7KL9wiNd4')
MANAGER = DeliveryManager()
STAT = {}
NOW_ASK = [0]
ACCEPT_ANS = {}
CLOSE_ANS = {}
UNWANTED_ORDER = {}
ORDER_QUEUE = []


def ask_deliveryman(id: int, road_length: float):
    if id not in UNWANTED_ORDER[ORDER_QUEUE[0]]:
        ACCEPT_ANS[id] = False
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Готов')
        btn2 = types.KeyboardButton('Не готов')
        markup.add(btn1, btn2)
        bot.send_message(id, f'Заказ: {ORDER_QUEUE[0]}\nРасстояние: '
                             f'{road_length}\nГотовы взять заказ?',
                         reply_markup=markup)


def ask_deliveryman_to_skip(id: int):
    if not CLOSE_ANS[id]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Закончил')
        btn2 = types.KeyboardButton('Не закончил')
        markup.add(btn1, btn2)
        bot.send_message(id, 'Закончили ли вы заказ?', reply_markup=markup)


# Регистрируем обработчик сообщений
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да')
    btn2 = types.KeyboardButton('Нет')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id,
                     'Привет, готов начать работу?',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Да':
        STAT[message.from_user.id] = []
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('1')
        btn2 = types.KeyboardButton('2')
        btn3 = types.KeyboardButton('3')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Хорошо, выбери район',
                         reply_markup=markup)
    elif message.text == '1' or message.text == '2' or message.text == '3':
        STAT[message.from_user.id].append(int(message.text))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('CAR')
        btn2 = types.KeyboardButton('BICYCLE')
        btn3 = types.KeyboardButton('SCOOTER')
        btn4 = types.KeyboardButton('AFOOT')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Хорошо, выбери транспортное '
                                               'средство',
                         reply_markup=markup)
    elif message.text == 'CAR' or message.text == 'BICYCLE' or message.text \
            == 'SCOOTER' or message.text == 'AFOOT':
        STAT[message.from_user.id].append(message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Ок')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Отлично жди заказы от нас)',
                         reply_markup=markup)
        tuple_str = [str(int(message.from_user.id))]
        new_deliveryman = DeliveryMan(tuple_str,
                                      int(STAT[message.from_user.id][0]) - 1,
                                      False,
                                      STAT[message.from_user.id][1], 0, ' ', 0)
        MANAGER.add_deliveryman(new_deliveryman)
    elif message.text == 'Готов':
        if NOW_ASK[0] == message.from_user.id:
            ACCEPT_ANS[message.from_user.id] = True
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Ок')
            markup.add(btn1)
            bot.send_message(message.from_user.id, 'Время ожидания истекло',
                             reply_markup=markup)
    elif message.text == 'Закончил':
        CLOSE_ANS[message.from_user.id] = True
    elif message.text == 'Не готов':
        UNWANTED_ORDER[ORDER_QUEUE[0]].append(message.from_user.id)
    elif message.text == 'Нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Ок')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Блин, а я уже обрадовался(',
                         reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Извините, не распознали вашу '
                                               'команду')
