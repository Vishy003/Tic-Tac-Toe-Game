from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Vishakha's Tic Tac Toe")

# X starts so True
clicked = True
count = 0

# Disable all buttons
def disable_all_buttons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)

# Check to see if someone won
def checkifwon():
    global winner
    winner = False

    # ------- Case 1: Checking if X wins -------
        
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg = "teal")
        b2.config(bg = "teal")
        b3.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X Wins")
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg = "teal")
        b5.config(bg = "teal")
        b6.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg = "teal")
        b8.config(bg = "teal")
        b9.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg = "teal")
        b4.config(bg = "teal")
        b7.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg = "teal")
        b5.config(bg = "teal")
        b8.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg = "teal")
        b6.config(bg = "teal")
        b9.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg = "teal")
        b5.config(bg = "teal")
        b9.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg = "teal")
        b5.config(bg = "teal")
        b7.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins")
        disable_all_buttons()

    # ------- Case 2: Checking if 0 Wins -------

    elif b1["text"] == "0" and b2["text"] == "0" and b3["text"] == "0":
        b1.config(bg = "teal")
        b2.config(bg = "teal")
        b3.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! 0 Wins")
        disable_all_buttons()

    elif b4["text"] == "0" and b5["text"] == "0" and b6["text"] == "0":
        b4.config(bg = "teal")
        b5.config(bg = "teal")
        b6.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! 0 Wins")
        disable_all_buttons()

    elif b7["text"] == "0" and b8["text"] == "0" and b9["text"] == "0":
        b7.config(bg = "teal")
        b8.config(bg = "teal")
        b9.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! 0 Wins")
        disable_all_buttons()

    elif b1["text"] == "0" and b4["text"] == "0" and b7["text"] == "0":
        b1.config(bg = "teal")
        b4.config(bg = "teal")
        b7.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! 0 Wins")
        disable_all_buttons()

    elif b2["text"] == "0" and b5["text"] == "0" and b8["text"] == "0":
        b2.config(bg = "teal")
        b5.config(bg = "teal")
        b8.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! 0 Wins")
        disable_all_buttons()

    elif b3["text"] == "0" and b6["text"] == "0" and b9["text"] == "0":
        b3.config(bg = "teal")
        b6.config(bg = "teal")
        b9.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! 0 Wins")
        disable_all_buttons()

    elif b1["text"] == "0" and b5["text"] == "0" and b9["text"] == "0":
        b1.config(bg = "teal")
        b5.config(bg = "teal")
        b9.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! 0 Wins")
        disable_all_buttons()

    elif b3["text"] == "0" and b5["text"] == "0" and b7["text"] == "0":
        b3.config(bg = "teal")
        b5.config(bg = "teal")
        b7.config(bg = "teal")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! 0 Wins")
        disable_all_buttons()

    # ------- Case 3: Checking if there's a Tie -------
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!\nNo One Wins")
        disable_all_buttons()

# Button Clicked Function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "0"
        clicked = True
        count += 1
        checkifwon()
        
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box...")

# Start the game over!
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    # Building the buttons
    b1 = Button(root, text = " ", font = "Helvetica", height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b1))
    b2 = Button(root, text = " ", font = "Helvetica", height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b2))
    b3 = Button(root, text = " ", font = "Helvetica", height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b3))

    b4 = Button(root, text = " ", font = "Helvetica", height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b4))
    b5 = Button(root, text = " ", font = "Helvetica", height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b5))
    b6 = Button(root, text = " ", font = "Helvetica", height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b6))

    b7 = Button(root, text = " ", font = "Helvetica", height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b7))
    b8 = Button(root, text = " ", font = "Helvetica", height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b8))
    b9 = Button(root, text = " ", font = "Helvetica", height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b9))

    # Grid our buttons to screen
    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)

    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)

    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)

# Creating a Menu
my_menu = Menu(root)
root.config(menu = my_menu)

# Creating Options Menu
options_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Options", menu = options_menu)
options_menu.add_command(label = "Reset Game", command = reset)

reset()
