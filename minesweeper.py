# Program mineSweeper
# Description: 
# 	    A 9x9 grid where the user inputs a command for a square
#           without hitting the 10 bombs in the grid
# Author: Alvin Tran
# Date: 11/13/2019
# Revised: 
# 	11/15/2019  11/28/2019  12/8/2019
# 	11/20/2019  11/30/2019  12/9/2019
#       11/25/2019  12/3/2019
#       11/26/2019  12/6/2019
#       11/27/2019  12/7/2019
import os
import random
import time
import copy

# Declare global constants (name in ALL_CAPS)
FILE_NAME = 'instructions.txt'
#declare global markers
total_markers = 0


def main():
    
    try:
        introduction(FILE_NAME)

        replay(FILE_NAME)

    except Exception as sysMsg:
        print(sysMsg)

    # Declare and INITIALIZE Variables (EVERY variable used in this main program)

def introduction(FILE_NAME):
    
    instructions = ''

    line = "\nThere are 10 bombs placed randomly in a 9x9 grid.\n"

    line1 = "The goal of the game is to type in coordinates of a square, e.g A1. without hitting a bomb.\n"

    line2 = "A sqaure that doesn't have a bomb behind it, and adjacent squares with # equal to 0 will reveal several other squares.\n"

    line3 = "Pay attention to the number after unlocking a square, "
    line3 += "they provide hints to how many bombs are surrounding that particular square\n"

    line4 = "You are able to mark squares that you think may be bombs"

    line4 += " by typing 'M' followed by the coordinates of that square. e.g. MD4\n"
    line5 = "You may also deselect a square you have marked by typing in the same coordinates "
    line5 += "that you marked the square with.\nThis will reset the total marker count you've used by however many you've deselected.\n"
    line5 += "Be aware of your markers because it won't adjust if squares that you marked are unlock.\n"
    line5 += "This adds a bit of a challenge so you're actively rationalizing where the next bomb will be, as long with being more attentive with your markers.\n"

    line6 = "Once you open all the squares without hitting a bomb, you win!\n"

    introduction = line + line1 + line2 + line3 + line4 + line5 + line6
                                    
    
    #Introduction
    
    print('Welcome to Minesweeper python v.2.0!')
    print('====================================')
    print('A game that involves a little bit of luck and skills using probability! \n') 

    #Writes and saves a file called instructions as a text file

    instructions = open(FILE_NAME, 'w')
    
    instructions.write(introduction)

    instructions.close()

#End Function introduction()

# Function replay()
# Description:
#   Asks the player if they want to read instructions.
#   Shows instructions if they press anything other than n
#   Calls functions to place mine in grid
#
# Calls:
#   placeMine()
#   
# Parameters:
#   FILE_NAME
#   
# Returns:
#   status String # either stopped by command or error
    

def replay(FILE_NAME):
    
    #Ask if the player wants to read the instructions
    ask_read_instructions = str(input("Do you want to read the instructions? Type 'n' if you don't, otherwise press anything: "))

    #Keeps looping the instructions as long as the player doesn't type 'n'
    if ask_read_instructions.lower() != 'n':

        os.system("cls")

        instructions_read = open(FILE_NAME, 'r')

        print(instructions_read.read())

        instructions_read.close()

        input("Press [Enter] to play: ")

    elif ask_read_instructions.lower() == 'n':

        os.system("cls")

        input("Press [Enter] to play: ")

    else:
        os.system("cls")
        replay(FILE_NAME)

    #End If
    
    #The 9x9 grid
    m = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    

    #calls function that places a mine 10 random times in the grid
    #{
    for i in range( 10 ):
        placeMine(m)

    #}

    #Adds a 1 to the 0's in the grid that are surrounded by bombs.
    #{
    for r in range( 0, 9 ):
        for c in range( 0, 9 ):
            value = coordValue( r, c, m)
            if value == '*':
                update_grid_values( r, c, m )
    
    #Creates an empty grid because mines aren't placed yet
    e = [['?', '?', '?', '?', '?', '?', '?', '?', '?'],
         ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
         ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
         ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
         ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
         ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
         ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
         ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
         ['?', '?', '?', '?', '?', '?', '?', '?', '?']]
    

    
    displayBoard(e)

    #starts the time and plays the game
    startTime = time.time()

    play( m, e, startTime)
    #}
            
#End Function replay

# Function coordValue(m)
# Description:
#      Displays the value of a coordinate on the grid
# Calls:
#       none
# Parameters:
#       none
# Returns:
#       m[r][c]

def coordValue( r, c, m ):
    
    return m[r][c]

