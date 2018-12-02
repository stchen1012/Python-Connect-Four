import turtle

myTurtle = turtle.Turtle('turtle')
myTurtle.speed(0)
tTurtle = turtle.Turtle()
winTurtle = turtle.Turtle()
winTurtle.hideturtle()
#grid = y,x - applicable for all Python matrices

print("Let's play Connect Four!")
player_one_name = input("Player One - what is your name? ")
player_two_name = input("Player Two - what is your name? ")

row_1 = [0,0,0,0,0,0,0]
row_2 = [0,0,0,0,0,0,0]
row_3 = [0,0,0,0,0,0,0]
row_4 = [0,0,0,0,0,0,0]
row_5 = [0,0,0,0,0,0,0]
row_6 = [0,0,0,0,0,0,0]

grid = [row_1,row_2,row_3,row_4,row_5,row_6]

def print_grid():
    print("")
    for row in grid:
        print(row)
    print("")

def player_one_drop():
    global player_coordinates
    global game_over
    if game_over == True:
        return 0
    #player_one_inpt = int(input(player_one_name + " select the column you would like to drop your piece: "))
    for row in range(5,-1,-1):
        if grid[row][player_one_inpt - 1] == 0:
            grid[row][player_one_inpt - 1] = 1
            player_coordinates = [row,player_one_inpt - 1]
            #print(player_coordinates)
            break
    print_grid()
     
def player_two_drop():
    global player_coordinates
    global game_over
    if game_over == True:
        return 0
    #player_two_inpt = int(input(player_two_name + " select the column you would like to drop your piece: "))
    for row in range(5,-1,-1):
        if grid[row][player_two_inpt - 1] == 0:
            grid[row][player_two_inpt - 1] = 2
            player_coordinates = [row,player_two_inpt - 1]
            break
    print_grid()

def win_graphics_pone():
    winTurtle.penup()
    winTurtle.setposition(-250,250)
    winTurtle.pendown()
    winTurtle.write(player_one_name + " wins!", font=("Cambria", 24, "bold"))

def win_graphics_ptwo():
    winTurtle.penup()
    winTurtle.setposition(-250,250)
    winTurtle.pendown()
    winTurtle.write(player_two_name + " wins!", font=("Cambria", 24, "bold"))

def check_vertical(x): #x will be player input
    global game_over
    if game_over == True:
        return 0
    y = [] #this list will be used as the comparator
    for row in range(5,-1,-1):
         if grid[row][x] != 0:
             y.append(grid[row][x])
             if y[-4:] == [1,1,1,1]:
                 print(player_one_name + " wins!")
                 win_graphics_pone()
                 game_over = True
                 break
             elif y[-4:] == [2,2,2,2]:
                 print(player_two_name + " wins!")
                 win_graphics_ptwo()
                 game_over = True
                 break

def check_horizontal(x): #x will be player input
    global game_over
    if game_over == True:
        return 0
    global player_coordinates
    y = [] #this list will be used as the comparator
    for item in grid[player_coordinates[0]]:
        #print("test" + str(grid[player_coordinates[0]]))
        y.append(item)
        if y[-4:] == [1,1,1,1]:
            print(player_one_name + " wins!")
            win_graphics_pone()
            game_over = True
            break
        elif y[-4:] == [2,2,2,2]:
            print(player_two_name + " wins!")
            win_graphics_ptwo()
            game_over = True
            break


