#I believe this is to a good point.  It works for one..lol. It contains a list, a class, a GUI, and a conditional.
#All we need is a loop, but we talked about doing that by asking if they want to create another card.
#I tried to comment it well for you guys, let me know if I missed something.

from tkinter import *
from random import *
from shutil import *
import os


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

        # Move Generated .gif files to Generated_Gifs directory
        for file in os.listdir("./"):
            if file.endswith(".gif"):
                print(os.path.join("./", file))
                move(file, './Generated_Gifs/')

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

    def file_name(self):
        # Get Save Name from Entry Field
        self.input = self.saveName.get()
        return self.input

    def file_save(self, x):
        print(x, self.file_name())
        copyfile(x, './'+self.file_name()+'.gif')
        self.eCard.destroy()

    def christmas(self):
        print("Its Christmas")
        self.eCard = Toplevel()  # Create window
        self.eCard.title("E-Card Generator") # Window title
        choice = randint(1,3) # Random variabel between 1 and 3 to choose which image is displayed
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

    def valentines(self):
        print("Its Valentines Day")
        eCard = Toplevel()  # Create window
        eCard.title("E-Card Generator") # Window title
        choice = randint(1,3) # Random variabel between 1 and 3 to choose which image is displayed

        # Set canvas
        self.canvas = Canvas(eCard, width = 592, height = 420)
        self.canvas.pack()

        # Set Frame
        frame = Frame(eCard)
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

    def birthday(self):
        print("Its Your Birthday")
        eCard = Toplevel()  # Create window
        eCard.title("E-Card Generator") # Window title
        choice = randint(1,3) # Random variabel between 1 and 3 to choose which image is displayed

        # Set canvas
        self.canvas = Canvas(eCard, width = 592, height = 420)
        self.canvas.pack()

        # Set Frame
        frame = Frame(eCard)
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


    def congratulations(self):
        print("Congrats!")
        eCard = Toplevel()  # Create window
        eCard.title("E-Card Generator") # Window title
        choice = randint(1,3) # Random variabel between 1 and 3 to choose which image is displayed

        # Set canvas
        self.canvas = Canvas(eCard, width = 592, height = 420)
        self.canvas.pack()

        # Set Frame
        frame = Frame(eCard)
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

    def anniversary(self):
        print("Happy Anniversary")
        eCard = Toplevel()  # Create window
        eCard.title("E-Card Generator") # Window title
        choice = randint(1,3) # Random variabel between 1 and 3 to choose which image is displayed

        # Set canvas
        self.canvas = Canvas(eCard, width = 592, height = 420)
        self.canvas.pack()

        # Set Frame
        frame = Frame(eCard)
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
