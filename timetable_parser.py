import openpyxl

# timetable = {
# 	"4134": {
# 		"even": {
# 			"пн": [
# 				{"time": "8.00", "subject": "Обществознание", "type": "пр", "house": "7", "teacher": "Швецова"},
# 				{"time": "9.40", "subject": "Русский язык", "type": "лк", "house": "7", "teacher": "Ибрагимова"},
# 				{"time": "11.20", "subject": "Математика", "type": "пр", "house": "7", "teacher": "Смирнов"}
# 			],
# 			"вт": [
# 				{"time": "8.00", "subject": "Обществознание", "type": "пр", "house": "7", "teacher": "Швецова"},
# 				{"time": "9.40", "subject": "Русский язык", "type": "лк", "house": "7", "teacher": "Ибрагимова"},
# 				{"time": "11.20", "subject": "Математика", "type": "пр", "house": "7", "teacher": "Смирнов"}
# 			],
# 			"ср": [
# 				{"time": "8.00", "subject": "Обществознание", "type": "пр", "house": "7", "teacher": "Швецова"},
# 				{"time": "9.40", "subject": "Русский язык", "type": "лк", "house": "7", "teacher": "Ибрагимова"},
# 				{"time": "11.20", "subject": "Математика", "type": "пр", "house": "7", "teacher": "Смирнов"}
# 			]
# 		}
# 	}
# }

def get_timetable_from_xlsx():
	timetable = {}
	wb = openpyxl.load_workbook("rasp.xlsx")
	sheet = wb.active

	counter = 0
	for row in sheet:
		if row[0].row == 1:
			continue

		group = str(row[0].value)
		day = row[1].value
		time = row[2].value
		date = row[3].value
		subject = row[4].value
		type = row[5].value
		room = row[6].value
		house = row[7].value
		teacher = row[9].value

		data = {
				"time": time.strftime("%H:%M"),
				"subject": subject,
				"type": type,
				"house": house,
				"room": room,
				"teacher": teacher.capitalize(),
			}

		if timetable.get(group) == None:
			timetable[group] = {
				"even": {"пн": [], "вт": [], "ср": [], "чт": [], "пт": [], "сб": []},
				"odd": {"пн": [], "вт": [], "ср": [], "чт": [], "пт": [], "сб": []}
				}

		if date == None:
			timetable[group]["even"][day].append(data)
			timetable[group]["odd"][day].append(data)

		else:
			if date.find("чет") != -1:
				timetable[group]["even"][day].append(data)
			if date.find("неч") != -1:
				timetable[group]["odd"][day].append(data)

	return timetable

if __name__ == "__main__":
	print(get_timetable_from_xlsx())