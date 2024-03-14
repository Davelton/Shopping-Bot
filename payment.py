from aiogram import Bot, types
from aiogram.types import LabeledPrice, PreCheckoutQuery
from config import PAY_TOKEN


async def order_1(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Черная Икра",
                           description="Свежая,Натуральная,Качественная Черная Икра ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://cs1.livemaster.ru/storage/c6/7d/c8e61298320cb87cf6ec2fe566sg--suveniry-i-podarki-chernaya-ikra-v-banke-zhemchug-biser-dlya-.jpg", # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=565_000_00),
                               LabeledPrice(label="Скидка", amount=-55_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Черная Икра',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot): # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """

    await message.answer(msg)


async def order_2(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Натуральные,Соленные огурчики Дядя Ваня",
                           description="Хрустящие, вкусные, отличная закуска",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://dyadya-vanya.ru/uploads/product/big/cf/07/0149b089a778d2bacb40a79870ac27ecc0ae633178544b7f5.jpg", # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=40_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Огурчики Соленные',
                           request_timeout=15
                           )

async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot): # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_2(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_3(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Колбаса Докторская",
                           description="Сочная колбаса, вареное мясное",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://belmostorg.ru/image/cache/catalog/grodno/kolb-varen-doktorskaya-klassik-extra-1200x800.jpg", # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=65_000_00),
                               LabeledPrice(label="Скидка", amount=-15_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Колбаска Вареная',
                           request_timeout=15
                           )

async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot): # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_3(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_4(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Чипсы Doritos",
                           description="Сочная колбаса, вареное мясное",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://sweetopt24.ru/wp-content/uploads/2021/01/doritos-kukuruznye-chipsy-tortilla-nacho-cheese-160gr-2.jpg", # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Вкусные,кукурузные чипсы',
                           request_timeout=15
                           )

async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot): # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_4(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)
