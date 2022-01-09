import dearpygui.dearpygui as dpg
from parseZoomFile import *

# Ideas: 
# - The UI is ugly at the moment. I could research the api to fix those up.
# - Figure out to disable the submit button until three files are selected.
# - When the window is showing, it is off-centered. I am guessing it is not dpi-aware.
# - Inform the user if the file was successfully created.
# - The generated report file name should be unique. Possibly use date time to create the file name.

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

def process_three_files():
	firstFile = dpg.get_value("file1")
	secondFile = dpg.get_value("file2")
	thirdFile = dpg.get_value("file3")
	print(str(firstFile))
	print(str(secondFile))
	print(str(thirdFile))
	CombineThreeFile(firstFile, secondFile, thirdFile)

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
	dpg.add_text("Combine Three Files into one file")
	dpg.add_button(label="Generate One File", callback=process_three_files)

dpg.set_primary_window("Primary Window", True)

dpg.start_dearpygui()
