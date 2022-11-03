# Module based on Python's idlelib module and StackOverflow answer by "crxguy52"
# 
# https://hg.python.org/cpython/file/63a00d019bb2/Lib/idlelib/ToolTip.py
# https://stackoverflow.com/a/36221216

import tkinter

class CreateToolTip(object):
    """
    Create a tooltip for widget object passed in.
    """

    def __init__(self, widget, text):
        self.waittime = 500     # milliseconds
        self.wraplength = 200   # pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event = None):
        self.schedule()

    def leave(self, event = None):
        self.unschedule()
        self.hidetip()

    def schedule(self = None):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self = None):
        id = self.id
        self.id = None

        if id:
            self.widget.after_cancel(id)

    def showtip(self, event = None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20

        # Create a toplevel window
        self.tw = tkinter.Toplevel(self.widget)

        # Leave only the label and remove the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))

        label = tkinter.Label(
                            self.tw,
                            text = self.text,
                            justify = "left",
                            background = "#ffffff",
                            relief = "solid",
                            borderwidth = 1,
                            wraplength = self.wraplength)

        label.pack(ipadx = 1)

    def hidetip(self):
        tw = self.tw
        self.tw = None

        if tw:
            tw.destroy()