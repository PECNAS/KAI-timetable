from aiogram.fsm.state import StatesGroup, State

class TeachersGroup(StatesGroup):
	TeacherName = State()

class StudentsGroup(StatesGroup):
	GroupState = State()
	DayState = State()
	WeekState = State()