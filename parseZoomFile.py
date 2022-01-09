common_names = { "555-555-5555": "John Doe" }

names = []

default_no_file_selected = "None Selected"

def CombineThreeFile(firstFile, secondFile, thirdFile):
	if not isinstance(firstFile, str) and not isinstance(secondFile, str) and not isinstance(thirdFile):
		return
	if firstFile == default_no_file_selected or secondFile == default_no_file_selected or thirdFile == default_no_file_selected:
		return
	with open(firstFile, 'r', encoding='utf-8') as file:
		for line in file:
			if line == '\n':
				continue
	#		print(line)
			tokens = line.split(",")
			name = tokens[0]
	#		print(name)
			names.append(name)
		file.close()
		
	names.pop(0)

	print('First Meeting Attendance:')
	for n in names:
		if n in common_names:
			print(common_names[n])
		else:
			print(n)

	relief_society_names = []
	with open(secondFile, 'r', encoding='utf-8') as file:
		for line in file:
			if line == '\n':
				continue
	#		print(line)
			tokens = line.split(",")
			name = tokens[0]
			relief_society_names.append(name)
		file.close()

	relief_society_names.pop(0)
	print('Second Meeting Attendance:')
	for n in relief_society_names:
		if n in common_names:
			if n != "Church":
				print(common_names[n])
		else:
			print(n)

	elder_quorum_names = []
	with open(thirdFile, 'r', encoding='utf-8') as file:
		for line in file:
			if line == '\n':
				continue
	#		print(line)
			tokens = line.split(",")
			name = tokens[0]
			elder_quorum_names.append(name)
		file.close()

	elder_quorum_names.pop(0)
	print('Third Meeting Attendance:')
	for n in elder_quorum_names:
		if n in common_names and n != "Zoom Leader":
			print(common_names[n])
		else:
			print(n)

	with open('test.txt', 'w') as file:
		file.write("First Meeting Attendance:\n")
		for n in names:
			if n in common_names:
				file.write(common_names[n])
			else:
				file.write(n)
			file.write('\n')

		file.write("\nSecond Meeting Attendance:\n")
		for n in relief_society_names:
			if n in common_names and n != "Zoom Leader":
				file.write(common_names[n])
			else:
				file.write(n)
			file.write('\n')
		
		file.write("\nThird Meeting Attendance:\n")
		for n in elder_quorum_names:
			if n in common_names and n != "Zoom Leader":
				file.write(common_names[n])
			else:
				file.write(n)
			file.write('\n')
		
		file.close()