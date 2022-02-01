import telebot
from telebot import types
import config
from pony.orm import *
from ORM import *
import random

# bot = telebot.TeleBot(TOKEN)
bot = telebot.TeleBot(config.TOKEN)

# command /start
@bot.message_handler(commands="start")
def start(message):

	# types
	item1 = types.KeyboardButton("Огoнь🔥")
	item2 = types.KeyboardButton("Вoда💦")
	item3 = types.KeyboardButton("Зeмля🌍")

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(item1, item2, item3)# add types
	bot.send_message(message.chat.id, "Начинаем, какую фотографию прислать?", reply_markup=markup)

# sends_photos
@bot.message_handler(content_types="text")
def text(message):

	# Fire
	if message.text == "Огoнь🔥":
		bot.delete_message(message.chat.id, message.message_id)
		link_photo = random.choice([fire1, fire2, fire3])
		bot.send_photo(message.chat.id, open(link_photo, "rb"))

	# Water
	if message.text == "Вoда💦":
		bot.delete_message(message.chat.id, message.message_id)

		item1 = types.KeyboardButton("Мoрe")
		item2 = types.KeyboardButton("Рекa")
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(item1, item2)

		bot.send_message(message.chat.id, "Выберите какой тип воды", reply_markup=markup)

	if message.text == "Мoрe":
		bot.delete_message(message.chat.id, message.message_id)

		item1 = types.KeyboardButton("Еще Морe")
		item2 = types.KeyboardButton("Нaзaд")
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(item1, item2)

		link_photo = random.choice([water1, water2, water3])
		bot.send_photo(message.chat.id, open(link_photo, "rb"), reply_markup=markup)

	if message.text == "Рекa":
		bot.delete_message(message.chat.id, message.message_id)

		item1 = types.KeyboardButton("Еще Рeкy")
		item2 = types.KeyboardButton("Нaзaд")
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(item1, item2)

		link_photo = random.choice([water4, water5, water6])
		bot.send_photo(message.chat.id, open(link_photo, "rb"), reply_markup=markup)

	# more sea
	if message.text == "Еще Морe":
		bot.delete_message(message.chat.id, message.message_id)

		item1 = types.KeyboardButton("Еще Морe")
		item2 = types.KeyboardButton("Нaзaд")
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(item1, item2)

		link_photo = random.choice([water1, water2, water3])
		bot.send_photo(message.chat.id, open(link_photo, "rb"), reply_markup=markup)

	# more river
	if message.text == "Еще Рeкy":
		bot.delete_message(message.chat.id, message.message_id)

		item1 = types.KeyboardButton("Еще Рeкy")
		item2 = types.KeyboardButton("Нaзaд")
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(item1, item2)

		link_photo = random.choice([water4, water5, water6])
		bot.send_photo(message.chat.id, open(link_photo, "rb"), reply_markup=markup)

	# back
	if message.text == "Нaзaд":
		bot.delete_message(message.chat.id, message.message_id)

		item1 = types.KeyboardButton("Огoнь🔥")
		item2 = types.KeyboardButton("Вoда💦")
		item3 = types.KeyboardButton("Зeмля🌍")
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(item1, item2, item3)

		bot.send_message(message.chat.id, "Выбирайте)", reply_markup=markup)

	# earth
	if message.text == "Зeмля🌍":
		bot.delete_message(message.chat.id, message.message_id)
		link_photo = random.choice([earth1, earth2, earth3])
		bot.send_photo(message.chat.id, open(link_photo, "rb"))

# RUN
bot.polling(none_stop=True, interval=0)