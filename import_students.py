import pandas as pd
import tkinter as tk
import tkinter.filedialog as filedialog
from StudentClass import Student


class Import(tk.Tk):
    

    def __init__(self):
        
        tk.Tk.__init__(self)
        open_btn = tk.Button(self, text="Open", command=self.open_file)
        open_btn.pack()

        self.student_label = tk.Label(self, text="")
        self.student_label.pack()
        
        self.mainloop()
    
    def open_file(self):
        file = filedialog.askopenfile()
        btn_list = []
        f = pd.read_csv(file)
        for name in f:
            
            # name_btn = tk.Button(self, text=name, command=lambda: self.display_student(name_btn.cget("text")))
            btn_list.append(Student(name, self.student_label))
            # btn_list.append(tk.Button(self, text=name, command=lambda : self.display_student(self.cget("text"))))
        for btn in btn_list:
            btn.pack(expand=True, fill=tk.BOTH)
    

if __name__ == "__main__":
    Import()


# names = pd.read_csv("students.csv")

# for name in names: 
#     print(name)

# Click button to initiate import of student name file/csv
# Possibly preview data from that file. Names should all be separated by commas
# Load names into a list or other appropriate data structure
# Loop through names and create tkinter buttons with corresponding names
# When a student is clicked, their name will be displayed as an active user which assignments will currently be downloaded for
