"""
Program: E-card Generator
Names: Zakary Anderson, Matt Burns, James Reardon
Description: This program will generate an E-card for the user.  It will first let the user select an occasion from a
drop down menu.  Then once the occasion is selected, the program will generate a canvas randomly filled with one of
three available images for each occasion.  The user will then have the option to name and save the generated image as
a .pdf file for later use.
"""

from tkinter import *
from random import *
from shutil import *
import os


#Create class
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


        # Set image variables
        self.Christmas1 = './gif images/Christmas.gif'
        self.Christmas2 = './gif images/Christmas2.gif'
        self.Christmas3 = './gif images/Christmas3.gif'
        self.Valentines1 = './gif images/Valentines.gif'
        self.Valentines2 = './gif images/Valentines2.gif'
        self.Valentines3 = './gif images/Valentines3.gif'
        self.Birthday1 = './gif images/Birthday.gif'
        self.Birthday2 = './gif images/Birthday2.gif'
        self.Birthday3 = './gif images/Birthday3.gif'
        self.Congratulations1 = './gif images/Congratulations.gif'
        self.Congratulations2 = './gif images/Congratulations2.gif'
        self.Congratulations3 = './gif images/Congratulations3.gif'
        self.Anniversary1 = './gif images/Anniversary.gif'
        self.Anniversary2 = './gif images/Anniversary2.gif'
        self.Anniversary3 = './gif images/Anniversary3.gif'

        self.move_files()

        mainloop()


    #Function to get the selection from the menu and call the appropriate function for each occasion
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

    # Move Generated .gif files to Generated_Gifs directory
    def move_files(self):
        for file in os.listdir("./"):
            if file.endswith(".pdf"):
                print("Moving file: " + os.path.join("./", file))
                move(file, './Generated_PDFs/')

    # Get Save Name from Entry Field
    def file_name(self):
        self.input = self.saveName.get()
        return self.input

    def file_save(self, x):
        print(x, self.file_name())
        copyfile(x, './'+self.file_name()+'.pdf')
        self.eCard.destroy()
        self.move_files()

    # Function for Christmas occasion
    def christmas(self):
        self.eCard = Toplevel()  # Create window
        self.eCard.title("E-Card Generator") # Window title
        choice = randint(1,3) # Random variable between 1 and 3 to choose which image is displayed
        imageChoice = '' # Image choice variable

        # Set canvas
        self.canvas = Canvas(self.eCard, width = 592, height = 420)
        self.canvas.pack()

        # Set Frame
        frame = Frame(self.eCard)
        frame.pack()

        # If statement to check the random choice to display image
        if choice == 1:
            imageChoice = self.Christmas1
        elif choice == 2:
            imageChoice = self.Christmas2
        elif choice == 3:
            imageChoice = self.Christmas3

        self.ecardImage = PhotoImage(file = imageChoice) # initializing image
        self.canvas.create_image(0, 0, image = self.ecardImage, anchor = NW) # display image

        # Save Name Label
        label = Label(frame, text="Save file as: ")
        label.grid(column=2, row=0)
        # Save Name Entry Field
        self.saveName = Entry(frame)
        self.saveName.grid(column=3, row=0)
        # Save Button
        saveButton = Button(frame, text="Save", command=lambda : self.file_save(imageChoice))
        saveButton.grid(column=4, row=0)

    # Function for Valentines Day occasion
    def valentines(self):
        self.eCard = Toplevel()  # Create window
        self.eCard.title("E-Card Generator") # Window title
        choice = randint(1,3) # Random variable between 1 and 3 to choose which image is displayed

        # Set canvas
        self.canvas = Canvas(self.eCard, width = 592, height = 420)
        self.canvas.pack()

        # Set Frame
        frame = Frame(self.eCard)
        frame.pack()

        imageChoice = ''

        # If statement to check the random choice to display image
        if choice == 1:
            imageChoice = self.Valentines1
        elif choice == 2:
            imageChoice = self.Valentines2
        elif choice == 3:
            imageChoice = self.Valentines3

        self.ecardImage = PhotoImage(file = imageChoice) # initializing image
        self.canvas.create_image(0, 0, image = self.ecardImage, anchor = NW) # display image

        # Save Name Label
        label = Label(frame, text="Save file as: ")
        label.grid(column=2, row=0)
        # Save Name Entry Field
        self.saveName = Entry(frame)
        self.saveName.grid(column=3, row=0)
        # Save Button
        saveButton = Button(frame, text="Save", command=lambda : self.file_save(imageChoice))
        saveButton.grid(column=4, row=0)

    # Function for Birthday occasion
    def birthday(self):
        self.eCard = Toplevel()  # Create window
        self.eCard.title("E-Card Generator")  # Window title
        choice = randint(1,3) # Random variable between 1 and 3 to choose which image is displayed

        # Set canvas
        self.canvas = Canvas(self.eCard, width = 592, height = 420)
        self.canvas.pack()

        # Set Frame
        frame = Frame(self.eCard)
        frame.pack()

        imageChoice = ''

        # If statement to check the random choice to display image
        if choice == 1:
            imageChoice = self.Birthday1
        elif choice == 2:
            imageChoice = self.Birthday2
        elif choice == 3:
            imageChoice = self.Birthday3

        self.ecardImage = PhotoImage(file = imageChoice) # initializing image
        self.canvas.create_image(0, 0, image = self.ecardImage, anchor = NW) # display image

        # Save Name Label
        label = Label(frame, text="Save file as: ")
        label.grid(column=2, row=0)
        # Save Name Entry Field
        self.saveName = Entry(frame)
        self.saveName.grid(column=3, row=0)
        # Save Button
        saveButton = Button(frame, text="Save", command=lambda : self.file_save(imageChoice))
        saveButton.grid(column=4, row=0)

    # Function for Congratulations occasion
    def congratulations(self):
        self.eCard = Toplevel()  # Create window
        self.eCard.title("E-Card Generator")  # Window title
        choice = randint(1,3) # Random variable between 1 and 3 to choose which image is displayed

        # Set canvas
        self.canvas = Canvas(self.eCard, width = 592, height = 420)
        self.canvas.pack()

        # Set Frame
        frame = Frame(self.eCard)
        frame.pack()

        imageChoice = ''

        # If statement to check the random choice to display image
        if choice == 1:
            imageChoice = self.Congratulations1
        elif choice == 2:
            imageChoice = self.Congratulations2
        elif choice == 3:
            imageChoice = self.Congratulations3

        self.ecardImage = PhotoImage(file = imageChoice) # initializing image
        self.canvas.create_image(0, 0, image = self.ecardImage, anchor = NW) # display image

        # Save Name Label
        label = Label(frame, text="Save file as: ")
        label.grid(column=2, row=0)
        # Save Name Entry Field
        self.saveName = Entry(frame)
        self.saveName.grid(column=3, row=0)
        # Save Button
        saveButton = Button(frame, text="Save", command=lambda : self.file_save(imageChoice))
        saveButton.grid(column=4, row=0)

    # Function for Anniversary occasion
    def anniversary(self):
        self.eCard = Toplevel()  # Create window
        self.eCard.title("E-Card Generator")  # Window title
        choice = randint(1,3) # Random variable between 1 and 3 to choose which image is displayed

        # Set canvas
        self.canvas = Canvas(self.eCard, width = 592, height = 420)
        self.canvas.pack()

        # Set Frame
        frame = Frame(self.eCard)
        frame.pack()

        imageChoice = ''

        # If statement to check the random choice to display image
        if choice == 1:
            imageChoice = self.Anniversary1
        elif choice == 2:
            imageChoice = self.Anniversary2
        elif choice == 3:
            imageChoice = self.Anniversary3

        self.ecardImage = PhotoImage(file = imageChoice) # initializing image
        self.canvas.create_image(0, 0, image = self.ecardImage, anchor = NW) # display image

        # Save Name Label
        label = Label(frame, text="Save file as: ")
        label.grid(column=2, row=0)
        # Save Name Entry Field
        self.saveName = Entry(frame)
        self.saveName.grid(column=3, row=0)
        # Save Button
        saveButton = Button(frame, text="Save", command=lambda : self.file_save(imageChoice))
        saveButton.grid(column=4, row=0)


Ecard()
