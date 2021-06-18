from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def submit():
    global root
    Password = entry_Password.get()
    username = entry_username.get()
    messageAlert = Label(root, width = 30)
    messageAlert.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)
    if Password != "1234":
        messageAlert.config(text = "Password incorrect")
        entry_username.delete
        entry_Password.delete
        entry_username.focus_set()    
    else:
        messageAlert.config(text = "Password accepted")
        print("Password accepted")
        messagebox.showinfo(title = "Password ok", message = "Good job you remembered your password")
        root.destroy()
        main()



def login():
    global password
    global entry_username
    global entry_Password
    global root
    #create window    
    root = Tk()
    root.geometry("270x240")
    root.title("Student Details")
    root.resizable (False, False)
    root.configure(background = "white")

    #place a frame to contain the form heading
    frame_heading = Frame(root)
    frame_heading.grid(row=0, column = 0, columnspan=2, padx=30, pady=5)

    #place a frame to contain labels and user entries
    frame_entry = Frame(root)
    frame_entry.grid(row=1, column=0, columnspan=2, padx=25, pady=10)

    #place a frame around the buttons
    frame_buttons = Frame(root)
    frame_buttons.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady = 10)

    #place labels and text entry for username
    Label(frame_entry, text = "Enter username:").grid(row = 0, column = 0, padx = 5, pady = 5)
    entry_username = Entry(frame_entry, width = 15, bg = "white")
    entry_username.grid(row = 0, column = 1, padx = 5, pady = 5)

    Label(frame_entry, text = "Enter Password:").grid(row = 1, column = 0, padx = 5, pady = 5)
    entry_Password = Entry(frame_entry, width = 15, bg = "white")
    entry_Password.grid(row = 1, column = 1, padx = 5, pady = 5)

    #for pass input show *    
    password = Entry(frame_entry, width = 15, bg = "white", show = '*')
    password.grid(row = 1, column = 1, padx = 5, pady = 5)

    #place submit button
    submit_button = Button(frame_buttons, text = "Submit", width = 8, command = submit )
    submit_button.grid(row = 0, column = 0, padx = 5, pady = 5 )

    #place quit button
    quit_button = Button(frame_buttons, text = "Quit", width = 15, command = quit )
    quit_button.grid(row = 0, column = 1, padx = 5, pady = 5 )
login()




def main():
    global root
    global button
    global frame_buttons
    global window
    #window
    window = Tk()
    window.geometry("500x500")
    window.title("Online School Clothing Store")
    window.resizable(False, False)
    window.configure(background = "White")        

    quit_button = Button(window, text = "Quit", width = 10, command = quit )
    quit_button.place(x = 400, y = 450)

    #place a frame to contain the form heading
    frame_heading = Frame(window)
    frame_heading.grid(row=0, column = 0, columnspan=2, padx=30, pady=5)

    #place a frame to contain labels and user entries 
    frame_entry = Frame(window)
    frame_entry.grid(row=1, column=0, columnspan=2, padx=25, pady=10)

    #place the form heading 
    Label(frame_heading,text="BTC Is Yummy", font=('Calibri', 16)).grid(row = 0, column = 00, padx = 0, pady = 5)  

    #where the image code would have gone
    canvas = Canvas(root, width = 50, height = 50)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("logo2.png"))  
    canvas.create_image(20, 20, anchor=NW, image=img)


root.mainloop()