from imports import *

@main_router.message(StateFilter(None), F.text == BUTTONS["start"]["students"])
async def students_timteable_handler(message, state):
	timetable = get_students_timetable()
	await state.update_data(timetable=timetable)
	await state.set_state(StudentsGroup.GroupState)

	await message.answer(
		MSGS["student_group"],
		reply_markup=getGroupsMarkup(list(timetable.keys())))

@main_router.callback_query(StateFilter(StudentsGroup.GroupState))
async def GroupState_handler(call, state):
	await call.answer()
	group = call.data.replace("group_", "")

	await state.update_data(group=group)
	await state.set_state(StudentsGroup.DayState)

	await call.message.answer(
		MSGS["student_day"],
		reply_markup=getDaysMarkup())

@main_router.callback_query(StateFilter(StudentsGroup.DayState))
async def DayState_handler(call, state):
	await call.answer()
	day = call.data.replace("day_", "")

	await state.update_data(day=day)
	await state.set_state(StudentsGroup.WeekState)

	await call.message.answer(
		MSGS["student_week"],
		reply_markup=getWeeksMarkup())

@main_router.callback_query(StateFilter(StudentsGroup.WeekState))
async def WeekState_handler(call, state):
	await call.answer()
	data = (await state.get_data())

	week = call.data
	if week == "even": text_week = "Чётная"
	else: text_week = "Нечётная"

	print(week)
	group = data.get("group")
	day = data.get("day")
	timetable = data.get("timetable")[group][week][day]
	text = ""

	for el in timetable:
		text += f"<b>{el["time"]}</b> <em>{el["subject"]}</em> ({el["house"]} зд., {el["room"]})\n\n"

	await call.message.answer(
		MSGS["student_timetable"].format(
			day,
			text_week,
			group,
			text), reply_markup=getStartMarkup())
	await state.clear()