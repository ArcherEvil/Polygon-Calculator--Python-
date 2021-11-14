# The Main File with the main Source Code !!!!!!

from tkinter import *
import tkinter.font as tkFont

root = Tk() # Tkinter root
root.title("Polygon Calculator (By:Archer)") #Tkinter title
root.geometry("900x500") #tkinter window Size

# Classes
class App: #All the GUI things is in here
    def __init__(self, root):

        self.root = root

        # Main Frame
        self.mainframe = Frame(self.root, highlightthickness=0, borderwidth=0)
        self.mainframe.pack()

        # Title of the Program
        title_font = tkFont.Font(family="Segoi UI", size=30)
        title_font.configure(underline = True)
        title = Label(self.mainframe, text="Polygon Calculator", font=title_font, fg="#383838", bg="#ffbdbd", pady=10, padx=10)
        title.pack()

        # Loop
        self.root.mainloop()
        



if __name__ == "__main__":
    App(root)