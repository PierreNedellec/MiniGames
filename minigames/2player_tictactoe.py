import tkinter as tk
from tkinter import messagebox

def initialise():
    for i in range(3):
        for j in range(3):
            BUTTONS[i][j].config(text="")
            BUTTONS[i][j].config(state="normal")
    SHOWTURN.config(text="Player X's turn", font=("Arial",20))

def determine_turn():
    grid = give_grid().replace("e","")
    if len(grid)%2 == 0:
        return "X"
    if len(grid)%2 == 1:
        return "O"

def show_turn_on_grid():
    print("called")
    SHOWTURN.config(text=f"Player {determine_turn()}'s turn")

def handle_click(row,column):
    square = BUTTONS[row][column]
    
    turn = determine_turn()
    square.config(text=turn)
    square.config(state = "disabled")
    show_turn_on_grid()

    won = game_is_won()
    drawn = game_is_draw()
    if won or drawn:
        if won:
            message = "Well done, player "+winner()+" wins!"
        else:
            message = "The game is a draw."
        disable_all_buttons()
        SHOWTURN.config(text= message, font=("Arial",20,"bold"))
        playagain = messagebox.askyesno(None, "Play again?")
        if playagain:
            initialise()
        else:
            root.destroy()

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
    grid = give_grid()
    cases = []
    squares = ["012","345","678","147","258","036","048","246"]
    for s in squares:
        case = ""
        for index in s:
            case += grid[int(index)]
        if is_win(case):
            return True, case[0]
    return False, None

def game_is_draw():
    len(give_grid().replace("e","")) == 9 and not game_is_won()

def game_is_won():
    return check_all_win_cases()[0]

def winner():
    return check_all_win_cases()[1]

def is_win(three):
    return three in ["XXX","OOO"]

def disable_all_buttons():
    for i in range(3):
        for j in range(3):
            BUTTONS[i][j].config(state = "disabled")

#Grid 
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("500x500")

for i in range(4):
    root.grid_rowconfigure(i, weight=1, uniform="row")
for j in range(3):
    root.grid_columnconfigure(j, weight=1, uniform="col")

header = tk.Label(root, text="Tic Tac Toe", font=("Arial", 30))
header.grid(row=0,column=0,columnspan=3)
SHOWTURN = tk.Label(root, text="Player X's turn", font=("Arial",20))
SHOWTURN.grid(row=4,column=0, columnspan=3)

BUTTONS = []
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(root, command=lambda r=i, c=j: handle_click(r, c), font = ("Arial",40))
        btn.grid(row=i+1,column=j,sticky="nsew")
        row.append(btn)
    BUTTONS.append(row)


root.mainloop()

