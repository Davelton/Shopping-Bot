import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from config import TOKEN
from buttons import *
from Payment import order_1, pre_checkout_query, successful_payment, order_2, order_3, order_4

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Добро Пожаловать", reply_markup=menu)


@dp.message(F.text == "Категория⌨️")
async def category(message: Message):
    await message.answer("Выберите кнопку", reply_markup=catMenu1)


@dp.message(F.text == "Профиль🧰")
async def profile(message: Message):
    await message.answer("💼На вашем счету:$100 mlrd\n"
                         "💸Все Эти деньги Виртуальные\n", reply_markup=menu)


@dp.message(F.text == "Поддержка📞")
async def support(message: Message):
    await message.answer("По всем вопросам обращаться к @Spxce01\n", reply_markup=menu)


@dp.message(F.text == "Черная Икра🫙")
async def product_1(message: Message):
    await message.answer_photo(photo="https://www.livemaster.ru/item/43815378-suveniry-i-podarki-chernaya-ikra-v-banke-zhemchug-biser-dlya-",
                               caption="Черная Икра Natural\n"
                                       "Black Original 100%\n", reply_markup=inlineBtn1)


@dp.message(F.text == "🔙Back")
async def support(message: Message):
    await message.answer("Выберите кнопку",reply_markup=menu)


dp.callback_query.register(order_1, F.data == "pay_1")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


@dp.message(F.text == "Соленные огурцы🥒")
async def product_2(message: Message):
    await message.answer_photo(photo="https://dyadya-vanya.ru/uploads/product/big/cf/07/0149b089a778d2bacb40a79870ac27ecc0ae633178544b7f5.jpg",
                               caption="Огурчики соленые Дядя Ваня\n"
                                       "Соленные 100%\n", reply_markup=inlineBtn2)


dp.callback_query.register(order_2, F.data == "pay_2")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


@dp.message(F.text == "Колбаса Докторская🫘")
async def product_3(message: Message):
    await message.answer_photo(photo="https://belmostorg.ru/image/cache/catalog/grodno/kolb-varen-doktorskaya-klassik-extra-1200x800.jpg",
                               caption="Вареная колбаса докторская\n"
                                       " Очень Сочная\n", reply_markup=inlineBtn3)


dp.callback_query.register(order_3, F.data == "pay_3")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


@dp.message(F.text == "Чипсы Доритос🥠")
async def product_4(message: Message):
    await message.answer_photo(photo="https://sweetopt24.ru/wp-content/uploads/2021/01/doritos-kukuruznye-chipsy-tortilla-nacho-cheese-160gr-2.jpg",
                               caption="Доритос кукурузные чипсы\n"
                                       " Очень вкусная\n", reply_markup=inlineBtn4)


dp.callback_query.register(order_4, F.data == "pay_4")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
