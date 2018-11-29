#I believe this is to a good point.  It works for one..lol. It contains a list, a class, a GUI, and a conditional.
#All we need is a loop, but we talked about doing that by asking if they want to create another card.
#I tried to comment it well for you guys, let me know if I missed something.

from tkinter import *


class Ecard:
    def __init__(self):
        # List of available occasions
        choices = ["Christmas", "Birthday", "Anniversary", "Valentines Day", "Congratulations"]

        # Create window, add title, and set size
        window = Tk()
        window.title("E-card Generator")
        window.geometry('280x100')

        Label(window, text="Choose an Occasion from Menu").place(x=55, y=5)

        self.selection = StringVar(window)  # Variable to hold selected occasion from menu
        self.selection.set(choices[0])  # Set default menu selection

        # Create menu and populate with "choices" list items
        occasions = OptionMenu(window, self.selection, *choices).place(x=90, y=30)

        button = Button(window, text="OK", command=self.getSelection).place(x=125, y=65)

        mainloop()

        # Images must be initialized in 'init' to be called in functions
        ##self.testPhoto = PhotoImage(file = 'Test.gif')  # Placeholder for image files (can be GIF and PGM/PPM)

    #This function gets the selection from the menu and calls the appropriate function for each occasion
    def getSelection(self):
        choice = self.selection.get()
        if choice == "Christmas":
            self.christmas()
        elif choice == "Valentines Day":
            self.valentines()
        elif choice == "Birthday":
            self.birthday()
        elif choice == "Anniversary":
            self.anniversary()
        elif choice == "Congratulations":
            self.congratulations()

    #These are the functions to hold what we want to happen when an occasion is selected.  For now I have just put a print
    #statment in each one to show that they return when selected and called. It will be the same code with
    #minor adjustments for naming of each occasion.  We could upload all images and then let the program randomly
    #select one or we could have it display a canvas with however many options we decide and let them select.  Once we get
    #one written it shoud just be copy, paste, and adjust names.  This is where we could use the code for the canvas that
    #Zakary has written.
    def christmas(self):
        print("Its Christmas")

    def valentines(self):
        print("Its Valentines Day")

    def birthday(self):
        print("Its Your Birthday")

    def congratulations(self):
        print("Congrats!")

    def anniversary(self):
        print("Happy Anniversary")


Ecard()
