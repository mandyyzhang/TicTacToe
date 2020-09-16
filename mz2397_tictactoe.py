#Mandy Zhang
#CS-UY 1114
#Final project

import turtle
import time
import random

# This list represents the state of the
# board. It's a list of nine strings,
# each of which is either "X", "O", "_",
# representing, respectively,
# a position occupied by an X, by an O, and
# an unoccupied position. The first three
# elements in the list represent the first row,
# and so on. Initially, all positions are
# unoccupied.
the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]



import math
boxes = [0,1,2,3,4,5,6,7,8] #list of positions on the board

#setting the width and height on the screen
w=turtle.window_width()
h=turtle.window_height()

row1 = [0,1,2]
row2 = [3,4,5]
row3 = [6,7,8]
column1 = [0,3,6]
column2 = [1,4,7]
column3 = [2,5,8]
dia1 = [2,4,6]
dia2 = [0,4,8]
lst = [row1,row2,row3,column1,column2,column3,dia1,dia2]#list of all possible ways for a win 


def draw_board(board):
    """
    signature: list(str) -> NoneType
    The current state of the board, indicating
    the position of all pieces, is given
    as a parameter. This function should draw
    the entire board on the screen using turtle.
    It must draw the grid lines as well as
    the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.clear()
    # initialize x and y coordinates
    x_cor = 0
    y_cor = 0

    hypo = math.sqrt(((h/3) ** 2) + ((w/3) ** 2))
    angle = math.atan((h/3)/(w/3))
    angle = math.degrees(angle)

    
#Vertical Lines of board
    turtle.setheading(90)
    turtle.penup()
    turtle.goto(-w/6,-h/2)
    turtle.pendown()
    turtle.forward(h)
    
    turtle.penup()
    turtle.goto(w/6,-h/2)
    turtle.pendown()
    turtle.forward(h)

#Horizontal Lines of board
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(-w/2,h/6)
    turtle.pendown()
    turtle.forward(w)
    
    turtle.penup()
    turtle.goto(-w/2,-h/6)
    turtle.pendown()
    turtle.forward(w)

    turtle.bgcolor("pink")

#Drawing the circle
    for i in range(len(board)):
        if board[i] =="O":
            turtle.color("purple")
            if i < 3:
                x_cor= ((w /3)*i) - (w /3)
                y_cor= h/3
            elif 2< i <6:
                x_cor= (w/3)*i - ((w/3) * 4)
                y_cor = 0
            elif 5< i < 9:
                x_cor= (w/3)*i - ((w/3) * 7)
                y_cor = -h/3
            y_cor -= 16
    
            turtle.penup()
            turtle.goto(x_cor,y_cor - h/7)
            turtle.pendown()

            if h > w:
                turtle.circle(w/6)
            else:
                turtle.circle(h/6)
#Drawing the Xs
        else:
            if board[i]=="X":
                turtle.color("blue")
                if i < 3:
                    x_cor= (w/3)*i - w/2
                    y_cor= h/2
                elif 2< i <6:
                    x_cor= (w/3)*i - (w/2 * 3)
                    y_cor = h/6
                elif 5< i < 9:
                    x_cor= (w/3)*i - ((w/2) * 5)
                    y_cor = -(h/6)
            
                turtle.penup()
                turtle.goto(x_cor,y_cor)
                turtle.pendown()
                turtle.setheading(-angle)
                turtle.forward(hypo)
                turtle.penup()
                turtle.goto(x_cor,y_cor - (h/3))
                turtle.pendown()
                turtle.setheading(angle)
                turtle.forward(hypo)
                turtle.right(45)
        
    turtle.update()



def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    The current state of the board is given as
    a parameter, as well as the x,y screen coordinate
    indicating where the user clicked. This function
    should update the board state variable
    with an O in the corresponding position. Your
    code will need to translate the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool, indicating if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True.
    """

    print("user clicked at "+str(x)+","+str(y))
    # makes x_cor and y_cor into a range of 0 to 900 and floors to find 0-2 and turns into integers for it to multiply and add to find the cor for each box
    column = int((-y + h/2)//(h/3))
    row = int((x + w/2)//(w/3))
    box = (column * 3) + row
    
    if board[box] =='_':
        board[box] = "O" #when clicked on a blank space, "O" would show up
        boxes.pop(boxes.index(box)) #when box is chosen, that box, or position, is popped out, removing it from the choices that the player or computer can make
        return True
    else:
        return False
    

def check_game_over(board):
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemante, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """
    #This loop determines when there is a win and will display on the board whether the computer/Xs, player/Os, or no one win.  
    for win in lst:
        win_count = 0
        for box in range(1,len(win)):
            if not(board[win[box]] == "_"):
                if board[win[box]] == board[win[box - 1]]:
                    win_count +=1
        if win_count == 2 or boxes == []:
            winner= board[win[0]] + board[win[1]] + board[win[2]]
            turtle.home()
            if winner == "OOO":
                turtle.write("You Won!" , font=("Arial", 28, "normal"))
            elif winner=="XXX":
                turtle.write("You Lose!" , font=("Arial", 28, "normal"))
            else:
                turtle.write( "No Winner!" , font=("Arial", 28, "normal"))
            time.sleep(2)#when the game is over, there is a 2 second gap before the game resets
            
            #This loop resets the board by clearing and drawing the board again
            for box in range (len(board)):
                if not board[box] == "_":
                    board[box] = "_"
                            
                boxes.clear()
                for box in range(9):
                    boxes.append(box)
                    draw_board(board)
            return True
    return False

def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """
    computer_move = random.choice(boxes)
    #This loop determine if there two Xs or two Os and will select the option that will win as Xs or block the Os.
    
    for win in lst:#lst is a global, defined on top
        #The following if statement compares the first and second position in the lst of each possible win,
        #and if the third position is empty and if one of the first or second is not empty'
        if board[win[0]] == board[win[1]] and board[win[2]]=="_" and board[win[0]] != "_":
            if board[win[0]]=="X":#if the first position is "X" which means the second position is also "X",
                board[win[2]]="X"# then by placing a "X" in the third position, the game will be won by the computer
                boxes.pop(boxes.index(win[2]))
            elif board[win[0]]=="O":
                board[win[2]]="X"
                boxes.pop(boxes.index(win[2]))
            return board[win[2]] 
         
        if board[win[0]]== board[win[2]] and board[win[1]]=="_" and board[win[0]] != "_":
            if board[win[2]]=="X":
                board[win[1]]="X"
                boxes.pop(boxes.index(win[1]))
            elif board[win[2]]=="O":
                board[win[1]]="X"
                boxes.pop(boxes.index(win[1]))
            return board[win[1]]
                    
        if board[win[1]] == board[win[2]] and board[win[0]]=="_" and board[win[1]] != "_":
            if board[win[1]]=="X":
                board[win[0]]="X"
                boxes.pop(boxes.index(win[0]))
            elif board[win[1]]=="O":
                board[win[0]]="X"
                boxes.pop(boxes.index(win[0]))
            return board[win[0]]
           
        else:
            computer_move = random.choice(boxes)#if no one is about to win, the computer will randomly go to a position
   
    board[computer_move] = "X"
    boxes.pop(boxes.index(computer_move))


def clickhandler(x, y):
    """
    signature: int, int -> NoneType
    This function is called by turtle in response
    to a user click. The parameters are the screen
    coordinates indicating where the click happened.
    The function will call other functions. You do not
    need to modify this function, but you do need
    to understand it.
    """
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)

def main():
    """
    signature: () -> NoneType
    Runs the tic-tac-toe game. You shouldn't
    need to modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()

main()
