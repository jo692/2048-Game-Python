import random
#######################################################
count = 0
#######################################################
#####FUNCTIONS#####
#Move left function
def shift_left(row):
    count = 0
    row[:] = (x for x in row if x != 0)#remove 0s
    while count < len(row)-1:
        if row[count] == row[count + 1]:
            row[count] *= 2
            del row[count + 1]#2 merge into 1
        count += 1
    while len(row) < 4:
        row.append(0)
    return row

#Looped left function 
def left_looped(grid):
  count = 0
  for i in range(4):
    if all([x == 0 for x in grid[count]]):
      pass
    else:
      row = grid[count]
      shift_left(row)
      grid[count] = row
    count += 1
  return grid

#Move right function #fixed
def shift_rightv2(row):
    count = 0
    row[:] = (x for x in row if x != 0)
    while count < len(row)-1:
        if row[count] == row[count + 1]:
            row[count] *= 2
            del row[count + 1]
        count += 1
    while len(row) < 4:
        row.insert(0, 0)
    return row

#Looped right function 
def right_looped(grid):
    count = 0
    for i in range(4):
        if all([x == 0 for x in grid[count]]):
            pass
        else:
            row = grid[count]
            shift_rightv2(row)
            grid[count] = row
        count += 1
    return grid

#right shift without print for up shift
def right_looped_up(grid):
    count = 0
    for i in range(4):
        if all([x == 0 for x in grid[count]]):
            pass
        else:
            row = grid[count]
            shift_rightv2(row)
            grid[count] = row
        count += 1
    return grid

#shift up function
def shift_up(grid):
    count = 0
    count2 = 0
    countx = 3
    cw_grid = [[] for i in range(4)] #rotate clockwise
    for i in range(4):
        cw_grid[count] = [x[count] for x in grid] 
        cw_grid[count].reverse()
        count += 1
    grid = cw_grid
    right_looped_up(grid) #shift right
    acw_grid = [[] for i in range(4)] #anticlockwise
    for i in range(4):
        acw_grid[count2] = [y[countx] for y in grid]
        count2 += 1
        countx -= 1
    grid = acw_grid
    return grid
	
#######grid = shift_up(grid)########
#left shift without print for down
def left_looped_down(grid):
  count = 0
  count_str = 0
  for i in range(4):
    if all([x == 0 for x in grid[count]]):
      pass
    else:
      row = grid[count]
      shift_left(row)
      grid[count] = row
    count += 1
  return grid

#shift down function
def shift_down(grid):
    count = 0
    count2 = 0
    countx = 3
    cw_grid = [[] for i in range(4)] #rotate clockwise
    for i in range(4):
        cw_grid[count] = [x[count] for x in grid]
        cw_grid[count].reverse()
        count += 1
    grid = cw_grid
    left_looped_down(grid) #shift left
    acw_grid = [[] for i in range(4)] #rotate anticlockwise
    for i in range(4):
        acw_grid[count2] = [y[countx] for y in grid]
        count2 += 1
        countx -= 1
    grid = acw_grid
    return grid
	
#####grid = shift_down(grid)#####
#print grid without brackets and commas
def print_grid(grid):
    c = 0
    for i in range(4):
        grid_row = grid[c]
        grid_line = '{:>4}  {:>4}  {:>4}  {:>4}'.format(grid_row[0],grid_row[1], grid_row[2], grid_row[3]) #space out and align the numbers 
        print(grid_line)
        c += 1

#assigns a 2 or 4 to a random zero cell 
def new_cell(grid):
    chance = random.randint(0,2)
    if chance == 0:
        new_value = 4
    elif chance > 0:
        new_value = 2
    index = []
    for a, range in enumerate(grid): #find an empty cell
        for b, x in enumerate(range):
            if x == 0:
                index.append((a, b))#list all empty cells
    size = len(index)-1
    rand = random.randint(0, size)
    selected = index[rand]
    row = selected[0]
    cell = selected[1]
    grid[row][cell] = new_value
    return grid
	
#Check for pairs, used in gameover function
def pairs_horizontal(grid):
    count = 0
    pairs = []
    pair = 0
    for i in range (4):
        row = grid[count]
        count2 = 0
        for i in range(3):
            if row[count2] == row[count2 + 1]:
                pairs.append(1)
            count2 += 1
        count += 1
    if len(pairs) != 0:
        pair = 1
    else:
        pass
    return pair

def pairs_vertical(grid):
    count = 0
    pairs = []
    pair2 = 0
    cw_grid = [[] for i in range(4)]
    for i in range(4):
        cw_grid[count] = [x[count] for x in grid] 
        cw_grid[count].reverse()
        count += 1
    count = 0
    for i in range(4):
        row = cw_grid[count]
        count2 = 0
        for i in range(3):
            if row[count2] == row[count2 + 1]:
                pairs.append(1)
            count2 += 1
        count += 1
    if len(pairs) != 0:
        pair2 = 1
    else:
        pass
    return pair2

#Check if the game is over. fixed
def gameover(grid):
    zeros = []
    pair = pairs_horizontal(grid)
    pair2 = pairs_vertical(grid)
    for a, range in enumerate(grid):
        for b, x in enumerate(range): #find any remaining 0s
            if x == 0:
                zeros.append((a, b))
    spaces = len(zeros)
    if spaces == 0:
        pairs_horizontal(grid)
        if pair == 0:
            pairs_vertical(grid)
            if pair2 == 0:
                print("Game Over, no possible moves")
            else:
                pass
        else:
            pass
    else:
        pass

#Check if 2048 is present and print
def victory(grid):
    count = 0
    for i in range(4):
        row = grid[count]
        if 2048 in row:
            print("You Win!")
            break
        count += 1    
     
#######################################################
#Empty 4x4 grid
grid = [[] for i in range(4)]
for i in range(4):
    for i in range(4):
        grid[count].append(0)
    count += 1
#place 2 or 4 in 2 random cells
for i in range(2):
    new_cell(grid)

#print the grid without commas or brackets
print_grid(grid)

#Ask user which direction to move
while True:
    choice = input("Which direction to shift? (wasd, 1 to exit) ")
    if choice == "a":
        left_looped(grid)
        new_cell(grid)
        print_grid(grid)
        victory(grid)
        gameover(grid)
    if choice == "d":
        right_looped(grid)
        new_cell(grid)
        print_grid(grid)
        victory(grid)
        gameover(grid)
    if choice == "w":
        grid = shift_up(grid) #need to call or grid wont return
        shift_up(grid)
        new_cell(grid)
        print_grid(grid)
        victory(grid)
        gameover(grid)
    if choice == "s":
        grid = shift_down(grid)
        shift_down(grid)
        new_cell(grid)
        print_grid(grid)
        victory(grid)
        gameover(grid)
    if choice == "1":
        break
