# The Main File with the main Source Code !!!!!!

from tkinter import *
import tkinter.font as tkFont


root = Tk() # Tkinter root
root.title("Polygon Calculator (By:Archer)") #Tkinter title
root.geometry("900x500") #tkinter window Size


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

        self.f_menu = Frame(self.mainframe, highlightthickness=0, borderwidth=0)
        self.f_menu.pack(pady=20)
        menu_list = ["Triangle",  # Menu text
                     "Square",
                     "Pentagon",
                     "Hexagon",
                     "Custom Shape"]

        menu_title_font = tkFont.Font(family="Segoe UI", size=15)
        menu_title = Label(self.f_menu, text="Choose the Polygon", font=menu_title_font)
        menu_title.pack()

        menu_var = IntVar()
        menu_var.set(0)
        f_button = self.create_frame(self.f_menu)
        f_button.pack()
        # Create Buttons
        for x, n in enumerate(menu_list):
            menu_buttons = Radiobutton(f_button, text=n, value=(x + 1)
            , variable=menu_var, command=lambda x=x: self.polygon_choosed(x))
            menu_buttons.grid(column=x, row=0)

        self.menuitems = [] # a list to store all the menu options widgets to delete them


        # Loop
        self.root.mainloop()

    def create_frame(self, root):
        return Frame(root, highlightthickness=0, borderwidth=0)

    def polygon_choosed(self, value):
        try:
            for n in self.menuitems:
                n.destroy()
        except:
            pass

        self.inputlist = [] # input list to destroy later

        # Sub Menus
        match value:
            case 0: #Triangle
                print("Triangle")# Triangle
                f_submenu = self.create_frame(self.f_menu) # Creating a sub menu
                f_submenu.pack()
                self.menuitems.append(f_submenu)

                f_submenu_options = self.create_frame(f_submenu)
                f_submenu_options.grid(row=0, column=0)
                self.menuitems.append(f_submenu_options)

                submenu_title_font = tkFont.Font(family="Segoe UI SemiBold", size=17, underline=True)
                submenu_title = Label(f_submenu_options, text="Triangle", font=submenu_title_font)
                self.menuitems.append(submenu_title)
                submenu_title.pack()

                # submenu radio buttons
                names = ["Area", "Perimeter", "Pythagorean theorem"]

                var = StringVar()
                var.set("a")

                for n in names:
                    button = Radiobutton(f_submenu_options, text=n, value=n, variable=var,
                     command=lambda: self.input(["triangle", var.get()]))
                    self.menuitems.append(button)
                    button.pack()            
            case 1: #Square
                print("Square")# Square

                f_submenu = self.create_frame(self.f_menu) # Creating a sub menu
                f_submenu.pack()
                self.menuitems.append(f_submenu)

                f_submenu_options = self.create_frame(f_submenu)
                f_submenu_options.grid(row=0, column=0)
                self.menuitems.append(f_submenu_options)

                submenu_title_font = tkFont.Font(family="Segoe UI SemiBold", size=17, underline=True)
                submenu_title = Label(f_submenu_options, text="Square", font=submenu_title_font)
                self.menuitems.append(submenu_title)
                submenu_title.pack()

                # submenu radio buttons
                names = ["Area", "Perimeter"]

                var = StringVar()
                var.set("a")

                for n in names:
                    button = Radiobutton(f_submenu_options, text=n, value=n, variable=var,
                     command=lambda: self.input(["square", var.get()]))
                    self.menuitems.append(button)
                    button.pack()
            case 2: #Pentagon
                print("Pentagon")# Pentagon

                f_submenu = self.create_frame(self.f_menu) # Creating a sub menu
                f_submenu.pack()
                self.menuitems.append(f_submenu)

                f_submenu_options = self.create_frame(f_submenu)
                f_submenu_options.grid(row=0, column=0)
                self.menuitems.append(f_submenu_options)

                submenu_title_font = tkFont.Font(family="Segoe UI SemiBold", size=17, underline=True)
                submenu_title = Label(f_submenu_options, text="Pentagon", font=submenu_title_font)
                self.menuitems.append(submenu_title)
                submenu_title.pack()

                # submenu radio buttons
                names = ["Area", "Perimeter"]

                var = StringVar()
                var.set("a")

                for n in names:
                    button = Radiobutton(f_submenu_options, text=n, value=n, variable=var,
                     command=lambda: self.input(["pentagon", var.get()]))
                    self.menuitems.append(button)
                    button.pack()     
            case 3: #Hexagon
                print("Hexagon")# Hexagon
                
                f_submenu = self.create_frame(self.f_menu) # Creating a sub menu
                f_submenu.pack()
                self.menuitems.append(f_submenu)

                f_submenu_options = self.create_frame(f_submenu)
                f_submenu_options.grid(row=0, column=0)
                self.menuitems.append(f_submenu_options)

                submenu_title_font = tkFont.Font(family="Segoe UI SemiBold", size=17, underline=True)
                submenu_title = Label(f_submenu_options, text="Hexagon", font=submenu_title_font)
                self.menuitems.append(submenu_title)
                submenu_title.pack()

                # submenu radio buttons
                names = ["Area", "Perimeter"]

                var = StringVar()
                var.set("a")

                for n in names:
                    button = Radiobutton(f_submenu_options, text=n, value=n, variable=var,
                     command=lambda: self.input(["hexagon", var.get()]))
                    self.menuitems.append(button)
                    button.pack()
            case 4: #Custom Shape
                print("Custom Shape")# Custom Shape

                
                f_submenu = self.create_frame(self.f_menu) # Creating a sub menu
                self.f_submenu = f_submenu
                f_submenu.pack()
                self.menuitems.append(f_submenu)

                f_submenu_options = self.create_frame(f_submenu)
                f_submenu_options.grid(row=0, column=0)
                self.menuitems.append(f_submenu_options)

                submenu_title_font = tkFont.Font(family="Segoe UI SemiBold", size=17, underline=True)
                submenu_title = Label(f_submenu_options, text="Custom Shape", font=submenu_title_font)
                self.menuitems.append(submenu_title)
                submenu_title.pack()

                # submenu radio buttons
                names = ["Area", "Perimeter"]

                var = StringVar()
                var.set("a")

                for n in names:
                    button = Radiobutton(f_submenu_options, text=n, value=n, variable=var, 
                    command=lambda: self.input(["custom", var.get()]))
                    self.menuitems.append(button)
                    button.pack()


    # Sub menu functions
    def input(self, value):
        print(value)

        match value[0]:
            case "triangle":
                match value[1]:
                    case "Area":
                        pass
                    case "Perimeter":
                        pass
                    case "Pythagorean theorem":
                        pass
            case "square":
                match value[1]:
                    case "Area":
                        pass
                    case "Perimeter":
                        pass
            case "pentagon":
                match value[1]:
                    case "Area":
                        pass
                    case "Perimeter":
                        pass
            case "hexagon":
                match value[1]:
                    case "Area":
                        pass
                    case "Perimeter":
                        pass
            case "custom":
                match value[1]:
                    case "Area":
                        pass
                    case "Perimeter":
                        pass
                            
        


if __name__ == "__main__":
    App(root)