def check_diagonal(): 
    #Check downward angle diag for rows 0-3 and starting at column 0
    global game_over
    for loops in range(1): #keep this for loop
        for row in range(3):
            winnerlist = []
            j = row
            i = 0
            while i<=6 and j<=5:
                winnerlist.append(grid[j][i])
                if winnerlist[-4:] == [1,1,1,1]:
                    print(player_one_name + " wins!")
                    win_graphics_pone()
                    game_over = True
                    return 0
                if winnerlist[-4:] == [2,2,2,2]:
                    print(player_two_name + " wins!")
                    win_graphics_ptwo()
                    game_over = True
                    return 0
                else:
                    i+=1
                    j+=1
                
        for column in range(4):
            winnerlist = []
            j = 0
            i = column
            while i<=6 and j<=5:
                winnerlist.append(grid[j][i])
                if winnerlist[-4:] == [1,1,1,1]:
                    print(player_one_name +" wins!")
                    win_graphics_pone()
                    game_over = True
                    return 0
                if winnerlist[-4:] == [2,2,2,2]:
                    print(player_two_name + " wins!")
                    winTurtle.penup()
                    winTurtle.setposition(-290,250)
                    winTurtle.pendown()
                    winTurtle.write(player_two_name + " wins!", font=("Arial", 24, "bold"))
                    game_over = True
                    return 0
                else:
                    i+=1
                    j+=1


        for row in range(3):
            winnerlist = []
            j = row
            i = 6
            while i>=0 and j<=5:
                winnerlist.append(grid[j][i])
                if winnerlist[-4:] == [1,1,1,1]:
                    print(player_one_name +" wins!")
                    win_graphics_pone()
                    print(winnerlist)
                    game_over = True
                    return 0
                if winnerlist[-4:] == [2,2,2,2]:
                    print(player_two_name + " wins!")
                    win_graphics_ptwo()
                    game_over = True
                    return 0
                else:
                    i-=1
                    j+=1

        for column in range(6,2,-1):
            winnerlist = []
            j = 0
            i = column
            while i>=0 and j<=5:
                winnerlist.append(grid[j][i])
                if winnerlist[-4:] == [1,1,1,1]:
                    print(player_one_name + " wins!")
                    win_graphics_pone()
                    game_over = True
                    return 0
                if winnerlist[-4:] == [2,2,2,2]:
                    print(player_two_name + " wins!")
                    win_graphics_ptwo()
                    game_over = True
                    return 0
                else:
                    i-=1
                    j+=1


turtle.setup(600,600)
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Let's Play Connect Four!")
tTurtle.penup()
tTurtle.color("darkgreen")
tTurtle.fillcolor("darkgreen")
tTurtle.setposition(-250,230)
tTurtle.begin_fill()
tTurtle.pendown()
tTurtle.forward(470)
tTurtle.right(90)
tTurtle.forward(410)
tTurtle.right(90)
tTurtle.forward(470)
tTurtle.right(90)
tTurtle.forward(410)
tTurtle.end_fill()

def drawGameBoard():
    for row in range(0,6):
        y = 155 + row * -65
        for column in range(6,-1,-1):
            x = -210 + column * 65
            myTurtle.penup()
            myTurtle.setposition(x,y)
            myTurtle.pendown()
            myTurtle.begin_fill()
            if grid[row][column] == 1:
                myTurtle.fillcolor('red')
            elif grid[row][column] == 2:
                myTurtle.fillcolor('yellow')
            else:
                myTurtle.fillcolor('white')
            myTurtle.circle(30)
            myTurtle.end_fill()

def updateBoard():
    row = player_coordinates[0]
    column = player_coordinates[1]
    x = -210 + player_coordinates[1]*65
    y = 155 + player_coordinates[0] * -65
    myTurtle.penup()
    myTurtle.setposition(x,y)
    myTurtle.pendown()
    myTurtle.begin_fill()
    if grid[row][column] == 1:
        myTurtle.fillcolor('red')
    elif grid[row][column] == 2:
        myTurtle.fillcolor('yellow')
    else:
        myTurtle.fillcolor('white')
    myTurtle.circle(30)
    myTurtle.end_fill()


def inputNumber(name):
  while True:
    try:
       userInput = int(input(name + ", which column(1-7) you would like to drop your piece: "))
    except ValueError:
       print("Not an integer! Try again")
       continue
    if userInput not in range(1, 8):
        print("Error: Please only enter numbers between 1-7")
    else:
        return userInput
        break

game_over = False

drawGameBoard()


while game_over != True:
    player_coordinates = [0,0]
    #player_one_inpt = int(input(player_one_name + ", which column(1-7) you would like to drop your piece: "))
    player_one_inpt = inputNumber(player_one_name)
    player_one_drop()
    updateBoard()
    #print("player Coordinate: " + str(player_coordinates))
    check_vertical(player_one_inpt - 1)
    check_horizontal(player_one_inpt - 1)
    check_diagonal()
    if game_over != True:
        #player_two_inpt = int(input(player_two_name + ", which column(1-7) you would like to drop your piece: "))
        player_two_inpt = inputNumber(player_two_name)
        player_two_drop()
        updateBoard()
        check_vertical(player_two_inpt - 1)
        check_horizontal(player_two_inpt - 1)
        check_diagonal()

turtle.exitonclick()

#put first name and last name in project name for submission
#email code and screenshot of output

