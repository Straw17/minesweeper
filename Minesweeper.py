import tkinter as tk
import random

continueMain = False

class Mode_Select(tk.Frame):  
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.mode()

    def create_mines(self):
        global mineList
        global neighborsDict
        global adjacentMinesDict
        global yMax
        global xMax
        global buttonNumdict
        global buttonCoordArray
        
        mineList = []
        for mine in range(self.mineNum):
            mineCoord = random.randint(1, (xMax * yMax))
            mineList.append('.!button' + str(mineCoord))

        adjacentMinesDict = {}
        neighborsDict = {}
        reps = 1
        for row in range(yMax):
            for column in range(xMax):
                mines = 0
                if str(row) + ', ' + str(column) in ['0, 0', str(xMax) + ', 0', '0, ' + str(yMax), str(xMax) + ', ' + str(yMax)]:
                    
                    #upper-left
                    if str(row) + ', ' + str(column) == '0, 0':
                        neighborsDict['.!button' + str(reps)] = [[1, 0], [1, 1], [0, 1]]
                        for tile in range(len(neighborsDict)):
                            if buttonCoordArray[neighborsDict[row][column]] in mineList:
                                mines += 1
                        adjacentMinesDict['!button' + str(rep)] = mines

                    #upper-right
                    if str(row) + ', ' + str(column) == str(xMax) + ', 0':
                        neighborsDict['.!button' + str(reps)] = [[xMax - 1, 0], [xMax -1, 1], [xMax, 1]]
                        for tile in range(len(neighborsDict)):
                            if buttonCoordArray[neighborsDict[row][column]] in mineList:
                                mines += 1
                        adjacentMinesDict['!button' + str(rep)] = mines

                    #lower-right
                    if str(row) + ', ' + str(column) == str(xMax) + ', ' + str(yMax):
                        neighborsDict['.!button' + str(reps)] = [[xMax - 1, yMax], [xMax -1, yMax - 1], [xMax, yMax - 1]]
                        for tile in range(len(neighborsDict)):
                            if buttonCoordArray[neighborsDict[row][column]] in mineList:
                                mines += 1
                        adjacentMinesDict['!button' + str(rep)] = mines

                    #lower-left
                    if str(row) + ', ' + str(column) == '0, ' + yMax:
                        neighborsDict['.!button' + str(reps)] = [[1, yMax], [1, yMax - 1], [0, yMax - 1]]
                        for tile in range(len(neighborsDict)):
                            if buttonCoordArray[neighborsDict[row][column]] in mineList:
                                mines += 1
                        adjacentMinesDict['!button' + str(rep)] = mines
        
        global continueMain
        continueMain = True
        root.destroy()

    def begMode(self):
        global yMax
        global xMax
        
        xMax = 9
        yMax = 9
        self.mineNum = 10
        self.create_mines()

    def intMode(self):
        global yMax
        global xMax
        
        xMax = 16
        yMax = 16
        self.mineNum = 40
        self.create_mines()

    def expMode(self):
        global yMax
        global xMax
        
        xMax = 30
        yMax = 16
        self.mineNum = 99
        self.create_mines()
    
    def mode(self):
        self.modeFunctionTitle = tk.Label(text = 'Please select an option')
        self.beginnerButton = tk.Button(text = 'Beginner Mode', command = self.begMode)
        self.intermediateButton = tk.Button(text = 'Intermediate Mode', command = self.intMode)
        self.expertButton = tk.Button(text = 'Expert Mode', command = self.expMode)
        
        self.modeFunctionTitle.pack()
        self.beginnerButton.pack()
        self.intermediateButton.pack()
        self.expertButton.pack()

class Main_Window(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.grid()
        self.create_buttons()

    def button_press(self, event):
        global mineList
        global adjacentMinesDict
        global neighborsDict
        
        button = str(event.widget)
        if button[-1] == 'n':
            button += '1'
        if button in mineList:
            x = self.buttonNumDict[button][0]
            y = self.buttonNumDict[button][1]
            self.buttons[y][x].config(text = 'B')
        else:
            x = self.buttonNumDict[button][0]
            y = self.buttonNumDict[button][1]
            self.buttons[y][x].config(text = str(adjacentMinesDict[button]))

    def create_buttons(self):
        global xMax
        global yMax
        global buttonNumdict
        global buttonCoordArray
        
        self.buttons = []
        self.buttonNum = 0
        buttonNumDict = {}
        buttonCoordArray = []
        for y in range(yMax):
            self.buttons.append([])
            self.buttonCoordArray.append([])
            for x in range(xMax):
                self.buttons[y].append(x)
                self.buttons[y][x] = tk.Button(command = self.button_press, width = 3, height = 1)
                self.buttons[y][x].grid(column = str(x), row = str(y))
                self.buttonNum += 1
                buttonNumDict['.!button' + str(self.buttonNum)] = [x, y]
                buttonCoordArray[y][x].append('.!button' + str(self.buttonNum))
                self.buttons[y][x].bind('<Button-1>', self.button_press)

root = tk.Tk()
mode = Mode_Select(master = root)
mode.mainloop()

while continueMain == False:
    continue

root = tk.Tk()
main = Main_Window(master = root)
main.mainLoop()
