#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Import Libraries
import random

# Generate 4*4 grid initially filled with 0's
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

# Randomly add 2
def add_new_2(mat):
    # Generate random row and column index in range 0 to 3
    r = random.randint(0,3)
    c = random.randint(0,3)
    while(mat[r][c] != 0): # Keep generating till we get empty place
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c] = 2 # Add 2 at empty place
    return mat

# Reverse each row   
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return new_mat

# Matrix Transpose
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

# Merge same values except zeros
def merge(mat):
    changed = False # By default no change
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j]!=0:
                mat[i][j] = mat[i][j]*2 # Merged value
                mat[i][j+1] = 0 # After merging previous place will become empty
                changed = True # Inside if block because of merge changed will be True
    return mat,changed

# Move all non zero values to left
def compress(mat):
    changed = False # By default no change
    # Create new matrix initially filled with 0's
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True # If column of element is changed means location is changed
                pos+=1
    return new_mat,changed

# Up move
def move_up(grid):
    # We can implement up move using left move logic after transposing the matrix
    transposed_grid = transpose(grid)
    new_grid,changed1 = compress(transposed_grid) # changed1 will be True if compress changed matrix
    new_grid,changed2 = merge(new_grid) # changed2 will be True if merge changed matrix
    changed = changed1 or changed2 # change detected
    new_grid,temp = compress(new_grid)
    final_grid = transpose(new_grid) # Transpose again to get final matrix
    return final_grid,changed # We will add 2 at random place only if there is change in matrix

# Down move
def move_down(grid):
    # We can implement down move using right move logic after transposing the matrix
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid,changed1 = compress(reversed_grid) # changed1 will be True if compress changed matrix
    new_grid,changed2 = merge(new_grid) # changed2 will be True if merge changed matrix
    changed = changed1 or changed2 # change detected
    new_grid,temp = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid) # Transpose again to get final matrix
    return final_grid,changed # We will add 2 at random place only if there is change in matrix

# Right move
def move_right(grid):
    # We can implement right move using left move logic after reversing the matrix
    reversed_grid = reverse(grid)
    new_grid,changed1 = compress(reversed_grid) # changed1 will be True if compress changed matrix
    new_grid,changed2 = merge(new_grid) # changed2 will be True if merge changed matrix
    changed = changed1 or changed2 # change detected
    new_grid,temp = compress(new_grid)
    final_grid = reverse(new_grid) # Reverse again to get final matrix
    return final_grid,changed # We will add 2 at random place only if there is change in matrix

# Left move
def move_left(grid):
    # Using compress, merge and compress we can implement left move
    new_grid,changed1 = compress(grid) # changed1 will be True if compress changed matrix
    new_grid,changed2 = merge(new_grid) # changed2 will be True if merge changed matrix
    changed = changed1 or changed2 # change detected
    new_grid,temp = compress(new_grid)
    return new_grid,changed # We will add 2 at random place only if there is change in matrix

def get_current_state(mat):
    # WON
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048: # If at any index we get 2048 it means game WON
                return 'WON'
            
    # GAME NOT OVER
    # Check for 0 anywhere
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0: # If at any index 0 is present it means moves are still possible
                return 'GAME NOT OVER'
    # Check if consecutive elements are equal
    # Check every row and column except last row and last column
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
                return 'GAME NOT OVER'
    # Check last row
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'GAME NOT OVER'
    # Check last column
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'GAME NOT OVER'
    
    return 'LOST'


# In[ ]:




