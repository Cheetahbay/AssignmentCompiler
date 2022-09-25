from cProfile import label
import tkinter as tk



class Student(tk.Button):
    def __init__(self, name, label):
        tk.Button.__init__(self, text=name, command=lambda: self.display_student(self.cget("text"), label))
        self.name = name
        self.pack()
        
    def display_student(self, name, label):
        # change the Import.student_label to the text value of the clicked button
        label.configure(text=name)
        print(name)