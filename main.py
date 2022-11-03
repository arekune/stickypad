import tkinter
from tkinter import ttk, StringVar, IntVar, scrolledtext, messagebox, filedialog, END
from PIL import ImageTk, Image
from styles import *

class Notepad():

    def __init__(self, master):
        self.root = master
        self.root.title("Stickypad")
        self.root.iconbitmap("icons/sticky_note.ico")
        self.root.geometry("800x600")

        self.root.config(bg = colours["root_colour"])

        # Add frames
        self.menu_frame = self.create_menu_frame()
        self.text_frame = self.create_text_frame()

        self.menu_frame.pack(padx = 5, pady = 5)
        self.text_frame.pack(padx = 5, pady = 5)

        # Add buttons
        self.new_button = self.create_new_button()
        self.open_button = self.create_open_button()
        self.save_button = self.create_save_button()
        self.screenshot_button = self.create_screenshot_button()
        self.close_button = self.create_close_button()

        self.new_button.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.open_button.grid(row = 0, column = 1, padx = 5, pady = 5)
        self.save_button.grid(row = 0, column = 2, padx = 5, pady = 5)
        self.screenshot_button.grid(row = 0, column = 3, padx = 5, pady = 5)
        self.close_button.grid(row = 0, column = 4, padx = 5, pady = 5)

        # Add font dropdown menus and text highlight checkbutton
        self.font_family_drop = self.create_font_family_drop()
        self.font_option_drop = self.create_font_option_drop()
        self.highlight_check = self.create_highlight_check()

        self.font_family_drop.grid(row = 0, column = 5, padx = 5, pady = 5)
        self.font_option_drop.grid(row = 0, column = 6, padx = 5, pady = 5)
        self.highlight_check.grid(row = 0, column = 7, padx = 5, pady = 5)

        # Add font size slider and font size label to display font size
        self.font_size_slider = self.create_font_size_slider()
        self.font_size_label = self.create_font_size_label()
        self.font_size_value_label = self.create_font_size_value_label()

        self.font_size_slider.grid(row = 1, column = 4, columnspan = 2, sticky = "WE", padx = 5, pady = 5)
        self.font_size_label.grid(row = 1, column = 6, padx = 5, pady = 5, sticky = "W")
        self.font_size_value_label.grid(row = 1, column = 6, pady = 5)

        # Add text input
        self.text_input = self.create_text_input()

        self.text_input.pack()
    
    # APP LAYOUT

    # Frames

    def create_menu_frame(self):
        self.menu_frame = tkinter.Frame(self.root, bg = colours["menu_colour"])
        return self.menu_frame
    
    def create_text_frame(self):
        self.text_frame = tkinter.Frame(self.root, bg = colours["text_colour"])
        return self.text_frame

    # Buttons
    
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
    
    def create_screenshot_button(self):
        self.screenshot_button_image = ImageTk.PhotoImage(Image.open("icons/camera-icon.png"))
        self.button = tkinter.Button(self.menu_frame, image = self.screenshot_button_image, command = self.take_screenshot)
        return self.button
    
    def create_close_button(self):
        self.close_button_image = ImageTk.PhotoImage(Image.open("icons/close-icon.png"))
        self.button = tkinter.Button(self.menu_frame, image = self.close_button_image, command = self.close_note)
        return self.button

    # Font dropdown menus, sliders and highlighting toggle
    
    def create_font_family_drop(self):
        self.font_family_drop = ttk.Combobox(self.menu_frame,
                                            state = "readonly",
                                            value = font_families,
                                            font = ("Cambria", 10),
                                            justify = "center", height = 15)
        
        self.font_family_drop.set(font_families[0])
        self.font_family_drop.bind("<<ComboboxSelected>>", self.change_font)

        return self.font_family_drop
    
    def create_font_option_drop(self):
        self.font_option_drop = ttk.Combobox(self.menu_frame,
                                            state = "readonly",
                                            value = font_options,
                                            font = ("Cambria", 10),
                                            justify = "center",
                                            height = 15)
        
        self.font_option_drop.set("normal")
        self.font_option_drop.bind("<<ComboboxSelected>>", self.change_font)

        return self.font_option_drop
    
    def create_highlight_check(self):
        self.highlight = IntVar()
        self.highlight_check = tkinter.Checkbutton(self.menu_frame,
                                                    variable = self.highlight,
                                                    onvalue = 1,
                                                    offvalue = 0,
                                                    text = "Highlighting",
                                                    justify = "right",
                                                    height = 2,
                                                    width = 10,
                                                    bg = colours["menu_colour"])
        
        self.highlight.set(0)
        return self.highlight_check
    
    def create_font_size_slider(self):
        self.font_size = IntVar()
        self.font_size_slider = ttk.Scale(self.menu_frame,
                                        from_ = 0,
                                        to = 100,
                                        orient = "horizontal",
                                        variable = self.font_size,
                                        command = self.slider_changed)

        self.font_size.set(12)
        return self.font_size_slider
        
    def create_font_size_label(self):
        self.font_size_label = tkinter.Label(self.menu_frame,
                                            text = "Font size:",
                                            bg = colours["menu_colour"])
        return self.font_size_label
    
    def create_font_size_value_label(self):
        self.font_size_value_label = tkinter.Label(self.menu_frame,
                                                text = self.get_font_size_value(),
                                                bg = colours["menu_colour"])
        
        return self.font_size_value_label

    # Text input field
    
    def create_text_input(self):
        # Define variable for fonts
        self.chosen_font = (self.font_family_drop.get(), self.font_size.get())

        # Define ScrolledText widget to scroll through the text field
        # Set default width and height to be more than the window size so that
        # the text field size is constant relative to root window (i.e. scales with root window)
        self.text_input = scrolledtext.ScrolledText(self.text_frame,
                                                    width = 1000,
                                                    height = 100,
                                                    bg = colours["text_colour"],
                                                    font = self.chosen_font)
        
        return self.text_input


    # BUTTON AND SLIDER FUNCTIONALITY

    def new_note(self):
        pass

    def close_note(self):
        pass

    def save_note(self):
        pass

    def open_note(self):
        pass

    def take_screenshot(self):
        pass

    def change_font(self, event):
        pass

    def slider_changed(self, event):
        pass

    def get_font_size_value(self):
        return f"{self.font_size.get()}"


    # RUN PROGRAM

    def run_app(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tkinter.Tk()
    notepad = Notepad(root)
    notepad.run_app()