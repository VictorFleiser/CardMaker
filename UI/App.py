from tkinter import *
from .Panel.Panel import Panel
from .Viewer.Viewer import Viewer
from .MenuBar import MenuBar

class App:
	"""
	Root class for the application
	"""
	def __init__(self, width=1200, height=800) :
		# Create the root window
		self.root = Tk()
		self.root.title("Hello World")
		self.root.geometry(f"{width}x{height}")
		self.root.minsize(400, 400)

		# Create a frame to hold the viewer and the panel
		self.frame = Frame(self.root)
		self.frame.pack(fill='both', expand=True)

		# Menu Bar
		self.menu_bar = MenuBar(self.root)

		# Create a paned window to hold the viewer and the panel
		self.paned_window = PanedWindow(self.frame, orient='horizontal', sashrelief='raised', sashwidth=5, handlepad=3)
		self.paned_window.pack(fill='both', expand=True)
		self.viewer = Viewer(self, "Viewer", width//2)
		self.panel = Panel(self, "Panel", width//2)

		# Start the main loop		
		self.root.mainloop()
	