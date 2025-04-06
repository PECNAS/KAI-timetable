from imports import *

@main_router.message(F.text == BUTTONS["start"]["teachers"])
async def teachers_timetable_handler(message, state):
	# await state.set_state(TeachersGroup.TeacherName)
	pass