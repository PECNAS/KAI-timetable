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

def getGroupsMarkup(groups):
	builder = InlineKeyboardBuilder()

	for group in groups:
		builder.button(
			text=group,
			callback_data=f"group_{group}")

	builder.adjust(2)
	return builder.as_markup()

def getDaysMarkup():
	builder = InlineKeyboardBuilder()

	for day in BUTTONS["days"]:
		builder.button(
			text=day,
			callback_data=f"day_{day}")

	builder.adjust(2)
	return builder.as_markup()

def getWeeksMarkup():
	builder = InlineKeyboardBuilder()

	for data, text in BUTTONS["weeks"].items():
		builder.button(
			text=text,
			callback_data=data)

	builder.adjust(2)
	return builder.as_markup()

if __name__ == "__main__":
	from imports import *
	timetable = get_students_timetable()
	print(getGroupsMarkup(list(timetable.keys())))