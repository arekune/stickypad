import tkinter

class Notepad():

    def __init__(self, master):
        self.root = master
        self.root.title("Stickypad")
        self.root.iconbitmap("icons/sticky_note.ico")
        self.root.geometry("600x600")
    
    def run_app(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tkinter.Tk()
    notepad = Notepad(root)
    notepad.run_app()