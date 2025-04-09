import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from token_config import *
from aiogram.fsm.storage.memory import MemoryStorage

dp = Dispatcher(storage=MemoryStorage())
try:
	bot = Bot(
			token=TOKEN,
			default=DefaultBotProperties(
				parse_mode=ParseMode.HTML
				)
			)
except Exception as e:
	print("Токен для телеграм бота не найден! Проверьте наличие файла token_config.py и присутствия в нем переменной TOKEN")
	sys.exit(0)

def startup():
	print("Bot started")

def shutdown():
	print("Goodbye, friend!")

async def main() -> None:
	startup()
	await dp.start_polling(bot)

if __name__ == "__main__":
	from imports import *

	from handlers.commands_handler import *
	from handlers.students_handler import *
	from handlers.teachers_handler import *

	logging.basicConfig(
		level=logging.INFO,
		stream=sys.stdout
		)

	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		shutdown()