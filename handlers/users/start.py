from aiogram.filters import CommandStart,Command
from loader import dp, bot
from aiogram import types,F
#from keyboards.defaults.buttons import button
from keyboards.inline.inline_button import btn
from aiogram.enums.parse_mode import ParseMode

@dp.message(CommandStart())
async def start_bot(message:types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name} botimizga xush kelibsiz! 🙋")

@dp.message(Command('inline_button'))
async def tugmalar(message:types.Message):
    await message.answer("🔝 Asosiy Menyu", reply_markup=btn.as_markup(resize_keyboard=True))

@dp.message(F.text=="📩 Biz bilan bog'lanish")
async def contact_us(message:types.Message):
    await message.answer("🙎🏻‍♂️ <b>Loyiha asoschisi:</b>\n @softwaredevuz", parse_mode=ParseMode.HTML)