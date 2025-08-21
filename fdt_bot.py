import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8326999962:AAGHsm79Phu5njRrj1FmA4xHIJCv9uykSRc"  # замени на токен из BotFather

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Клавиатура ---
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(
    [KeyboardButton("ℹ️ Что такое ФДТ?"), KeyboardButton("💡 Преимущества ФДТ")],
    [KeyboardButton("📋 Показания"), KeyboardButton("⚠️ Ограничения")],
    [KeyboardButton("📍 Где проводится ФДТ?"), KeyboardButton("👨‍⚕️ Консультация врача")],
    [KeyboardButton("ℹ️ Об авторе")]
)

# --- Обработчики ---
@dp.message(commands=["start", "help"])
async def start(message: types.Message):
    await message.answer("Привет! Я бот по фотодинамической терапии (ФДТ).", reply_markup=keyboard)

@dp.message()
async def answer(message: types.Message):
    if message.text == "ℹ️ Что такое ФДТ?":
        await message.answer("ФДТ — это метод лечения с использованием фотосенсибилизатора и лазера.")
    elif message.text == "💡 Преимущества ФДТ":
        await message.answer("✔️ Минимальная травматичность\n✔️ Селективность\n✔️ Повторяемость процедуры")
    elif message.text == "📋 Показания":
        await message.answer("ФДТ применяется при лечении онкологии, дерматологии и офтальмологии.")
    elif message.text == "⚠️ Ограничения":
        await message.answer("Противопоказания: фотодерматозы, тяжелые сопутствующие болезни и др.")
    elif message.text == "📍 Где проводится ФДТ?":
        await message.answer("ФДТ проводится в специализированных клиниках. Уточните у врача.")
    elif message.text == "👨‍⚕️ Консультация врача":
        await message.answer("Для консультации обратитесь в клинику или напишите врачу.")
    elif message.text == "ℹ️ Об авторе":
        await message.answer("Автор бота: @MSL72Rph")
    else:
        await message.answer("Пожалуйста, выберите вариант из меню.")

# --- Запуск ---
async def main():
    print("🤖 FDT бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




