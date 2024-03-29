from tkinter import *

class MenuBar:
	"""
	Class to hold the menu bar
	"""
	def __init__(self, root):
		# Create the menu bar
		self.menu_bar = Menu(root)

			# Create the file menu
		self.file_menu = Menu(self.menu_bar, tearoff=0)
		self.menu_bar.add_cascade(label="File ", menu=self.file_menu)
				# Add the menu items
		self.file_menu.add_command(label="Open")
		self.file_menu.add_command(label="Save")
		self.file_menu.add_separator()
		self.file_menu.add_command(label="Exit", command=root.quit)
		
			# Create the edit menu
		self.edit_menu = Menu(self.menu_bar, tearoff=0)
		self.menu_bar.add_cascade(label="Edit ", menu=self.edit_menu)
				# Add the menu items
		self.edit_menu.add_command(label="Cut")
		self.edit_menu.add_command(label="Copy")
		self.edit_menu.add_command(label="Paste")

			# Create the help menu
		self.help_menu = Menu(self.menu_bar, tearoff=0)
		self.menu_bar.add_cascade(label="Help ", menu=self.help_menu)
				# Add the menu items
		self.help_menu.add_command(label="About ")

		root.config(menu=self.menu_bar)