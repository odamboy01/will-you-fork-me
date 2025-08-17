from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# --- Main Reply Keyboard with 5 buttons ---
main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌟 Motivatsiya")],
        [KeyboardButton(text="😔 Depressiya")],
        [KeyboardButton(text="🤓 Qiziqarli faktlar")],
        [KeyboardButton(text="💪 Sog'lomlik maslahatlari")],
        [KeyboardButton(text="🎲 Xar xil maslahatlar")],
        [KeyboardButton(text="Bot egasi")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Kerakli tugmani bosing..."
)


# --- Inline Example (your cars) ---
cars = ['Nexia 2', 'Gentra', 'Damas', 'Cobalt', 'Malibu', 'Tahoe']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(
            InlineKeyboardButton(
                text=car,
                url='https://www.uzautomotors.com/'
            )
        )
    return keyboard.adjust(3).as_markup()
