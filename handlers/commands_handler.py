from imports import *

@main_router.message(Command(commands=["start"]))
async def start_handler(message, state):
	await state.clear()
	await message.answer(
		MSGS["start"],
		reply_markup=getStartMarkup())