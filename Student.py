from os import path, listdir
import tkinter as tk

# from fpdf import FPDF


PIC_FORMATS = ("jpg", "jpeg", "png", "gif")
test_img = path.abspath("C://Users/Chi/Desktop/test_img")


class Student:
    def __init__(self, name, old_list, _dir):
        updated_list = listdir(_dir)
        self.name = name
        self.submissions = [sub for sub in updated_list if sub not in old_list and sub.endswith(PIC_FORMATS)]

    @staticmethod
    def get_submission(_dir):
        return listdir(_dir)

    def __str__(self):
        return f"Student({self.name}, {self.submissions})"


class Button2(tk.Button):
    @property
    def filep(self):
        return self._filep

    @filep.setter
    def filep(self, value):
        self._filep = value
