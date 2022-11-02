import tkinter
from PIL import ImageTk, Image
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
    
    def create_new_button(self):
        self.new_button_image = ImageTk.PhotoImage(Image.open("icons/document-icon.png"))
        self.button = tkinter.Button(self.menu_frame, image = self.new_button_image, command = self.new_note)
        return self.button
    
    def create_open_button(self):
        self.open_button_image = ImageTk.PhotoImage(Image.open("icons/folder-open-icon.png"))
        self.button = tkinter.Button(self.menu_frame, image = self.open_button_image, command = self.open_note)
        return self.button
    
    def create_save_button(self):
        self.save_button_image = ImageTk.PhotoImage(Image.open("icons/disk-icon.png"))
        self.button = tkinter.Button(self.menu_frame, image = self.save_button_image, command = self.save_note)
        return self.button
    
    def create_close_button(self):
        self.close_button_image = ImageTk.PhotoImage(Image.open("icons/close.png"))
        self.button = tkinter.Button(self.menu_frame, image = self.close_button_image, command = self.close_note)
        return self.button
    
    # BUTTON AND SLIDER FUNCTIONALITY

    def new_note(self):
        pass

    def close_note(self):
        pass

    def save_note(self):
        pass

    def open_note(self):
        pass


    # RUN PROGRAM

    def run_app(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tkinter.Tk()
    notepad = Notepad(root)
    notepad.run_app()