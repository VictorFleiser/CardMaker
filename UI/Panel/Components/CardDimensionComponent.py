from tkinter import *

from UI.Panel.Components.Component import Component
from UI.Panel.Elements.LabelElt import LabelElt
from UI.Panel.Elements.TextElt import TextElt

class CardDimensionComponent(Component):
	def __init__(self, parent, parentFrame, width="min", height="min", id=None, classes=[], bg=None, side=LEFT):
		super().__init__(parent, parentFrame, width, height, id, classes, bg, side)
		self.title = LabelElt("Card Dimension", self, self.frame, width="min", height="min", bg=self.bg, side=TOP)
		self.title.label.config(font=("Arial", 16))
		# self.title.label.pack()
		self.widthLabel = LabelElt("Width : ", self, self.frame, width="min", height="min", bg=self.bg, side=LEFT)
		self.width = TextElt("100", self, self.frame, format="int", height=1, width=4, bg=self.bg, side=LEFT)
		self.heightLabel = LabelElt("Height : ", self, self.frame, width="min", height="min", bg=self.bg, side=LEFT)
		self.height = TextElt("141", self, self.frame, format="int", height=1, width=4, bg=self.bg, side=LEFT)

		self.add(self.title)
		self.add(self.heightLabel)
		self.add(self.height)
		self.add(self.widthLabel)
		self.add(self.width)

	def get(self):
		return (self.width.get(), self.height.get())