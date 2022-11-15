#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Import Libraries
from tkinter import Frame, Label, CENTER
# Frame allows to create box in which we can place all our widgets
import LogicsFinal
import constants as c

class Game2048(Frame): # class Game2048 will inherit Frame
    def __init__(self):
        Frame.__init__(self) # Frame created

        self.grid() # Frame visualized as grid
        self.master.title('2048') # Grid title
        self.master.bind("<Key>", self.key_down) # If any key is pressed go to key_down function
        # Key map
        self.commands = {c.KEY_UP: LogicsFinal.move_up, c.KEY_DOWN: LogicsFinal.move_down,
                        c.KEY_LEFT: LogicsFinal.move_left, c.KEY_RIGHT: LogicsFinal.move_right}

        self.grid_cells = [] # Empty grid created
        self.init_grid() # Add the grid cells
        self.init_matrix() # Start game and add two 2's randomly
        self.update_grid_cells() # Update background and text color according to values

        self.mainloop() # Actually run the program after everything is ready
    
    def init_grid(self):
        # Background cell of size 400*400
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME, width=c.SIZE, height=c.SIZE)
        background.grid()
        
        # Create cells
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY, width=c.SIZE/c.GRID_LEN, height=c.SIZE/c.GRID_LEN)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING, pady=c.GRID_PADDING)
                
                # Cell text
                t = Label(master=cell, text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)
            
            self.grid_cells.append(grid_row)
    
    def init_matrix(self):
        # Start game
        self.matrix = LogicsFinal.start_game()
        # Add two 2's at random place
        LogicsFinal.add_new_2(self.matrix)
        LogicsFinal.add_new_2(self.matrix)
    
    # Update background and text color according to values
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),bg=c.BACKGROUND_COLOR_DICT[new_number],fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks() # Wait till all colors change as it may take time
    
    def key_down(self, event): # event means what key is pressed
        key = repr(event.char) # event.char gives key
        if key in self.commands: # Only do something if key is in commands ie w,s,a or d
            # reper gives printable part of
            self.matrix, changed = self.commands[repr(event.char)](self.matrix) # Move according to input
            if changed:
                LogicsFinal.add_new_2(self.matrix) # Add new 2 everytime change happens
                self.update_grid_cells() # Update grid cells
                changed = False # Reset changed
                
                # Display result
                if LogicsFinal.get_current_state(self.matrix) == "WON":
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if LogicsFinal.get_current_state(self.matrix) == "LOST":
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

gamegrid = Game2048()


# In[ ]:




