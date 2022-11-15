#!/usr/bin/env python
# coding: utf-8

# In[2]:


SIZE = 400 # Size of grid
GRID_LEN = 4 # Grid 4*4 ie 16 cells each of 400/4=100 size
GRID_PADDING = 10 # Grid padding

BACKGROUND_COLOR_GAME = "#92877d" # Background color
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a" # Background color of empty cell

# Different background color of cell for different numbers
BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                         16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                         1024: "#edc53f", 2048: "#edc22e",
                         
                         4096: "#eee4da", 8192: "#edc22e", 16384: "#f2b179",
                         32768: "#f59563", 65536: "#f67c5f"}

# Different text color of cell for different numbers
CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2",
                   16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2",
                   128: "#f9f6f2", 256: "#f9f6f2", 512: "#f9f6f2",
                   1024: "#f9f6f2", 2048: "#f9f6f2",
                   
                   4096: "#776e65", 8192: "#f9f6f2", 16384: "#776e65",
                   32768: "#776e65", 65536: "#f9f6f2"}

FONT = ("Verdana", 40, "bold") # Font

# Keys used for movement
KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"


# In[ ]:




