import tkinter as tk
import tkinter.filedialog as filedialog
from AssignmentGUI import MainPage


SETUP_STYLE = ("Arial", 16)

class SetupWindow(tk.Tk):

    '''Window shown at program startup.
    Requires user to specify downloads folder
    and assignment name.'''
    
    def __init__(self):
        # Initialization 
        tk.Tk.__init__(self)

        # Configuration of window
        self.geometry("400x250+910+400")
        self.resizable(0, 0)
        self.title("Assignment Compiler")


        self.greeting = tk.Label(self, text="Assignment Compiler", font=SETUP_STYLE)
        self.greeting.pack()

        # Assignment label
        self.assignment_name_label = tk.Label(self, text="Assignment Name:")
        self.assignment_name_label.pack()

        # Assignment label entry box
        self.assignment_name = tk.Entry(self, width=16, font=SETUP_STYLE)
        self.assignment_name.pack()
        
        # Button to open file dialog and select downloads folder
        self.folder_btn = tk.Button(self, text="Select Folder", font=SETUP_STYLE, command=self.set_folder)
        self.folder_btn.pack(pady=15)

        # Downloads folder label. Changes with selected folder
        self.folder_lbl = tk.Label(self, text="Path to downloads folder:", font=SETUP_STYLE)
        self.folder_lbl.pack()

        # Continue button. If required info is present, continues to main page
        self.continue_btn = tk.Button(self, text="Continue", font=SETUP_STYLE, command=lambda: self.setup_continue(self.folder_lbl.cget("text"), self.assignment_name.get()))
        self.continue_btn.pack(pady=5)

        self.mainloop()
    
    def set_folder(self):
        """Opens file dialog and changes self.folder_lbl text to selected folder path""" 
        self.folder = filedialog.askdirectory()
        self.folder_lbl.configure(text=f"Folder: {self.folder}")

    def setup_continue(self, dir, assignment_name):
        """Conitinues to main page if assingment name and downloads folder is specified"""
        if not assignment_name or dir == "Path to downloads folder:":
            MainPage.create_warning("Please make sure folder and assignment name are specified")
        else: 
            self.destroy()
            MainPage(dir, assignment_name)


setup = SetupWindow()
