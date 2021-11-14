# The Main File with the main Source Code !!!!!!

from tkinter import *
import tkinter.font as tkFont


root = Tk()  # Tkinter root
root.title("Polygon Calculator (By:Archer)")  # Tkinter title
root.geometry("900x500")  # tkinter window Size


# Classes
class App:  # All the GUI things is in here
    def __init__(self, root):
        self.root = root

        # Main Frame
        self.mainframe = Frame(self.root, highlightthickness=0, borderwidth=0)
        self.mainframe.pack()


        # Title of the Program
        title_frame = self.create_frame(self.mainframe)
        title_frame.pack()
        title_font = tkFont.Font(family="Segoe UI Black", size=30)
        title_font.configure(underline=True)
        title = Label(title_frame, text="Polygon Calculator", font=title_font, fg="#383838")
        title.grid(row=0, column=0)

        # Main Menu

        f_menu = Frame(self.mainframe, highlightthickness=0, borderwidth=0)
        f_menu.pack(pady=20)
        menu_list = ["Triangle",  # Menu text
                     "Square",
                     "Pentagon",
                     "Hexagon",
                     "Custom Shape"]

        menu_title_font = tkFont.Font(family="Segoe UI", size=15)
        menu_title = Label(f_menu, text="Choose the Polygon", font=menu_title_font)
        menu_title.pack()

        menu_var = IntVar()
        menu_var.set(0)
        f_button = self.create_frame(f_menu)
        f_button.pack()
        # Create Buttons
        for x, n in enumerate(menu_list):
            menu_buttons = Radiobutton(f_button, text=n, variable=menu_var, command=lambda x=x: self.polygon_choosed(x))
            menu_buttons.grid(column=x, row=0)


        # Loop
        self.root.mainloop()

    def create_frame(self, root):
        return Frame(root, highlightthickness=0, borderwidth=0)

    def polygon_choosed(self, value):
        print(value)


if __name__ == "__main__":
    App(root)
