import subprocess
import os
import tkinter as tk

interface = tk.Tk()
formats = ["ogg", "opus", "mp3", "wav", "flac"]

class MusicDL(tk.Frame):
	def __init__(self):
		self.createStartup()

	def createStartup(self):
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
		self.infoButton.bind("<Button-1>", self.createInfo)
		self.quitButton.bind("<Button-1>", quit)
		self.downloadButton.bind("<Button-1>", self.createDownload)

	def clearStartup(self):
		self.openingText.destroy()
		self.downloadButton.destroy()
		self.infoButton.destroy()
		self.quitButton.destroy()

	def createInfo(self, event):
		self.clearStartup()
		rawInfo = "\nIn order to run music-dl, you need the following installed at their LATEST version:\nPython 3.6+: Can be installed from your systems package manager or from python.org, run python -v to check your installed version\nyoutube-dl: Installed with 'pip install youtube-dl', can be upgraded with 'pip install --upgrade youtube-dl'\nffmpeg: Installed/upgraded with your system's package manager. Debian-based users can run 'sudo apt install ffmpeg'"
		self.infoText = tk.Label(text=rawInfo)
		self.infoText.grid(column=0, row=0)

		self.backButton = tk.Button(interface, text="Back")
		self.backButton.grid(column=0, row=1)
		self.backButton.bind("<Button-1>", self.backInfo)

	def clearInfo(self):
		self.infoText.destroy()
		self.backButton.destroy()

	def backInfo(self, event):
		self.clearInfo()
		self.createStartup()
	
	def createDownload(self, event):
		self.clearStartup()

		# Download URL label
		self.downloadLabel = tk.Label(text="Enter YouTube URL: ")
		self.downloadLabel.grid(column=0, row=0)

		# Download URL input
		self.downloadLink = tk.Entry(interface, text="Enter YouTube URL...")
		self.downloadLink.grid(column=1, row=0)

		# Download location button
		self.downloadLocation = tk.Button(interface, text="Select location")
		self.downloadLocation.grid(column=0, row=1)
		self.downloadLocation.bind("<Button-1>", self.chooseFolder)
		
		# Confirmation button
		self.confirmationButton = tk.Button(interface, text="Get Album")
		self.confirmationButton.grid(column=0, row=2)
		self.confirmationButton.bind("<Button-1>", self.downloadAlbum)
	
	def chooseFolder(self, event):
		pass
	
	def downloadAlbum(self, event):
		print(self.downloadLink.get())

	def quit(event):
		interface.quit()

app = MusicDL()
interface.mainloop()

