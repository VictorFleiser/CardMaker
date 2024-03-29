from tkinter import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	# avoid circular import at runtime
	from UI.App import App

class Viewer:
	"""
	Class to hold the card viewer
	"""
	def __init__(self, parent : 'App', title, width):
		# Set the title and parent
		self.title = title
		self.parent : App = parent

		# Create the frame to hold the viewer
		self.frame = Frame(self.parent.paned_window, bg='red', width=width)

		# Create a label to display the title
		self.label = Label(self.frame, text=self.title)
		self.label.pack()

		# Add the frame to the paned window
		self.parent.paned_window.add(self.frame, stretch='always')
		
		