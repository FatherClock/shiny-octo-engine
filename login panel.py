from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image





def shirt():
    shirt = open("items.txt", "r")
    shirt = open("items.txt", "a")
    shirt.write("1 Shirt Added To Cart.\n")
    shirt.close()


def pants():
    pants = open("items.txt", "r")
    pants = open("items.txt", "a")
    pants.write("1 Pair of Pants Added To Cart.\n")
    pants.close()    
    

def tie():
    tie = open("items.txt", "r")
    tie = open("items.txt", "a")
    tie.write("1 Tie Added To Cart.\n")
    tie.close()    


def shoe():
    shoe = open("items.txt", "r")
    shoe = open("items.txt", "a")
    shoe.write("1 Tie Added To Cart.\n")
    shoe.close() 

#commands for submit button
def submit():
    global window
    Password = entry_Password.get()
    username = entry_username.get()
    messageAlert = Label(root, width = 30)
    messageAlert.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)
    if Password != "1234":
        messageAlert.config(text = "Password incorrect")
        entry_username.delete(0, "END")
        entry_Password.delete(1, "END")
        entry_username.focus_set()

    else:
        messageAlert.config(text = "Password accepted")
        messagebox.showinfo(title = "Password Accepted", message = "Click OK to continue")
        root.destroy()
        main()


def signout():
    window.destroy()
    Login()
    
#display a message box with hint for password
def hint():
    messagebox.showinfo(title = "Password Hint", message = "Hint: Try Password 1234")

def Login():
    #global variables called throughout script
    global Password
    global entry_username
    global entry_Password
    global root
    #create Online Shop window
    root = Tk()
    root.geometry("250x180")
    root.title("Login Screen")
    root.resizable(False, False)
    root.configure(background = "white")

    #place a frame around labels and user entries
    frame_entry = Frame(root)
    frame_entry.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

    #place a frame around the buttons
    frame_buttons = Frame(root)
    frame_buttons.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady = 10)

    #place labels and text entry for username
    Label(frame_entry, text = "Enter username:").grid(row = 0, column = 0, padx = 5, pady = 5)
    entry_username = Entry(frame_entry, width = 15, bg = "white")
    entry_username.grid(row = 0, column = 1, padx = 5, pady = 5)

    #place labels and text entry for password ("*")
    Label(frame_entry, text = "Enter Password:").grid(row = 1, column = 0, padx = 10, pady = 10)
    entry_Password = Entry(frame_entry, width = 15, bg = "white", show = "*")
    entry_Password.grid(row = 1, column = 1, padx = 5, pady = 5)

    #place submit button
    submit_button = Button(frame_buttons, text = "Submit", width = 8, command = submit )
    submit_button.grid(row = 0, column = 0, padx = 5, pady = 5 )

    #place hint button
    hint_button = Button(frame_buttons, text = "Password hint", width = 15, command = hint )
    hint_button.grid(row = 0, column = 1, padx = 5, pady = 5 )
Login()

def signout():
    Login()
    window.destroy()



def main():
    global window
    global button
    global frame_buttons
    global teacher
    global student
    #create main window
    window = Tk()
    window.geometry("500x500")
    window.title("Shop")
    window.resizable(False, False)
    window.configure(background = "White")

    signout_button = Button(window, text = "Go Back", width = 10, command = signout )
    signout_button.place(x = 400, y = 450)

    #place a frame to contain the form heading
    frame_heading = Frame(window)
    frame_heading.grid(row=0, column = 0, columnspan=2, padx=30, pady=5)

    #place a frame to contain labels and user entries 
    frame_entry = Frame(window)
    frame_entry.grid(row=1, column=0, columnspan=2, padx=25, pady=10)

    #place the form heading 
    Label(frame_heading,text="Online Uniform Shop", font=('Calibri', 16)).grid(row = 0, column = 00, padx = 0, pady = 5)  

    #place buy button for each product
    shirt_button = Button(window, text = "Buy a Shirt", width = 12, command = shirt )
    shirt_button.place(x = 40, y = 200)

    pants_button = Button(window, text = "Buy Pants", width = 12, command = pants )
    pants_button.place(x = 325, y = 200)
    
    tie_button = Button(window, text = "Buy a Tie", width = 12, command = tie )
    tie_button.place(x = 325, y = 350)

    shoe_button = Button(window, text = "Buy some shoes", width = 12, command = shoe )
    shoe_button.place(x = 40, y = 350)

    #images











#run mainloop
root.mainloop()

