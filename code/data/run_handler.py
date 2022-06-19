import os
from threading import Thread


class RunHandler: # Handles all the run functions.
	def __init__(self, master):
		self.master = master

	def run(self):
		# TODO: Add a console command in the config file that will determine a command that will be run when a program needs to be run.
		self.start_thread(self.run_thread)

	def run_thread(self): # ! Figure out a way to make an internal console that can take inputs and display outputs instead of opening a new window.
		os.system(f"python {self.master.path}")

	def start_thread(self, function):
		thread = Thread(target=function)
		thread.setDaemon(True)
		thread.start()
