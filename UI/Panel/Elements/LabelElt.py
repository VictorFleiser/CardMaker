from tkinter import *

from UI.Panel.Components.Component import Component
from UI.Panel.Elements.Element import Element

class LabelElt(Element):
	def __init__(self, text, parent: Component, parentFrame, width="min", height="min", id=None, classes=[], bg=None, side=LEFT):
		super().__init__(parent, parentFrame, width, height, id, classes, bg, side)
		self.text = text
		self.label = Label(self.frame, text=self.text, bg=self.bg, width=0 if (type(self.width) == str) else self.width, height=0 if (type(self.height) == str) else self.height)
		self.label.pack()