#End Function coordValue

# Function coordValueDisplay()
# Description:
#        Displays the 0's as blanks on the grid
# Calls:
#       none
# Parameters:
#       m   list
#       r   int
#       c   int
#       
# Returns:
#       none

def coordValueDisplay( r, c, m ):
    
    value = m[r][c]
   
    if value == 0:
        return ' '
    return value

#End Function coordValueDisplay()
    

# Function update_grid_values()
# Description:
#      Updates the grid value by adding a 1 to each grid that's surrounded by a bomb
#      Updates the grid value specific to certain rows and columns by indexing
# Calls:
#       none
# Parameters:
#       ri  int
#       c   int
#       m   list
# Returns:
#       
def update_grid_values(ri, c, m):
    
    #Updates values of the row above
    #{
    if ri-1 > -1:
        r = m[ri-1]
        #{
        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1
        #}
    #Updates values of the same row.    
    r = m[ri]
    
    if c-1 > -1:
        if not r[c-1] == '*':
            r[c-1] += 1

    if 9 > c+1:
        if not r[c+1] == '*':
            r[c+1] += 1

    
    #Updates values of the row below.
    if 9 > ri+1:
        r = m[ri+1]
        #{
        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1
      #}  
    #}

#End function update_grid_values()

# Function placeMine(m)
# Description:
#       Places a mine in a random location in grid m by indexing rows and columns
# Calls:
#       placeMine()
#   
# Parameters:
#       m   list
# Returns:
#       none

def placeMine(m):
    #{
    r = random.randint(0,8)
    c = random.randint(0,8)

    #Places a mine at a random location or at a different location if a mine is already at the current location
    currentRow = m[r]
    if not currentRow[c] == "*":
        currentRow[c] = "*"
    else:
        placeMine(m)
    #}

#End Function placeMine()

# Function displayBoard()
# Description:
#       displays the board 
# Calls:
#       coordValueDisplay()
# Parameters:
#       m   str
# Returns:
#       none

def displayBoard(m):
    
    os.system("cls")
    for indent in range(35):
        print()
    #End For

    print('    A   B   C   D   E   F   G   H   I')
    print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')

    #Displays the value by indexing. Middle number are columns which stay the same for each row
    # r are rows that loop down 9 times. Starts at index 0 column in a row and stops at a mine. 
    # Prints vertical walls between each column 
    for r in range (0, 9):
        
        print (r,'║',(coordValueDisplay(r,0,m)),'║',(coordValueDisplay(r,1,m)),
                 '║',(coordValueDisplay(r,2,m)),'║',(coordValueDisplay(r,3,m)),
                 '║',(coordValueDisplay(r,4,m)),'║',(coordValueDisplay(r,5,m)),
                 '║',(coordValueDisplay(r,6,m)),'║',(coordValueDisplay(r,7,m)),'║',(coordValueDisplay(r,8,m)),'║')
    
        #Prints the lines above and below each row but not after the last row 
        if not r == 8:
            print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    
    print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')
    global total_markers
    print('Total Markers Used: ', total_markers)
    

        #End If
    
    #End For
        
#End Function displayBoard()

# Function commandInput()
# Description:
#       User will input coordinates as a command to fill in the grid 
# Calls:
#       play()
#       marker()
# Parameters:
#       m   list
#       e   list
#       startTime  int
# Returns:
#       none


def commandInput(m, e, startTime):

    #Declare Variables
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    
    #This will keep looping if there are incorrect commands
    while True:
        choose_square = input('Input coordinates for square (ex. A4) or place a marker (ex.MB4): ').lower()
        
        #Checks to see if a square hasn't been chosen before and puts a marker if there's an m in the first index
        if len(choose_square) == 3 and choose_square[0] == 'm' and choose_square[1] in letters and choose_square[2] in numbers:

            c, r = (ord(choose_square[1]))-97, int(choose_square[2])
            marker(r, c, e)
            play(m, e, startTime)
            break
        
        

        elif len(choose_square) == 2 and choose_square[0] in letters and choose_square[1] in numbers: 
            
            return (ord(choose_square[0]))-97, int(choose_square[1])
        
        else: 
            choose_square
        
    
    
        
        #End If

    #End While

#End Function commandInput()

# Function zero_open_squares()
# Description:
#        Squares that have a 0 value when a command goes through will unlock squares around it
# Calls:
#       coordValue()
# Parameters:
#       m   list
#       e   list
#       r   list
#       c   list
# Returns:
#       none
   
