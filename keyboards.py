from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from config import BUTTONS

def getStartMarkup():
	builder = ReplyKeyboardBuilder()
	for btn in BUTTONS["start"].values():
		builder.button(text=btn)

	builder.adjust(2)
	markup = builder.as_markup()
	markup.resize_keyboard = True

	return markup

if __name__ == "__main__":
	getCategoriesMarkup()