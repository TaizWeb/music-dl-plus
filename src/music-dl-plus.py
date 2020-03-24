import subprocess
import os
import tkinter as tk

interface = tk.Tk()
formats = ["ogg", "opus", "mp3", "wav", "flac"]

class StartText:

	def create(self):
		# Creating elements
		self.openingText = tk.Label(text="Welcome to music-dl, a tool built on youtube-dl!")
		self.downloadButton = tk.Button(interface, text="Download")
		self.infoButton = tk.Button(interface, text="Info")
		self.quitButton = tk.Button(interface, text="Quit")

		# Placing them on the grid
		self.openingText.grid(column=0, row=0)
		self.downloadButton.grid(column=0, row=1)
		self.infoButton.grid(column=0, row=2)
		self.quitButton.grid(column=0, row=3)

		# Binding to functions
		self.infoButton.bind("<Button-1>", info)
		self.quitButton.bind("<Button-1>", quit)

	def clear(self):
		self.openingText.destroy()
		self.downloadButton.destroy()
		self.infoButton.destroy()
		self.quitButton.destroy()

def info(event):
	startup.clear()
	infoText = tk.Label(text="This is some info")

def quit(event):
	interface.quit()

startup = StartText()
startup.create()

interface.mainloop()

