from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
# 1-usul
# button = ReplyKeyboardMarkup(resize_keyboard=True,input_field_placeholder="Kerakli tugmalarni tanlang!",one_time_keyboard=True,
#     keyboard=[
#         [KeyboardButton(text="tugma1"),
#          KeyboardButton(text="tugma2")],
#         [KeyboardButton(text="tugma3")]
#     ]
# )
from aiogram.utils.keyboard import ReplyKeyboardBuilder,KeyboardButton
# 2-usul
button = ReplyKeyboardBuilder()
button.add(KeyboardButton(text="Tugma1"))
button.add(KeyboardButton(text="Tugma2"))
button.add(KeyboardButton(text="Tugma3"))
button.add(KeyboardButton(text="Tugma4"))
button.add(KeyboardButton(text="📩 Biz bilan bog'lanish"))
button.add(KeyboardButton(text="📊 Statistika"))
button.adjust(1,2)