def zero_open_squares(r, c, e, m):
    global total_markers
    #Reveals the squares that have zereos for the row above 
    #{
    if r-1 > -1:
        row = e[r-1]

        if c-1 > -1: 
            row[c-1] = coordValue(r-1, c-1, m)
            
        row[c] = coordValue(r-1, c, m)

        if 9 > c+1: 
            row[c+1] = coordValue(r-1, c+1, m)
    

    #Reveals the squares that have zereos for the same row
    row = e[r]
    
    if c-1 > -1: 
        row[c-1] = coordValue(r, c-1, m)
        
    if 9 > c+1: 
        row[c+1] = coordValue(r, c+1, m)
        

    #Reveals the squares that have zereos for the row below
    if 9 > r+1:
        row = e[r+1]

        if c-1 > -1: 
            row[c-1] = coordValue(r+1, c-1, m)
            
        row[c] = coordValue(r+1, c, m)

        if 9 > c+1: 
            row[c+1] = coordValue(r+1, c+1, m)
            

    #}

#End Function zero_open_squares()

#Checks a grid for 0s

# Function checkZeroes()
# Description:
#        Checks the grid for 0's
# Calls:
#       coordValue()
#       zero_open_squares()
# Parameters:
#       m   list
#       e   list
#       r   list
#       c   list
# Returns:
#       none

def checkZeros(e, m, r, c):
    
    emptyGrid = copy.deepcopy(e)
    zero_open_squares(r, c, e, m)
    #{
    if emptyGrid == e:
        return
    #}
    #{
    while True:
        emptyGrid = copy.deepcopy(e)
        
        for r in range (9):
            
            for c in range (9):
                
                if coordValue(r, c, e) == 0:
                    zero_open_squares(r ,c ,e, m)
        
        if emptyGrid == e:
            return
    #}

#End Function checkZeroes

# Function marker()
# Description:
#        Places a marker at the location from the command
# Calls:
#       displayBoard()
#       removeMarker()
#       coordValue()
# Parameters:
#       e   list
#       r   list
#       c   list
# Returns:
#       none

def marker(r, c, e): 

    global total_markers

    if coordValue(r,c,e) == '?':
        e[r][c] = '⚐'
        total_markers += 1
    else:
        removeMarker(r,c,e)
    
    displayBoard(e)

#End Function marker()
    
# Function removemarker()
# Description:
#        Removes the marker that was placed with ? and lowers the count by 1 for each marker deselected.
# Calls:
#       coordValue()
# Parameters:
#       e   list
#       r   list
#       c   list
# Returns:
#       none

def removeMarker(r, c, e):

    global total_markers
    if coordValue(r,c,e) == '⚐':
        e[r][c] = '?'
        total_markers -= 1
            

#End removemarker()
             

# Function play()
# Description:
#        Checks the grid for 0's
# Calls:
#       commandInput()  
#       coordValue()
#       displayBoard()
#       replay()
#       checkZeroes()
# Parameters:
#       m   list
#       e   list
#       startTime   int
#       
# Returns:
#       none

def play( m, e, startTime ):

    #Declare and initialize variables
    restart = ''
    
    
    #Player will input a command to choose a square
    c, r = commandInput( m, e, startTime )
    
    #Calculates the value at coordinates
    value = coordValue( r, c, m )
    #{
    #if you hit a bomb then you lose and games ends
    if value == '*':
        displayBoard(m)
        print('Sorry, You Lose! You may try again!')
        
        #Displays the timer result
        print('Time: ' + str(round(time.time() - startTime)) + 's')
        
        #Asks to play again
        restart = input('Play again? (Y/N): ').lower()
        if restart == 'y':
            global total_markers
            total_markers = 0
            replay(FILE_NAME)
        else:
            quit()

    #Inputs the value into the empty grid e
    e[r][c] = value
    
    #Checks if the value is 0 and displays the empty board
    if value == 0:

        checkZeros(e, m, r, c)

    displayBoard(e)
    
    #Checks and displays if you have won
    squaresLeft = 0
    
    for x in range (0, 9):
        row = e[x]
        squaresLeft += row.count('?')
        squaresLeft += row.count('⚐')
    
    if squaresLeft == 10:

        displayBoard(m)
        print('Congratualations, You win!')
        
        #Print result of time finished
        print("You've finished in: " + str(round(time.time() - startTime)) + 's')
        
        #Asks to play again
        restart = input('Would you like to play again? (Y/N): ')
        restart = restart.lower()
        
        if restart == 'y':
            total_markers = 0
            replay(FILE_NAME)
        else:
            quit()
    #}
    #This will keep repeating
    play(m, e, startTime)

#End Function play()


main()
    


    




