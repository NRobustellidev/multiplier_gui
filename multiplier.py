"""
Program: multiplier.py
Author: Nicholas
Date: 4/26/2021

*** Note: the file breezypythongui.py MUST be in the same directory as this file for the application to work. ***
"""

from breezypythongui import EasyFrame

class Multiplier(EasyFrame):
	
	def __init__(self):
		"""Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Multiplier App", resizable = False, background = "khaki", width = 320, height = 260)
		self.addLabel(text = "Multiplier", row = 0, column = 0, columnspan = 2, background = "khaki", sticky = "NSEW").config(font = ("Courier", 20))
		self.addLabel(text = "Enter your base number", row = 1, column = 0, background = "khaki")
		self.base = self.addIntegerField(value = 0, row = 1, column = 1)
		self.addLabel(text = "Enter the factor number", row = 2, column = 0, background = "khaki")
		self.factor = self.addIntegerField(value = 0, row = 2, column = 1)
		self.factor.bind("<Return>", lambda event: self.multiply())
		self.addButton(text = "Calculate", row = 3, column = 0, columnspan = 2, command = self.multiply)

		
	def multiply(self):
		"""Multiplies the base number times the factor number and outputs the result"""
		self.addLabel(text = "The result is: ", row = 4, column = 0, background = "khaki").config(font = ("Courier", 14), foreground = "red")
		self.resultField = self.addIntegerField(value = 0, row = 4, column = 1, state = "readonly")

		# input phase
		baseNum = self.base.getNumber()
		factorNum = self.factor.getNumber()

		# calculation phase
		result = baseNum * factorNum

		# output phase
		self.resultField.setNumber(result)


# definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	Multiplier().mainloop()

# global call to the main() function
main()