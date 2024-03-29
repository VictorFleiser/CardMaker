from tkinter import *

from UI.Panel.Components.Component import Component
from UI.Panel.Elements.LabelElt import LabelElt
from UI.Panel.Elements.TextElt import TextElt

class CollapsibleComponent(Component):
	def __init__(self, parent, parentFrame, title, width="min", height="min", id=None, classes=[], bg=None, side=LEFT):
		super().__init__(parent, parentFrame, width, height, id, classes, bg, side)

		self.title = LabelElt(title, self, self.frame, width="min", height="min", bg=self.bg, side=TOP)
		self.title.label.config(font=("Arial", 16))

		self.collapsibleFrame = Frame(self.frame, width=None if (type(self.width) == str) else self.width, height=None if (type(self.height) == str) else self.height, bg=self.bg, relief='raised', borderwidth=1)
		self.collapsibleFrame.pack()

		self.collapsed = False
		self.add(self.title)


		self.title.label.bind("<Button-1>", self.toggle)
		self.title.label.bind("<Return>", self.toggle)


		self.title.label.config(cursor="hand2")
		self.title.label.config(bg="lightgrey")
	
	def toggle(self, event):
		if self.collapsed:
			self.collapsibleFrame.pack()
			self.collapsed = False
		else:
			self.collapsibleFrame.pack_forget()
			self.collapsed = True