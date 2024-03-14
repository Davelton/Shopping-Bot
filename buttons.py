from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn = [
    [KeyboardButton(text="Категория⌨️"), KeyboardButton(text="Профиль🧰")],
    [KeyboardButton(text="Поддержка📞"), KeyboardButton(text="Депозит💶")]

]
menu = ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)

btnCat = [
    [KeyboardButton(text="Черная Икра🫙"), KeyboardButton(text="Соленные огурцы🥒")],
    [KeyboardButton(text="Колбаса Докторская🫘"), KeyboardButton(text="Чипсы Доритос🥠")],
    [KeyboardButton(text="🔙Back")]

]

catMenu1 = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)

inlineBtn1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить",callback_data="pay_1")]
])


catMenu2 = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)

inlineBtn2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить",callback_data="pay_2")]
])


catMenu3 = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)

inlineBtn3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить",callback_data="pay_3")]
])

catMenu4 = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)

inlineBtn4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить",callback_data="pay_4")]
])
