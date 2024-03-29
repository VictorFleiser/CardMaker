from tkinter import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	# avoid circular import at runtime
	from UI.App import App
	from UI.Panel.Elements.Element import Element

class Component:
	"""
	Abstract Component class
	"""
	def __init__(self, parent : 'App|Component', parentFrame : Frame, width = "fill", height = "fill", id = None, classes = [], bg = None, side=TOP):
		self.parent = parent
		self.parentFrame = parentFrame
		self.width = width
		self.height = height
		self.side = side
		self.bg = bg
		self.id = id
		self.classes = classes
		
		self.frame = Frame(parentFrame, width=None if (type(self.width) == str) else self.width, height=None if (type(self.height) == str) else self.height, bg=self.bg, relief='raised', borderwidth=1)
		if self.height != "min" and self.width != "min":
			self.frame.pack_propagate(False)  # Prevent the frame from resizing to its children (I think)

		if width == "fill" and height == "fill":
			self.frame.pack(fill='both', expand=True, side=self.side)
		elif width == "fill":
			self.frame.pack(fill='x', expand=False, side=self.side)
		elif height == "fill":
			self.frame.pack(fill='y', expand=False, side=self.side)
		else:
			self.frame.pack(side=self.side)

		# self.parent.add(self)
		self.contents : list['Component|Element'] = []

	def getParentFrame(self):
		return self.frame

	def add(self, component : 'Component|Element'):
		self.contents.append(component)
