import os
import telebot
from telebot import types

# Токен берется из секретов GitHub
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("🎮 Предзаказ Blood on Both Sides", callback_data='preorder')
    btn2 = types.InlineKeyboardButton("📦 Коллекционное издание", callback_data='collector')
    btn3 = types.InlineKeyboardButton("👕 Мерч и Фигурки", callback_data='merch')
    btn4 = types.InlineKeyboardButton("💬 Поддержка", callback_data='support')
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.send_message(
        message.chat.id, 
        "Добро пожаловать в лавку братьев Воронцовых! Выберите раздел:", 
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    responses = {
        'preorder': "Цифровая копия платформера для PC. Цена: $15. Релиз: 1919 год.",
        'collector': "Стилбук, артбук на 100 страниц и копия приказа. Цена: $50.",
        'merch': "Доступны пиксельные фигурки Петра (с обрезом) и Павла (с шашкой). Цена: $25.",
        'support': "Опишите вашу проблему, и дежурный телеграфист свяжется с вами."
    }
    bot.send_message(call.message.chat.id, responses.get(call.data, "Неизвестный запрос"))
    bot.answer_callback_query(call.id)

if __name__ == '__main__':
    print("Бот запущен. Ожидание команд...")
    bot.polling(none_stop=True)
