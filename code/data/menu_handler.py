from tkinter import*

class MenuHandler:
	def __init__(self, master):
		self.master = master
		self.menu = Menu()
		self.master.config(menu=self.menu)

		self.file_menu = Menu(self.menu, tearoff="off")
		self.file_menu.add_command(label="Save")
		self.file_menu.add_command(label="Save As...")
		self.file_menu.add_command(label="Open File")
		self.file_menu.add_separator()
		self.file_menu.add_command(label="Exit", command=self.exit)
		self.menu.add_cascade(label="File", menu=self.file_menu)


	def exit(self):
		# TODO: Add an alert that asks if the user is sure they want to close the program aswell as check if the document.
		exit()
