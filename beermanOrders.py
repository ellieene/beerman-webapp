import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
)
from aiogram.filters import Command

# ---- Твой токен ----
TOKEN = "8416977089:AAG49nmrwX1RuCSxJL3zlqaTgeLLa8jgs3Y"
ADMIN_USERNAME = "ellieene"   # проверь правильность
MANAGER_CHAT_ID = None        # сюда можно вставить ID группы/чата для заказов

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Кнопка с MiniApp ---
def menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(
                text="🛒 Сделать заказ",
                web_app=WebAppInfo(url="https://YOUR-SITE/index.html")  # <-- вставь ссылку на index.html
            )
        ]],
        resize_keyboard=True
    )

# --- /start ---
@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer(
        "Привет 👋\nВы можете сделать заказ через кнопку ниже:",
        reply_markup=menu_keyboard()
    )

# --- /menu ---
@dp.message(Command("menu"))
async def menu(msg: types.Message):
    await msg.answer("Открой меню:", reply_markup=menu_keyboard())

# --- Приём данных из WebApp ---
@dp.message(F.web_app_data)
async def webapp_handler(msg: types.Message):
    data = msg.web_app_data.data  # JSON-строка
    await msg.answer(f"✅ Заказ получен:\n{data}")

    # Отправляем заказ менеджеру
    if MANAGER_CHAT_ID:
        await bot.send_message(MANAGER_CHAT_ID, f"📦 Новый заказ:\n{data}")

# --- Запуск ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())