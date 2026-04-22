import tkinter as tk

def initialise():
    print("-"*30)
    for i in range(3):
        for j in range(3):
            BUTTONS[i][j].config(text="")
            BUTTONS[i][j].config(state="normal")

def determine_turn():
    grid = give_grid().replace("e","")
    return len(grid)%2

def handle_click(row,column):
    square = BUTTONS[row][column]
    
    turn = determine_turn()
    if turn == 0:
        square.config(text="X")
        square.config(state="disabled")
    if turn == 1:
        square.config(text="O")
        square.config(state="disabled")

    if game_is_won():
        print("Well done, player "+winner()+" wins!")

    if game_is_draw():
        print("The game is a draw.")

    if game_is_finished():
        disable_all_buttons()
        decision = input("Would you like to play again? (y/n)").lower()
        if decision == "y":
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

def game_is_finished():
    return game_is_draw() or game_is_won()

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

