from tkinter import*
from data.file_handler import*
from data.run_handler import*
from data.alert_handler import*

class MenuHandler:
	def __init__(self, master):
		self.master = master
		self.menu = Menu()
		self.master.config(menu=self.menu)

		self.file_handler = FileHandler(self.master)
		self.alert_handler = AlertHandler()

		self.file_menu = Menu(self.menu, tearoff="off")
		self.file_menu.add_command(label="Save", command=self.file_handler.save)
		self.file_menu.add_command(label="Save As...", command=self.file_handler.save_as)
		self.file_menu.add_command(label="Open File", command=self.file_handler.open_file)
		self.file_menu.add_separator()
		self.file_menu.add_command(label="Exit", command=self.exit)
		self.menu.add_cascade(label="File", menu=self.file_menu)

		self.run_handler = RunHandler(self.master)

		self.run_menu = Menu(self.menu, tearoff="off")
		self.run_menu.add_command(label="Run", command=self.run)
		self.menu.add_cascade(label="Run", menu=self.run_menu)

	def exit(self): 
		confirm = self.alert_handler.ask_yes_no("Quit?", "Are you sure you want to quit?")
		if confirm:
			if not self.file_handler.check_if_saved():
				self.file_handler.file_not_saved_confirm_quit()
			else:
				exit()
		else:
			pass

	def run(self):
		# run the file stored in the current path.
		if self.master.path != None:
			self.run_handler.run()
		else:
			self.file_handler.save()
