import tkinter.messagebox as ms

class AlertHandler:
	def __init__(self):
		pass

	def ask_yes_no(self, title, message):
		return ms.askyesno(title=title, message=message)

	def ask_yes_no_cancel(self, title, message):
		return ms.askyesnocancel(title=title, message=message)

