import tkinter.filedialog as fd
from data.alert_handler import*


class FileHandler: # Handles actions related to files.
	def __init__(self, master):
		self.master = master
		self.default_extensions = [("All Files", "*.*"), ("Python Files", "*.py"), ("Text Document", "*.txt")]
		self.alert_handler = AlertHandler()

	def save(self):
		# Run the save_as command if a path is not already specified.
		if self.master.path == None:
			self.save_as()
		else:
			data = self.master.get_data()
			with open(self.master.path, "w") as file:
				file.write(data)
				file.close()

	def save_as(self): # ! BUG: The save as promt has problems saving in certain directories.
		path = fd.asksaveasfile(mode='w', filetypes = self.default_extensions)

		if path != None: # Check if the user didn't click cancel on the save-as prompt.
			self.master.path = path.name
			path = path.name
			with open(path, "w") as file:
				file.write(self.master.get_data())
				file.close()


	def check_if_saved(self): # Compare the hash of the contens in the text widget to the contents of the file located at master.path.
		if self.master.path != None:
			file_to_check = open(self.master.path, "r").read()
			file_to_check_hash = hash(file_to_check)

			if self.master.content_hash == file_to_check_hash:
				return True
		return False

	def file_not_saved_confirm_quit(self): 
		bool = self.alert_handler.ask_yes_no("Quit?", "Your file is not saved, are you sure you want to quit?")
		if bool:
			exit()
		else:
			pass

	def open_file(self):
		path = fd.askopenfile(mode='r', filetypes = self.default_extensions)
		if path != None:
			path = path.name

			self.master.path = path
			with open(path, 'rb') as file:
				data = file.read()
				file.close()
			self.master.load_data(data)