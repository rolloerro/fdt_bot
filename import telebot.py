import telebot
from telebot import types
import os

# Подставь свой реальный токен здесь
TOKEN = "8326999962:AAGHsm79Phu5njRrj1FmA4xHIJCv9uykSRc"
bot = telebot.TeleBot(TOKEN)

# Главное меню с эмодзи
def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        "💡 Что такое ФДТ",
        "💊 Препарат РАДАХЛОРИН",
        "⭐ Преимущества метода",
        "📋 Этапы лечения",
        "📍 Где применяется",
        "📄 Скачать брошюру",
        "🎓 Обучение врачей",
        "❓ FAQ / Контакты"
    ]
    for b in buttons:
        keyboard.add(b)
    return keyboard

# Старт
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Здравствуйте! 👋 Добро пожаловать в информационный бот по ФДТ.\nВыберите раздел:",
        reply_markup=main_menu()
    )

# Ответы на кнопки
@bot.message_handler(func=lambda m: True)
def answer(message):
    text = message.text.strip()

    if text == "💡 Что такое ФДТ":
        bot.send_message(
            message.chat.id,
            "Фотодинамическая терапия (ФДТ) – современный метод лечения опухолей, "
            "основанный на активации светочувствительных препаратов с последующим разрушением патологических клеток.\n\n"
            "Метод минимально инвазивный и высокоэффективный."
        )

    elif text == "💊 Препарат РАДАХЛОРИН":
        bot.send_message(
            message.chat.id,
            "Радахлорин – фотосенсибилизатор для ФДТ. Используется для лечения онкологических и дерматологических заболеваний.\n\n"
            "Дозировки: 10мг, 15мг."
        )

    elif text == "⭐ Преимущества метода":
        bot.send_message(
            message.chat.id,
            "✅ Минимальное повреждение здоровых тканей\n"
            "✅ Высокая эффективность на ранних стадиях\n"
            "✅ Быстрое восстановление после процедуры\n"
            "✅ Возможность повторного применения при рецидивах"
        )

    elif text == "📋 Этапы лечения":
        bot.send_message(
            message.chat.id,
            "1️⃣ Введение фотосенсибилизатора\n"
            "2️⃣ Ожидание накопления препарата в опухоли\n"
            "3️⃣ Воздействие света специфической длины волны\n"
            "4️⃣ Контроль результата и последующее наблюдение"
        )

    elif text == "📍 Где применяется":
        bot.send_message(
            message.chat.id,
            "🏥 Онкологические клиники\n"
            "💉 Дерматологические центры\n"
            "🧬 Исследовательские лаборатории\n\n"
            "Метод активно применяется как в РФ, так и за рубежом."
        )

    elif text == "📄 Скачать брошюру":
        brochure_path = os.path.join(os.getcwd(), "001. Брошюра ФДТ постранично.pdf")
        if os.path.exists(brochure_path):
            with open(brochure_path, 'rb') as f:
                bot.send_document(message.chat.id, f)
        else:
            bot.send_message(message.chat.id, "Брошюра пока недоступна 😔")

    elif text == "🎓 Обучение врачей":
        bot.send_message(
            message.chat.id,
            "✅ Практические занятия по фотодинамической терапии\n"
            "✅ Выдача сертификата по окончании курса\n\n"
            "Для записи и деталей обращайтесь: @MSL72Rph",
            reply_markup=main_menu()
        )

    elif text == "❓ FAQ / Контакты":
        bot.send_message(
            message.chat.id,
            "📞 Для связи и консультации: @MSL72Rph",
            reply_markup=main_menu()
        )

    else:
        bot.send_message(
            message.chat.id,
            "Пожалуйста, выберите раздел из меню ниже:",
            reply_markup=main_menu()
        )

print("🤖 FDT Bot запущен...")
bot.polling(none_stop=True)
