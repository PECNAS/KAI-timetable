from imports import *

@main_router.message(F.text == BUTTONS["start"]["teachers"])
async def teachers_timetable_handler(message, state):
	await state.set_state(TeachersGroup.TeacherName)
	timetable = get_teachers_timetable()
	await state.update_data(timetable=timetable)

	await message.answer(
		MSGS["teacher_name"],
		reply_markup=getTeachersMarkup(list(timetable.keys())))

@main_router.callback_query(StateFilter(TeachersGroup.TeacherName))
async def TeacherName_handler(call, state):
	await call.answer()
	await state.update_data(teacher=call.data.replace("teacher_", ""))

	await call.message.answer(
		MSGS["teacher_day"],
		reply_markup=getDaysMarkup())

	await state.set_state(TeachersGroup.DayState)

@main_router.callback_query(StateFilter(TeachersGroup.DayState))
async def DayState_handler(call, state):
	await call.answer()
	await state.update_data(day=call.data.replace("day_", ""))

	await call.message.answer(
		MSGS["teacher_week"],
		reply_markup=getWeeksMarkup())

	await state.set_state(TeachersGroup.WeekState)

@main_router.callback_query(StateFilter(TeachersGroup.WeekState))
async def WeekState_handler(call, state):
	await call.answer()
	data = (await state.get_data())

	week = call.data
	if week == "even": text_week = "Чётная"
	else: text_week = "Нечётная"

	day = data.get("day")
	teacher = data.get("teacher")
	timetable = data.get("timetable")[teacher][week][day]

	text = ""

	for el in timetable:
		text += f"<b>{el["time"]}</b> <em>{el["subject"]}</em> ({el["house"]} зд., {el["room"]}) {el["group"]}\n\n"

	await call.message.answer(
		MSGS["teacher_timetable"].format(
			day,
			text_week,
			teacher,
			text), reply_markup=getStartMarkup())
	await state.clear()

