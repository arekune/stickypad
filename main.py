import tkinter
from styles import *

class Notepad():

    def __init__(self, master):
        self.root = master
        self.root.title("Stickypad")
        self.root.iconbitmap("icons/sticky_note.ico")
        self.root.geometry("600x600")

        self.root.config(bg = colours["root_colour"])
    
    # APP LAYOUT

    def create_menu_frame(self):
        self.menu_frame = tkinter.Frame(self.root, bg = colours["menu_colour"])
        return self.menu_frame

    # RUN PROGRAM
    
    def run_app(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tkinter.Tk()
    notepad = Notepad(root)
    notepad.run_app()