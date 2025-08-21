from aiogram import Bot, Dispatcher, types
import asyncio

TOKEN = "8416977089:AAG49nmrwX1RuCSxJL3zlqaTgeLLa8jgs3Y"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def order_handler(message: types.Message):
    if message.web_app_data:  # ловим данные из WebApp
        data = message.web_app_data.data
        await message.answer(f"📦 Ваш заказ:\n{data}")

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))