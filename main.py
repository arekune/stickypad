import tkinter
import pyautogui
import time
from tkinter import ttk, IntVar, scrolledtext, colorchooser, messagebox, filedialog, END
from PIL import ImageTk, Image
from styles import *
from tooltip import CreateToolTip

class Notepad():

    def __init__(self, master):
        self.root = master
        self.root.title("Stickypad")
        self.root.iconbitmap("icons/sticky_note.ico")
        self.root.geometry("900x700")
        self.root.resizable(0, 0)

        self.root.config(bg = colours["root_colour"])

        # Counter for number of text tags (see function 'change_tag_font')
        self.tags = 0

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

        self.new_button.grid(row = 0, column = 0, padx = (15, 5), pady = 5)
        self.open_button.grid(row = 0, column = 1, padx = 5, pady = 5)
        self.save_button.grid(row = 0, column = 2, padx = (5, 0), pady = 5, sticky = "W")
        self.screenshot_button.grid(row = 0, column = 3, padx = (0, 15), pady = 5, sticky = "E")
        self.close_button.grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "W")

        # Add font dropdown menus and text highlight checkbutton
        self.font_family_drop = self.create_font_family_drop()
        self.font_option_drop = self.create_font_option_drop()
        self.highlight_check = self.create_highlight_check()

        self.font_family_drop.grid(row = 0, column = 5, padx = 5, pady = 5)
        self.font_option_drop.grid(row = 0, column = 6, padx = 5, pady = 5)
        self.highlight_check.grid(row = 0, column = 7, padx = 5, pady = 5)

        # Add text input field colour selector button
        self.colour_selector_button = self.create_colour_selector_button()

        self.colour_selector_button.grid(row = 1, column = 0, columnspan = 2, padx = (15, 5), pady = 5, ipadx = 5, ipady = 5)

        # Add reset settings button
        self.reset_button = self.create_reset_button()

        self.reset_button.grid(row = 1, column = 2, columnspan = 2, padx = 5, pady = 5, ipadx = 5, ipady = 5)

        # Add font size slider and font size label to display font size
        self.font_size_slider = self.create_font_size_slider()
        self.font_size_label = self.create_font_size_label()
        self.font_size_value_label = self.create_font_size_value_label()

        self.font_size_slider.grid(row = 1, column = 4, columnspan = 2, sticky = "WE", padx = 5, pady = 5)
        self.font_size_label.grid(row = 1, column = 6, sticky = "W", padx = 5, pady = 5)
        self.font_size_value_label.grid(row = 1, column = 6, pady = 5)

        # Add underline and overstrike buttons
        self.underline_button = self.create_underline_button()
        self.overstrike_button = self.create_overstrike_button()

        self.underline_button.grid(row = 1, column = 6, padx = 5, pady = 5, ipady = 5, sticky = "E")
        self.overstrike_button.grid(row = 1, column = 7, padx = 5, pady = 5, ipady = 5)

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

        self.new_button_tooltip = CreateToolTip(self.button, "Create a new note")

        return self.button
    
    def create_open_button(self):
        self.open_button_image = ImageTk.PhotoImage(Image.open("icons/folder-open-icon.png"))
        self.button = tkinter.Button(self.menu_frame, image = self.open_button_image, command = self.open_note)

        self.open_button_tooltip = CreateToolTip(self.button, "Open a saved note")

        return self.button
    
    def create_save_button(self):
        self.save_button_image = ImageTk.PhotoImage(Image.open("icons/disk-icon.png"))
        self.button = tkinter.Button(self.menu_frame, image = self.save_button_image, command = self.save_note)

        self.save_button_tooltip = CreateToolTip(self.button, "Save note")

        return self.button
    
    def create_screenshot_button(self):
        self.screenshot_button_image = ImageTk.PhotoImage(Image.open("icons/camera-icon.png"))
        self.button = tkinter.Button(self.menu_frame, image = self.screenshot_button_image, command = self.take_screenshot)
        
        self.screenshot_button_tooltip = CreateToolTip(self.button, "Take a screenshot of sticky note")

        return self.button
    
    def create_close_button(self):
        self.close_button_image = ImageTk.PhotoImage(Image.open("icons/close-icon.png"))
        self.button = tkinter.Button(self.menu_frame, image = self.close_button_image, command = self.close_note)

        self.close_button_tooltip = CreateToolTip(self.button, "Close note and exit program")

        return self.button

    # Font dropdown menus, sliders and highlighting toggle
    
    def create_font_family_drop(self):
        self.font_family_drop = ttk.Combobox(self.menu_frame,
                                            state = "readonly",
                                            value = font_families,
                                            font = ("Cambria", 10),
                                            justify = "center",
                                            height = 15)
        
        self.font_family_tooltip = CreateToolTip(self.font_family_drop, "Choose font family")
        
        self.font_family_drop.set("Terminal")
        self.font_family_drop.bind("<<ComboboxSelected>>", self.change_font)

        return self.font_family_drop
    
    def create_font_option_drop(self):
        self.font_option_drop = ttk.Combobox(self.menu_frame,
                                            state = "readonly",
                                            value = font_options,
                                            font = ("Cambria", 10),
                                            justify = "center",
                                            height = 15)
        
        self.font_option_tooltip = CreateToolTip(self.font_option_drop, "Choose font option")
        
        self.font_option_drop.set("normal")
        self.font_option_drop.bind("<<ComboboxSelected>>", self.change_font)

        return self.font_option_drop
    
    def create_highlight_check(self):
        self.highlight_on = IntVar()
        self.highlight_check = tkinter.Checkbutton(self.menu_frame,
                                                    variable = self.highlight_on,
                                                    onvalue = 1,
                                                    offvalue = 0,
                                                    text = "Highlighting",
                                                    justify = "right",
                                                    height = 2,
                                                    width = 10,
                                                    bg = colours["menu_colour"])
        
        self.font_highlight_tooltip = CreateToolTip(self.highlight_check, "Toggle highlighting on and off")
        
        self.highlight_on.set(0)
        return self.highlight_check
    
    def create_font_size_slider(self):
        self.font_size = IntVar()
        self.font_size_slider = ttk.Scale(self.menu_frame,
                                        from_ = 1,
                                        to = 100,
                                        orient = "horizontal",
                                        variable = self.font_size,
                                        command = self.slider_changed)
        
        self.font_size_tooltip = CreateToolTip(self.font_size_slider, "Choose font size between 1 and 100")

        self.font_size.set(12)
        return self.font_size_slider
        
    def create_font_size_label(self):
        self.font_size_label = tkinter.Label(self.menu_frame,
                                            text = "Font size:",
                                            bg = colours["menu_colour"])
        return self.font_size_label
    
    def create_font_size_value_label(self):
        self.font_size_value_label = tkinter.Label(self.menu_frame,
                                                text = f"{self.font_size.get()}",
                                                bg = colours["menu_colour"])
        
        return self.font_size_value_label
    
    def create_underline_button(self):
        self.underline_button = ttk.Button(self.menu_frame,
                                        text = "a͟b͟c͟",
                                        width = 8,
                                        command = self.underline_tag)
        
        self.underline_tooltip = CreateToolTip(self.underline_button, "Underline text")
        
        return self.underline_button
    
    def create_overstrike_button(self):
        self.overstrike_button = ttk.Button(self.menu_frame,
                                        text = "a̵b̵c̵",
                                        width = 8,
                                        command = self.overstrike_tag)
        
        self.overstrike_tooltip = CreateToolTip(self.overstrike_button, "Overstrike text")
        
        return self.overstrike_button

    # Text input field and text input colour selector button
    
    def create_text_input(self):
        # Define variable for fonts
        self.chosen_font = (self.font_family_drop.get(), self.font_size.get())

        # Define ScrolledText widget to scroll through the text field
        # Set default width and height to be more than the window size so that
        # the text field size is constant relative to root window (i.e. scales with root window)
        self.text_input = scrolledtext.ScrolledText(self.text_frame,
                                                    width = 1500,
                                                    height = 200,
                                                    bg = colours["text_colour"],
                                                    font = self.chosen_font)
        
        return self.text_input
    
    def create_colour_selector_button(self):
        self.colour_selector_button = ttk.Button(self.menu_frame,
                                                text = "Select a Colour",
                                                command = self.change_colour)
        
        self.colour_selector_tooltip = CreateToolTip(self.colour_selector_button,
                                                    "Create and choose custom color for sticky note")
        
        return self.colour_selector_button
    
    def create_reset_button(self):
        self.reset_button = ttk.Button(self.menu_frame,
                                        text = "Reset",
                                        command = self.reset_all)
        
        self.reset_tooltip = CreateToolTip(self.reset_button, "Reset all settings")
        
        return self.reset_button


    # BUTTON AND SLIDER FUNCTIONALITY

    def change_colour(self):
        """Change text input field colour by choosing custom colour with Tkinter's colour selector."""

        self.colour_selector = colorchooser.askcolor(title = "Colour Selection")
        self.text_input.config(bg = self.colour_selector[1])
    

    def reset_all(self):
        """Reset all settings to default."""

        self.text_input.config(bg = colours["text_colour"])
        self.font_family_drop.set("Terminal")
        self.font_option_drop.set("normal")
        self.font_size.set(12)
        self.highlight_on.set(0)
        self.font_size_value_label.configure(text = f"{self.font_size.get()}")


    def change_font(self, event):
        """Change text font based on dropdown menu options and font size slider value."""
        if self.highlight_on.get() == 1:
            self.change_tag_font()

        else:
            # Delete all tags in text in order to apply the exact same font configurations for all text
            for tag in self.text_input.tag_names():
                self.text_input.tag_delete(tag)

            if self.font_option_drop.get() == "None":
                self.chosen_font = (self.font_family_drop.get(), self.font_size.get())
            else:
                self.chosen_font = (self.font_family_drop.get(), self.font_size.get(), self.font_option_drop.get())
        
        # Change font style
        if self.highlight_on.get() == 0:
            return self.text_input.config(font = self.chosen_font)
    

    def tag_update(self):
        """Update tag counter for dynamic tag name creation."""
        self.tags += 1
    

    def change_tag_font(self):
        """
        Change font configuration on sections of text highlighted with a tag.

        Each tag name is dynamically generated by updating the tag counter and setting
        the current value of the counter as the tag name.
        """

        self.tag_update()
        self.text_input.tag_config(f"{self.tags}", font = (self.font_family_drop.get(),
                                                            self.font_size.get(),
                                                            self.font_option_drop.get()))

        try:
            self.text_input.tag_add(f"{self.tags}", "sel.first", "sel.last")
        except tkinter.TclError:
            # If no text is highlighted for tagging
            pass
    

    def underline_tag(self):
        """Underline text.
        
        If highlighting is on, only highlighted text will be underlined with a tag.
        Otherwise the whole text under current font configurations will be underlined.
        """

        self.tag_update()
        self.text_input.tag_config(f"{self.tags}", font = (self.font_family_drop.get(),
                                                            self.font_size.get(),
                                                            self.font_option_drop.get()),
                                                            underline = True)

        if self.highlight_on.get() == 1:
            try:
                self.text_input.tag_add(f"{self.tags}", "sel.first", "sel.last")
            except tkinter.TclError:
                # If no text is highlighted for tagging
                pass
        
        else:
            self.text_input.tag_add(f"{self.tags}", "1.0", END)


    def overstrike_tag(self):
        """Overstrike text.
        
        If highlighting is on, only highlighted text will be overstruck with a tag.
        Otherwise the whole text under current font configurations will be overstruck.
        """
        
        self.tag_update()
        self.text_input.tag_config(f"{self.tags}", font = (self.font_family_drop.get(),
                                                            self.font_size.get(),
                                                            self.font_option_drop.get()),
                                                            overstrike = True)

        if self.highlight_on.get() == 1:
            try:
                self.text_input.tag_add(f"{self.tags}", "sel.first", "sel.last")
            except tkinter.TclError:
                # If no text is highlighted for tagging
                pass
        
        else:
            self.text_input.tag_add(f"{self.tags}", "1.0", END)


    def new_note(self):
        """Create a new note that clears the text input field."""

        # Use a messagebox to confirm clearing note and creating a new note
        question = messagebox.askyesnocancel("New Note",
        "Are you sure that you want to create a new note?\n \
        Unsaved changes to current note will be deleted.")

        if question == 1:
            # ScrolledText widget indexing starts at "1.0"
            self.text_input.delete("1.0", END)


    def close_note(self):
        """Close the note and the window to quit program."""

        question = messagebox.askyesnocancel("Close Note",
        "Are you sure that you want to close the note?\n \
        Unsaved changes to current note will be deleted.")

        if question == 1:
            self.root.destroy()


    def save_note(self):
        """
        Save the note as a txt file.
        The first three lines saved to the file are saved as font family, font size, and font option.
        Font size is converted to a string for the file.

        Only the font configurations chosen when saving will be preserved and later applied to
        a text file opened again as a note in Stickypad.
        """

        # Use filedialog (imported from tkinter) to ask user for file path and file name
        # this will initialize a file path and file name for us to use when writing to a file
        save_name = filedialog.asksaveasfilename(initialdir = "./",
                                                title = "Save Note",
                                                defaultextension = ".txt",
                                                filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")))
        
        # Write first three lines of font specification
        try:
            with open(save_name, "w") as file:
                file.write(self.font_family_drop.get() + "\n")
                file.write(str(self.font_size.get()) + "\n")
                file.write(self.font_option_drop.get() + "\n")
            
                # Write remaining text to the file with starting and ending indexes specified
                file.write(self.text_input.get("1.0", END))

        except FileNotFoundError:
            # If no filename is given
            pass


    def open_note(self):
        """
        Open a previously saved note.
        The first three lines of file are the file's specified font family, font size, and font option.
        """

        question = messagebox.askyesnocancel("Open Note",
        "Are you sure that you want to open another new note?\nUnsaved changes to current note will be deleted.")

        if question == 1:
            # Use filedialog to ask user for file path and to choose the file to be opened
            open_name = filedialog.askopenfilename(initialdir = "./",
                                                    title = "Open Note",
                                                    filetypes = (("Text Files", "*.txt"), ("All Files", "*.*")))
            
            try:
                with open(open_name, "r+") as file:
                    self.text_input.delete("1.0", END)

                    # Newline characters at the end of the first three lines need to be stripped
                    self.font_family_drop.set(file.readline().strip())
                    self.font_size.set(int(file.readline().strip()))
                    self.font_option_drop.set(file.readline().strip())

                    # Call change_font function to implement the .set() methods, pass in arbitrary value
                    self.change_font(1)

                    # Read the rest of the file and insert into the text field
                    text = file.read()
                    self.text_input.insert("1.0", text)

            except FileNotFoundError:
                # If no filename is given
                pass


    def take_screenshot(self):
        """
        Take screenshot of text input field as a virtual sticky note using Pyautogui.
        
        The screenshot will be saved in the local directory as 'screenshot.png'.
        Any similarly named file will be over written.
        """

        question = messagebox.askyesnocancel("Screenshot",
        "Do you want to take a screenshot of the current sticky note?\
        Please move or rename any previously taken screenshots to avoid\
        having them replaced by a new screenshot.")

        if question == 1:
            x, y = self.text_input.winfo_rootx(), self.text_input.winfo_rooty()
            w, h = self.text_input.winfo_width(), self.text_input.winfo_height()
            # Timer to ensure that Pyautogui doesn't screenshot the messagebox
            time.sleep(0.5)
            pyautogui.screenshot("screenshot.png", region = (x, y, w, h))


    def slider_changed(self, event):
        """
        Set the font size value label when the slider is moved.
        'Change_font' function is called to apply the change in font size to text.
        """

        self.font_size_value_label.configure(text = f"{self.font_size.get()}")
        self.change_font(event)


    # RUN PROGRAM

    def run_app(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tkinter.Tk()
    notepad = Notepad(root)
    notepad.run_app()