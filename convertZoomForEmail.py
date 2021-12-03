import dearpygui.dearpygui as dpg

def callbackFile1(sender, app_data):
	print("Sender: ", sender)
	print("App Data: ", app_data)
	selections = app_data["selections"]
	for selection in selections:
		print(selection)
		print(selections[selection])
		directory = selection
		file_directory = selections[selection]
		dpg.set_value("filedir1", directory)
		dpg.set_value("file1", file_directory)

def callbackFile2(sender, app_data):
	selections = app_data["selections"]
	for selection in selections:
		directory = selection
		file_directory = selections[selection]
		dpg.set_value("filedir2", directory)
		dpg.set_value("file2", file_directory)

def callbackFile3(sender, app_data):
	selections = app_data["selections"]
	for selection in selections:
		directory = selection
		file_directory = selections[selection]
		dpg.set_value("filedir3", directory)
		dpg.set_value("file3", file_directory)

with dpg.file_dialog(directory_selector=False, show=False, callback=callbackFile1, id="file_dialog_id1"):
    dpg.add_file_extension(".csv", color=(255, 255, 0, 255))
    dpg.add_file_extension(".*", color=(255, 255, 255, 255))

with dpg.file_dialog(directory_selector=False, show=False, callback=callbackFile2, id="file_dialog_id2"):
    dpg.add_file_extension(".csv", color=(255, 255, 0, 255))
    dpg.add_file_extension(".*", color=(255, 255, 255, 255))

with dpg.file_dialog(directory_selector=False, show=False, callback=callbackFile3, id="file_dialog_id3"):
    dpg.add_file_extension(".csv", color=(255, 255, 0, 255))
    dpg.add_file_extension(".*", color=(255, 255, 255, 255))

with dpg.window(id= "Primary Window", label="Tutorial", width=600, height=200):
	dpg.add_button(label="File Selector", callback=lambda: dpg.show_item("file_dialog_id1"))
	dpg.add_text("Directory Path: ")
	dpg.add_same_line()
	dpg.add_text(label="##filedir", default_value="None Selected", id="filedir1")
	dpg.add_text("File Path: ")
	dpg.add_same_line()
	dpg.add_text(label="##file", default_value="None Selected", id="file1")
	dpg.add_button(label="File Selector", callback=lambda: dpg.show_item("file_dialog_id2"))
	dpg.add_text("Directory Path: ")
	dpg.add_same_line()
	dpg.add_text(label="##filedir", default_value="None Selected", id="filedir2")
	dpg.add_text("File Path: ")
	dpg.add_same_line()
	dpg.add_text(label="##file", default_value="None Selected", id="file2")
	dpg.add_button(label="File Selector", callback=lambda: dpg.show_item("file_dialog_id3"))
	dpg.add_text("Directory Path: ")
	dpg.add_same_line()
	dpg.add_text(label="##filedir", default_value="None Selected", id="filedir3")
	dpg.add_text("File Path: ")
	dpg.add_same_line()
	dpg.add_text(label="##file", default_value="None Selected", id="file3")

dpg.set_primary_window("Primary Window", True)

dpg.start_dearpygui()
