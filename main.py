import tkinter
from styles import *

class Notepad():

    def __init__(self, master):
        self.root = master
        self.root.title("Stickypad")
        self.root.iconbitmap("icons/sticky_note.ico")
        self.root.geometry("600x600")

        self.root.config(bg = colours["root_colour"])

        # Add frames
        self.menu_frame = self.create_menu_frame()
        self.text_frame = self.create_text_frame()

        self.menu_frame.pack(padx = 5, pady = 5)
        self.text_frame.pack(padx = 5, pady = 5)
    
    # APP LAYOUT

    def create_menu_frame(self):
        self.menu_frame = tkinter.Frame(self.root, bg = colours["menu_colour"])
        return self.menu_frame
    
    def create_text_frame(self):
        self.text_frame = tkinter.Frame(self.root, bg = colours["text_colour"])
        return self.text_frame

    # RUN PROGRAM

    def run_app(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tkinter.Tk()
    notepad = Notepad(root)
    notepad.run_app()