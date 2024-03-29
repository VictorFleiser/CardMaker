from tkinter import *
from UI.Panel.Components.Component import Component
from UI.Panel.Elements.Element import Element

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	# avoid circular import at runtime
	from UI.App import App

class Panel:
	"""
	Class to hold the components panel
	"""
	def __init__(self, parent : 'App', title, width):
		# Set the title and parent
		self.title = title
		self.parent : App = parent

		# Create the frame to hold the panel
		self.frame = Frame(self.parent.paned_window, bg='blue', width=width)

		# contents
		self.contents = []

		# Create a label to display the title
		self.label = Label(self.frame, text=self.title)
		self.label.pack()

		# create a test component :
		from UI.Panel.Components.Component import Component
		self.d = Component(self, self.frame, width="fill", height="min", bg='green')
		self.add(self.d)
		self.c = Component(self, self.frame, height=50, bg='yellow')
		self.add(self.c)
		self.e = Component(self, self.frame, bg='pink')
		self.add(self.e)
		from UI.Panel.Elements.LabelElt import LabelElt
		from UI.Panel.Elements.ButtonElt import ButtonElt
		# self.c.add(LabelElt("heeeyya!", self.c, width=300, height=300, bg='grey'))
		# self.d.add(LabelElt("heeeyya!", self.d, bg='grey'))
		# self.e.add(LabelElt("heeeyya!", self.e, height=300, bg='grey'))

		self.d.add(LabelElt("heeeyya!", self.d, self.d.frame, bg='brown', side=LEFT))
		self.d.add(ButtonElt("heeeyya!", lambda: print("heeeyya!"), self.d, self.d.frame, bg='purple', side=LEFT))
		self.d.add(ButtonElt("heeeyyooo?", lambda: print("heeeyyooo?!"), self.d, self.d.frame, bg='yellow'))
		from UI.Panel.Elements.TextElt import TextElt
		self.c.add(TextElt("heeeyya!", self.c, self.c.frame, width=53, height=6, bg='grey'))
		self.c.add(ButtonElt("print text", lambda: print(self.c.contents[0].get()), self.c, self.c.frame, bg='purple'))

		from UI.Panel.Components.CardDimensionComponent import CardDimensionComponent

		self.e.add(CardDimensionComponent(self.e, self.e.frame, bg='grey'))
		self.e.add(ButtonElt("print dimensions", lambda: print(self.e.contents[0].get()), self.e, self.e.frame, bg='purple'))

		from UI.Panel.Components.EditDimensionsComponent import EditDimensionsComponent
		self.e.add(EditDimensionsComponent(self.e, self.e.frame, bg='grey'))

		from UI.Panel.Components.CollapsibleComponent import CollapsibleComponent
		f = CollapsibleComponent(self.e, self.e.frame, title="collapsible test", bg='grey', side=LEFT)
		f.add(EditDimensionsComponent(f, f.collapsibleFrame, bg='grey'))
		g = CollapsibleComponent(f, f.collapsibleFrame, title="collapsibler test", bg='grey', side=TOP)
		f.add(g)
		g.add(EditDimensionsComponent(g, g.collapsibleFrame, bg='grey'))
		self.e.add(f)
		# Add the frame to the paned window
		self.parent.paned_window.add(self.frame, stretch='always')

		
	def add(self, component : 'Component|Element'):
		self.contents.append(component)