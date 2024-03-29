from tkinter import *

from UI.Panel.Components.Component import Component
from UI.Panel.Elements.LabelElt import LabelElt
from UI.Panel.Elements.TextElt import TextElt

class EditDimensionsComponent(Component):
	def __init__(self, parent, parentFrame, width="min", height="min", id=None, classes=[], bg=None, side=LEFT):
		super().__init__(parent, parentFrame, width, height, id, classes, bg, side)
		# self.title = LabelElt("Edit Dimensions", self, width="min", height="min", bg=self.bg, side=TOP)
		# self.title.label.config(font=("Arial", 16))
		# self.title.label.pack()
		self.posXLabel = LabelElt("x:", self, self.frame, width="min", height="min", bg=self.bg, side=LEFT)
		self.posX = TextElt("0", self, self.frame, format="int", height=1, width=4, bg=self.bg, side=LEFT)
		self.posYLabel = LabelElt("y:", self, self.frame, width="min", height="min", bg=self.bg, side=LEFT)
		self.posY = TextElt("0", self, self.frame, format="int", height=1, width=4, bg=self.bg, side=LEFT)
		self.widthLabel = LabelElt("w:", self, self.frame, width="min", height="min", bg=self.bg, side=LEFT)
		self.width = TextElt("1", self, self.frame, format="number", height=1, width=4, bg=self.bg, side=LEFT)
		self.heightLabel = LabelElt("h:", self, self.frame, width="min", height="min", bg=self.bg, side=LEFT)
		self.height = TextElt("1", self, self.frame, format="number", height=1, width=4, bg=self.bg, side=LEFT)

		# self.add(self.title)
		self.add(self.posXLabel)
		self.add(self.posX)
		self.add(self.posYLabel)
		self.add(self.posY)
		self.add(self.heightLabel)
		self.add(self.height)
		self.add(self.widthLabel)
		self.add(self.width)

	def get(self):
		return {"pos" : (self.posX.get(), self.posY.get()), "dim" : (self.width.get(), self.height.get())}