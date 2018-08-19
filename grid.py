#!/usr/bin/python3
from tkinter import *
import numpy as np
from world_gen import *
import os

class Cell():

    EMPTY_COLOR_BG = "white"
    EMPTY_COLOR_BORDER = "black"

    def __init__(self, master, x, y, size):
        #Constructor of the object called by Cell
        self.master = master
        self.abs = x
        self.ord = y
        self.size= size
        self.fill= 0

    def _switch(self):
        #Switch the cell fill color
        self.fill+=1

    def draw(self):
        #Fill selected cell on grid canvas
        if self.master != None :

            if self.fill%3==1:
                fill = "dark blue"
                outline = "dark blue"
            elif self.fill%3==2:
                fill = "blue"
                outline = "blue"
            else:
                fill = "white"
                outline = "black"

            xmin = self.abs * self.size
            xmax = xmin + self.size
            ymin = self.ord * self.size
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline)

    def drawinitial(self):
        if self.master != None :
            if not self.fill:
                fill = Cell.EMPTY_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER

            xmin = self.abs * self.size
            xmax = xmin + self.size
            ymin = self.ord * self.size
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline)


class CellGrid(Canvas):
    def __init__(self,master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber, *args, **kwargs)

        self.cellSize = cellSize
        self.totalRows = rowNumber
        self.totalColumns = columnNumber
        self.CompleteGrid = np.zeros((rowNumber,columnNumber))

        self.grid = []
        for row in range(rowNumber):

            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize))

            self.grid.append(line)

        #memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.switched = []

        #bind click action
        self.bind("<Button-1>", self.handleMouseClick)
        #bind moving while clicking
        #   self.bind("<B1-Motion>", self.handleMouseMotion)
        #bind release button action - clear the memory of midified cells.
        #self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())
        self.drawinitial()



    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def drawinitial(self):
        for row in self.grid:
            for cell in row:
                cell.drawinitial()

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def handleMouseClick(self, event):
        row, column = self._eventCoords(event)
        self.setRoad(row,column)
        cell = self.grid[row][column]
        cell._switch()
        cell.draw()
        #add the cell to the list of cell switched during the click
        self.switched.append(cell)
    """
    def handleMouseMotion(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if cell not in self.switched:
            cell._switch()
            cell.draw()
            self.switched.append(cell)
    """
    def printgrid(self):
        for row in self.CompleteGrid:
            print(" ".join(str(int(i)) for i in row))

    def setRoad(self,row,col):
        if self.CompleteGrid[row][col] == 1:
            self.CompleteGrid[row][col] = 2
        elif self.CompleteGrid[row][col] == 2:
            self.CompleteGrid[row][col] = 0
        else:
            self.CompleteGrid[row][col] = 1


#if __name__ == "__main__" :
def OpenGrid(w):
    app = Tk()

    grid = CellGrid(app,w.rows,w.cols,25)
    grid.pack()
    Button(app,text="Generate Roadmap",command=app.destroy).pack()
    app.mainloop()
    grid.printgrid()

    worldGenerator(grid,w)
