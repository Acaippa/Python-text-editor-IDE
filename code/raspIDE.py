from tkinter import*
import os
from data.Texto import CustomText
from data.run_handler import*
from data.file_handler import*
from data.menu_handler import*
import pyautogui

class App(Tk): # creates the class for the whole project
	def __init__(self):
		super().__init__() # initiating the tkinter super "parent"
		self.conf = eval(open("data/config.rpi", "r").read()) # open the config file
		self.schemelogic()
		self.fontsize = 12

		self.path = None
		self.content_hash = None

		self.menu = MenuHandler(self) # This line also "draws" the menu

		self.text_frame = LabelFrame(self, bd=0)

		self.mainTxt = CustomText(self.text_frame, bg=self.scheme["mainColor"], bd=0, fg=self.scheme["fontColor"], insertbackground=self.scheme["selectorColor"], font=("bruh", self.fontsize), tabs="1c") # making the main text widget

		self.numberLine = CustomText(self.text_frame, width=7, bg=self.scheme["numberLineColor"], bd=0, font=("bruh", self.fontsize), fg=self.scheme["numberlineFontColor"])
		self.numberLine.tag_configure("centerText", justify="center")
		self.numberLine.tag_add("centerText", "1.0", "end")
		self.scroll = Scrollbar(self)

		self.draw()

		self.scroll["command"] = self.onScrollbar
		self.mainTxt["yscrollcommand"] = self.ontextScroll
		self.numberLine["yscrollcommand"] = self.ontextScroll


		self.mainTxt.bind("<<TextModified>>", self.lineLogic)
		self.bind('<Return>', self.returnLogic)


	def draw(self):
		# Draw all the text elements.
		self.scroll.pack(side=RIGHT, fill=Y)
		self.numberLine.pack(side=LEFT, fill=Y)
		self.mainTxt.pack(side=LEFT, fill=BOTH, expand=True)

		self.text_frame.pack(fill=BOTH, expand=True)

	# ! Some of these line code should be moved.
	def lineLogic(self, event):
		self.mainTxt.configure(state="disabled")
		self.numberLine.delete("1.0", "end")

		self.numberLine.insert(INSERT, "\n".join([str(i+1) for i in range(int(self.mainTxt.index('end').split(".")[0])-1)])) #adding all the lines to the numberline

		self.numberLine.tag_add("centerText", "1.0", "end")
		self.mainTxt.configure(state="normal")

		self.update_hash()


	def returnLogic(self, event):
		char = self.mainTxt.get(self.mainTxt.index("insert-2c")) #gets the character that is before the cursor

		if char == ":":
			pyautogui.press("tab") # inserting a tab

	def onScrollbar(self, *args): # moves the text widgets when the scrollbar moves
		self.mainTxt.yview(*args)
		self.numberLine.yview(*args)

	def ontextScroll(self, *args): # moves the scrollbar when the text widgets are scrolled
		self.scroll.set(*args)
		self.onScrollbar("moveto", args[0])
	
	def schemelogic(self):
		amountOfSchemes = len(os.listdir(f"{os.getcwd()}\\data\\schemes")) # get the amount of schemes in the schemes directory
		if amountOfSchemes == 1: # if there is only one scheme, use the default one.
			self.confColor = os.listdir(f"{os.getcwd()}\\data\\schemes")

		elif amountOfSchemes > 1:
			found = False
			for i in range(amountOfSchemes): # if not, we look for the scheme name in the config file and see if it matches the name in the schemes directory
				name = os.listdir(f"{os.getcwd()}/data/schemes")[i]
				if name == self.conf["schemeName"]:
					path = f"{os.getcwd()}\\data\\schemes\\{name}"
					found = True
					self.scheme = eval(open(path, "r").read())
		if found == False:
			print("scheme not found")

	def get_data(self):
		return self.mainTxt.get("1.0", END)

	def load_data(self, data): # ! Applications laggs heavilly when large files are loaded. This is mostly due to the wrapper having to calculate the line breaks and so on.
		# TODO: Figure out a way to make the application handle large files.
		self.mainTxt.insert(END, data)

	def update_hash(self):
		self.content_hash = hash(self.get_data())

if __name__ == __name__:
	main = App()
	main.mainloop()
	print(main.scheme)