import tkinter as tk

def initialise():
    print("-"*30)
    for i in range(3):
        for j in range(3):
            BUTTONS[i][j].config(text="")

def determine_turn():
    grid = give_grid().replace("e","")
    return len(grid)%2

def handle_click(row,column):
    square = BUTTONS[row][column]

    if not valid_click(square) or game_is_finished():
        return
    
    turn = determine_turn()
    if turn == 0:
        square.config(text="X")
    if turn == 1:
        square.config(text="O")

    if game_is_won():
        print("Well done, player "+winner()+" wins!")

    if game_is_draw():
        print("The game is a draw.")

    if game_is_finished():
        decision = input("Would you like to play again? (y/n)").lower()
        if decision == "y":
            initialise()
        else:
            root.destroy()

def valid_click(square):
    if len(square.cget("text")) == 0:
        return True
    return False

def give_grid():
    totaltext = ''
    for i in range(3):
        for j in range(3):
            value = BUTTONS[i][j].cget("text")
            if value == '':
                value = 'e' #e = empty
            totaltext += value
    return totaltext

def check_all_win_cases():
    cases = give_columns() + give_diagonals() + give_rows()
    for case in cases:
        if is_win(case):
            return True, case[0]
    return False, None

def game_is_draw():
    if len(give_grid().replace("e","")) == 9 and not game_is_won():
        return True
    return False

def game_is_won():
    return check_all_win_cases()[0]

def game_is_finished():
    return game_is_draw() or game_is_won()

def winner():
    return check_all_win_cases()[1]

def is_win(three):
    if three == "XXX" or three == "OOO":
        return True
    return False

def give_rows():
    grid = give_grid()
    return [grid[0:3],grid[3:6],grid[6:9]]

def give_columns():
    grid = give_grid()
    cols = []
    for a in range(3):
        column = ''
        for b in range(3):
            column += grid[3*b + a]
        cols.append(column)
    return cols

def give_diagonals():
    grid = give_grid()
    diags = []
    diags.append(grid[0]+grid[4]+grid[8])
    diags.append(grid[6]+grid[4]+grid[2])
    return diags


#Grid 
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("500x400")

BUTTONS = []
for i in range(3):
    root.grid_rowconfigure(i, weight=1, uniform="row")
    root.grid_columnconfigure(i, weight=1, uniform="col")

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(root, command=lambda r=i, c=j: handle_click(r, c), font = ("Arial",40))
        btn.grid(row=i,column=j,sticky="nsew")
        row.append(btn)
    BUTTONS.append(row)


root.mainloop()

