from tkinter import *

from UI.Panel.Components.Component import Component
from UI.Panel.Elements.Element import Element
from UI.Panel.utils import focus_next_widget, focus_previous_widget

class TextElt(Element):
	def __init__(self, defaultText, parent: Component, parentFrame, format = "any", width=4, height=1, id=None, classes=[], bg=None, side=LEFT):
		super().__init__(parent, parentFrame, "min", "min", id, classes, bg, side)
		self.defaultText = defaultText
		self.format = format
		self.text = Text(self.frame, bg=self.bg, width=0 if (type(width) == str) else width, height=0 if (type(width) == str) else height, maxundo=3)
		self.text.bind("<Tab>", focus_next_widget)
		self.text.bind("<Shift-Tab>", focus_previous_widget)
		if format == "int":
			self.text.bind("<Key>", self.validate_input_int)
			# self.text.bind('<Up>', lambda _: self.add1)
			# self.text.bind('<Down>', lambda _: self.remove1)
			self.text.bind('<Return>', lambda _: "break")
		elif format == "number":
			self.text.bind("<Key>", self.validate_input_number)
			# self.text.bind('<Up>', lambda _: self.add1)
			# self.text.bind('<Down>', lambda _: self.remove1)
			self.text.bind('<Return>', lambda _: "break")
		self.text.insert(INSERT, self.defaultText)
		self.text.pack()

	# get the text from the text element
	def get(self):
		returnText = self.text.get("1.0", "end-1c")
		if self.format == "int":
			try :
				int(returnText)
			except ValueError:
				self.text.delete("1.0", END)
				self.text.insert(INSERT, "0")
				return 0
			return int(returnText)
		elif self.format == "number":
			try :
				float(returnText)
			except ValueError:
				self.text.delete("1.0", END)
				self.text.insert(INSERT, "0.0")
				return 0.0
			return float(returnText)
		return self.text.get("1.0", END)
	
	def test_modifier_keys(self, event):
		# mods = {
		# 	0x0001: 'Shift',
		# 	0x0002: 'Caps Lock',
		# 	0x0004: 'Control',
		# 	0x0008: 'Left-hand Alt',
		# 	0x0010: 'Num Lock',
		# 	0x0080: 'Right-hand Alt',
		# 	0x0100: 'Mouse button 1',
		# 	0x0200: 'Mouse button 2',
		# 	0x0400: 'Mouse button 3'
		# }

		# test if ctrl, alt, or shift is pressed
		s = event.state
		ctrl  = (s & 0x4) != 0
		alt   = (s & 0x8) != 0 or (s & 0x80) != 0
		shift = (s & 0x1) != 0
		return (ctrl or alt or shift)

	def validate_input_int(self, event):
		# if ctrl, alt, or shift is pressed : validate the input
		if self.test_modifier_keys(event):
			return
		
		# Get the current content of the Text widget
		current_text = self.text.get("1.0", "end-1c")

		# check if the current text is an int :
		try :
			int(current_text)
		except ValueError:
			# if the current text is not an int, reset the text to "0"
			self.text.delete("1.0", END)
			self.text.insert(INSERT, "0")
			return 'break'

		# Check if each character is a digit or backspace
		for char in event.char:
			if not char.isdigit() and char != '\b':
				# If the character is not a digit or backspace, prevent it from being added to the Text widget
				self.text.bell()  # Beep to indicate invalid input
				return 'break'      # Return 'break' to prevent the character from being inserted

	def validate_input_number(self, event):
		# if ctrl, alt, or shift is pressed : validate the input
		if self.test_modifier_keys(event):
			return

		# Get the current content of the Text widget
		current_text = self.text.get("1.0", "end-1c")

		# check if the current text is a float :
		try :
			float(current_text)
		except ValueError:
			# if the current text is not a float, reset the text to "0.0"
			self.text.delete("1.0", END)
			self.text.insert(INSERT, "0.0")
			return 'break'

		# Check if each character is a digit, a period, or backspace
		for char in event.char:
			if not char.isdigit() and char != '.' and char != '\b':
				# If the character is not a digit, period, or backspace, prevent it from being added to the Text widget
				self.text.bell()
				return 'break'

	# def add1(self, event):
	# 	current_text = self.text.get("1.0", "end-1c")
	# 	try :
	# 		i = int(current_text)
	# 		if event.state & 0x1:
	# 			i += 10
	# 		else:
	# 			i += 1
	# 		self.text.delete("1.0", END)
	# 		self.text.insert(INSERT, str(i))
	# 	except ValueError:
	# 		self.text.delete("1.0", END)
	# 		self.text.insert(INSERT, "0")
	# 		return
	
	# def remove1(self, event):
	# 	current_text = self.text.get("1.0", "end-1c")
	# 	try :
	# 		i = int(current_text)
	# 		if event.state & 0x1:
	# 			i -= 10
	# 		else:
	# 			i -= 1
	# 		self.text.delete("1.0", END)
	# 		self.text.insert(INSERT, str(i))
	# 	except ValueError:
	# 		self.text.delete("1.0", END)
	# 		self.text.insert(INSERT, "0")
	# 		return