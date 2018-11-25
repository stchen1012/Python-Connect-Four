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
    #player_two_inpt = int(input(player_two_name + " select the column you would like to drop your piece: "))
    for row in range(5,-1,-1):
        if grid[row][player_two_inpt - 1] == 0:
            grid[row][player_two_inpt - 1] = 2
            player_coordinates = [row,player_two_inpt - 1]
            break
    print_grid()


def check_vertical(x): #x will be player input
    y = [] #this list will be used as the comparator
    for row in range(5,-1,-1):
         if grid[row][x] != 0:
             y.append(grid[row][x])
             #print(y)
             if y[-4:] == [1,1,1,1]:
                 print(player_one_name + "wins!")
             elif y[-4:] == [2,2,2,2]:
                 print(player_two_name + "wins!")

def check_horizontal(x): #x will be player input
    global player_coordinates
    y = [] #this list will be used as the comparator
    for item in grid[player_coordinates[0]]:
        #print("test" + str(grid[player_coordinates[0]]))
        y.append(item)
        #print(y)
        if y[-4:] == [1,1,1,1]:
            print(player_one_name + " wins!")
        elif y[-4:] == [2,2,2,2]:
            print(player_two_name + " wins!")
    

while True:
    player_coordinates = [0,0]
    player_one_inpt = int(input(player_one_name + " select the column you would like to drop your piece: "))
    player_one_drop()
    check_vertical(player_one_inpt - 1)
    check_horizontal(player_one_inpt - 1)
    player_two_inpt = int(input(player_two_name + " select the column you would like to drop your piece: "))
    player_two_drop()
    check_vertical(player_two_inpt - 1)
    check_horizontal(player_two_inpt - 1)
    


    
#type out 3 if statments - check for positions i+1 , etc
#graphics if you're feeling real fancy
