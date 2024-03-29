from tkinter import *

def focus_next_widget(event):
	event.widget.tk_focusNext().focus()
	return("break")

def focus_previous_widget(event):
	event.widget.tk_focusPrev().focus()
	return("break")