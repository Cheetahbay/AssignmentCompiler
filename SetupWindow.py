import tkinter as tk
import tkinter.filedialog as filedialog
from AssignmentGUI import MainPage


SETUP_STYLE = ("Arial", 16)

class SetupWindow(tk.Tk):

    '''Window shown at program startup.
    Requires user to specify downloads folder
    and assignment name.'''
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("400x250+910+400")
        self.resizable(0, 0)
        self.title("Assignment Compiler")

        self.greeting = tk.Label(self, text="Assignment Compiler", font=SETUP_STYLE)
        self.greeting.pack()

        self.assignment_name_label = tk.Label(self, text="Assignment Name:")
        self.assignment_name_label.pack()

        self.assignment_name = tk.Entry(self, width=16, font=SETUP_STYLE)
        self.assignment_name.pack()

        self.folder_btn = tk.Button(self, text="Select Folder", font=SETUP_STYLE, command=self.set_folder)
        self.folder_btn.pack(pady=15)

        self.folder_lbl = tk.Label(self, text="Path to downloads folder:", font=SETUP_STYLE)
        self.folder_lbl.pack()

        self.continue_btn = tk.Button(self, text="Continue", font=SETUP_STYLE, command=lambda: self.setup_continue(self.folder_lbl.cget("text"), self.assignment_name.get()))
        self.continue_btn.pack(pady=5)

        self.mainloop()
    
    def set_folder(self):
        self.folder = filedialog.askdirectory()
        self.folder_lbl.configure(text=f"Folder: {self.folder}")

    def setup_continue(self, dir, assignment_name):
        if not assignment_name or dir == "Path to downloads folder:":
            MainPage.create_warning("Please make sure folder and assignment name are specified")
        else: 
            self.destroy()
            MainPage(dir, assignment_name)


setup = SetupWindow()
