#! /usr/bin/python

#TODO: Test layering

import tkinter as tk
import random

modeSelected = False

class Mode_Selection(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.pack()
		self.create_buttons()
	
	def closeWindow(self):
		global modeSelected
		modeSelected = True

	def begMode(self):
		global mode
		mode = 'beginner'
		self.closeWindow()

	def intMode(self):
		global mode
		mode = 'intermediate'
		self.closeWindow()

	def expMode(self):
		global mode
		mode = 'expert'
		self.closeWindow()
	
	def create_buttons(self):
		self.title = tk.Label(text = 'Please select a mode.\nWhen a mode has been selected, close this window.')
		self.beginnerButton = tk.Button(text = 'Beginner Mode', command = self.begMode)
		self.intermediateButton = tk.Button(text = 'Intermediate Mode', command = self.intMode)
		self.expertButton = tk.Button(text = 'Expert Mode', command = self.expMode)

		self.title.pack()
		self.beginnerButton.pack()
		self.intermediateButton.pack()
		self.expertButton.pack()

class Tile:
	def __init__(self, x, y, xRange, yRange, mineList):
		self.coordinates = [x, y]
		self.mineList = mineList
	
	def adjacentMines(self):
		self.adjacentMines = 0
		for tile in self.neighbors():
			if self.tileNeighbors[tile] in mineList:
				self.adjacentMines += 1
		return self.adjacentMines
	
	def neighbors(self):
		self.tileNeighbors = []
		for xValue in range(-1, 2):
			for yValue in range(-1, 2):
				if xValue + coordinates[0] >= 0 and xValue + coordinates[0] <= xRange and yValue + coordinates[1] >= 0 and yValue + coordinates[1] <= yRange and [xValue, yValue] != [x, y]:
					self.tileNeighbors.append([xValue, yValue])
		return self.tileNeighbors
	
class Board(tk.Frame):
	def __init__(self, tileID_dict, master = None):
		super().__init__(master)
		self.tileID_dict = tileID_dict
		self.grid()
		self.create_buttons()
	
	def tileReveal(self, tile):
		adjacentMines = tile.adjacentMines()
		neighbors = tile.neighbors()
		self.buttonBoard[tile.y][tile.x][text] = str(adjacentMines)
		print(neighbors)
		
	def buttonPress(self, event):
		ID = str(event.widget)
		if ID[-1] == 'n':
			ID += '1'
		tile = self.tileID_dict[ID]
		self.tileReveal(tile)
		
	def create_buttons(self):
		global yRange
		global xRange
		
		self.buttonBoard = []
		for y in range(yRange):
			self.buttonBoard.append([])
			for x in range(xRange):
				self.buttonBoard[y].append(tk.Button(command = self.buttonPress, width = 3, height = 1))
				self.buttonBoard[y][x].bind('<Button-1>', self.buttonPress)
				self.buttonBoard[y][x].grid(column = x, row = y)

def create_mines(mines, xRange, yRange):
	mineList = []
	for mine in range(mines):
		xValue = random.randint(1, xRange)
		yValue = random.randint(1, yRange)
		if [xValue, yValue] in mineList:
			mine += 1
		else:
			mineList.append([xValue, yValue])
	return mineList

def create_board(mode):
	global xRange
	global yRange
	
	if mode == 'beginner':
		xRange = 9
		yRange = 9
		mines = 10

	if mode == 'intermediate':
		xRange = 16
		yRange = 16
		mines = 40

	if mode == 'expert':
		xRange = 30
		yRange = 16
		mines = 99

	mineList = create_mines(mines, xRange, yRange)

	tileBoard = []
	tileID_dict = {}
	tileID = 1
	for y in range(yRange):
		tileBoard.append([])
		for x in range(xRange):
			tileBoard[y].append(Tile(x, y, xRange, yRange, mineList))
			tileID_dict['.!button' + str(tileID)] = tileBoard[y][x]
			tileID += 1
	
	Board(tileID_dict)

root = tk.Tk()
root.title('Mode Selection')
mode = Mode_Selection(master = root)
mode.mainloop()

while modeSelected == False:
	continue

create_board(mode)