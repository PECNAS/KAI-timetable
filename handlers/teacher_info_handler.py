from imports import *

@main_router.message(F.text == BUTTONS["start"]["teacher_info"])
async def teacher_info_handler(message, state):
	await message.answer(
		MSGS["teacher_info__start"],
		reply_markup=getTeacherInfoMarkup())

	await state.set_state(TeacherInfoGroup.TeacherNameState)

@main_router.callback_query(StateFilter(TeacherInfoGroup.TeacherNameState))
async def teacher_fio_handler(call, state):
	await call.answer()
	teacher_id = int(call.data.replace("teacher_info__", ""))
	teacher = TEACHERS[teacher_id]

	text = f'<b>{teacher["name"]}</b>\n\n{teacher["desc"]}\n\nШанс списать: <em>{teacher["chance"]}</em>'

	await call.message.answer(text, reply_markup=getStartMarkup())
	await state.clear()