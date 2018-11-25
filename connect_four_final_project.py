player_one_name = input("Player one - what is your name? ")
player_two_name = input("Player two - what is your name? ")

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

player_one_inpt = int(input(player_one_name + " select the column you would like to drop your piece: "))

def player_one_drop(columnselected):
    if columnselected == 1:
        if row_6[0] == 0:
            row_6[0] = 1
    elif columnselected == 2:
        if row_6[1] == 0:
            row_6[1] = 1
    elif columnselected == 3:
        if row_6[2] == 0:
            row_6[2] = 1
    elif columnselected == 4:
        if row_6[3] == 0:
            row_6[3] = 1
    elif columnselected == 5:
        if row_6[4] == 0:
            row_6[4] = 1
    elif columnselected == 6:
        if row_6[5] == 0:
            row_6[5] = 1
    else:
        print("Select a number 1-6")
    print_grid()

player_one_drop(player_one_inpt)

player_two_input = int(input(player_two_name + " select the column you would like to drop your piece: "))

def player_two_drop(columnselected):
    if columnselected == 1:
        #if row_6[0] == 0:
        #   row_6[0] = 1
        coin_slot_row = 5
        while coin_slot_row >= 0:
            if grid[coin_slot_row][columnselected-1] == 0:
                grid[coin_slot_row][columnselected-1] = 1
                break
            else:
                coin_slot_row = coin_slot_row -1
        coin_slot_row = 5
        
    elif columnselected == 2:
        if row_6[1] == 0:
            row_6[1] = 1
    elif columnselected == 3:
        if row_6[2] == 0:
            row_6[2] = 1
    elif columnselected == 4:
        if row_6[3] == 0:
            row_6[3] = 1
    elif columnselected == 5:
        if row_6[4] == 0:
            row_6[4] = 1
    elif columnselected == 6:
        if row_6[5] == 0:
            row_6[5] = 1    
    print_grid()


player_two_drop(player_two_input)
