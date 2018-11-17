from tkinter import *

#List of available occasions
choices = ["Christmas", "Birthday", "Anniversary", "Valentines Day", "Congratulations"]

#Create window, add title, and set size
window = Tk()
window.title("E-card Generator")
window.geometry('280x100')

Label(window, text="Choose an Occasion from Menu").place(x=55, y=5)

selection = StringVar(window)     #Variable to hold selected occasion from menu
selection.set(choices[0])     #Set default menu selection

#Create menu and populate with "choices" list items
occasions = OptionMenu(window, selection, *choices).place(x=90, y=30)

#Function to get selected occasion(It just prints now so I knew it returned correctly, we would assign it to a variable later)
def getSelection():
    print("Occasion is:" + selection.get())


button = Button(window, text="OK", command=getSelection).place(x=125, y=65)


mainloop()

