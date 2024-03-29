from tkinter import *

from UI.Panel.Components.Component import Component
from UI.Panel.Elements.Element import Element

class ButtonElt(Element):
	def __init__(self, text, command, parent: Component, parentFrame, width="min", height="min", id=None, classes=[], bg=None, side=LEFT):
		super().__init__(parent, parentFrame, width, height, id, classes, bg, side)
		self.text = text
		self.command = command
		self.button = Button(self.frame, command=self.command, text=self.text, bg=self.bg)
		self.button.pack()
