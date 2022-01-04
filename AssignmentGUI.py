from Student import Student, Button2
import tkinter.filedialog
import tkinter as tk
from datetime import date
import shutil
from os import path
from PIL import Image, ImageTk
from fpdf import FPDF

deleted_files = path.abspath("C:/Users/Chi/Desktop/removed")
student_list = []
master_list = []
MAIN_COLOR = "#007580"
SEC_COLOR = "#282846"
DL_HELP = "Download submissions for student.\nClick 'Create when finished"
LIST_HELP = "Click 'Get List' to start on another student"


class MainPage(tk.Tk):
    def __init__(self, _dir: str, ass_name):
        tk.Tk.__init__(self)  # initialization of tkinter
        self.geometry("650x700+910+400")
        self.title("PDF Creator")
        self.propagate(0)
        self._dir = _dir
        self.ass_name = ass_name
        #  LEFT, RIGHT, AND MIDDLE FRAMES
        self.leftFrame = tk.Frame(self)
        self.rightFrame = tk.Frame(self)
        self.middleFrame = tk.Frame(self)
        self.leftFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.rightFrame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        self.middleFrame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

        #  Frame for user input (assignment, student name, folder path)
        self.input_frame = tk.Frame(self.leftFrame, pady=20, bg="blue")
        self.input_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

        #  Frame for student buttons
        self.student_btn_frame = tk.Frame(self.leftFrame, bg="white")
        self.student_btn_frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        #  Split into left & right halves
        self.student_lframe = tk.Frame(self.student_btn_frame, bg="orange")
        self.student_rframe = tk.Frame(self.student_btn_frame, bg="yellow")
        self.student_lframe.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.student_rframe.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        #  Frame for create button and user feedback
        self.info_frame = tk.Frame(self.rightFrame, bg="green")
        self.info_frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

        # Input frame widgets
        self.assignment_lbl = tk.Label(self.input_frame, text=f"Assignment: {self.ass_name}", font=("Arial", 18))
        self.assignment_lbl.grid(column=0, row=1, sticky=tk.W)
        self.folder_name = tk.Label(self.input_frame, text=f"Folder: {self._dir.split('/')[-1]}", font=("Arial", 18))
        self.folder_name.grid(column=0, row=2, sticky=tk.W)
        self.name_lbl = tk.Label(self.input_frame, text="Name:", font=("Arial", 18))
        self.name_entry = tk.Entry(self.input_frame, width=18, font=("Arial", 18))
        self.name_lbl.grid(column=0, row=3, sticky=tk.W)
        self.name_entry.grid(column=1, row=3, sticky=tk.W)

        # Info frame button/s
        self.action_btn = tk.Button(self.info_frame, text="Create", font=("Arial", 18),
                                    command=lambda: self.switch(self.btn_txt))
        self.btn_txt = self.action_btn.cget("text")
        self.action_btn.pack(fill=tk.BOTH)
        # self.create = tk.Button(self.info_frame, text="Create", font=("Arial", 18),
        #                         command=lambda: self.create_student(self.name_entry.get(), master_list,
        #                                                             self._dir))
        # self.create.pack(fill=tk.BOTH)
        self.save_btn = tk.Button(self.info_frame, text="Save", font=("Arial", 18),
                                  command=lambda: self.save(self.ass_name, student_list, self._dir))
        self.save_btn.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.get_list()
        self.mainloop()

    #  Button functions
    def switch(self, txt):
        help_lbl = tk.Label(self.info_frame)

        if txt == "Get List":
            self.get_list()
            help_lbl.configure(text=DL_HELP)
            help_lbl.pack()
        if txt == "Create":
            self.create_student(self.name_entry.get(), master_list, self._dir)
            help_lbl.configure(text=LIST_HELP)
            help_lbl.pack()
        self.btn_txt = self.action_btn.cget("text")

    def get_list(self):
        global master_list
        # tk.Label(self, text="Start Downloading").pack()
        self.action_btn.configure(text="Create")
        master_list = Student.get_submission(self._dir)

    def create_student(self, name, ML, _dir):
        # Creates new student if name_entry widget has a value, else prompts user for a value
        if name.isspace() or name == "":
            message = "Enter Student Name first"
            MainPage.create_warning(message)
        else:
            self.action_btn.configure(text="Get List")
            self.name_entry.delete(0, tk.END)
            new_student = Student(name, ML, _dir)
            student_list.append(new_student)

            #  Pack the left frame with student buttons, then pack right frame when left frame is full
            if len(self.student_lframe.winfo_children()) <= 10:
                name_btn = tk.Button(self.student_lframe, text=new_student.name,
                                     command=lambda: self.show_submissions(name_btn.cget("text"), name_btn,
                                                                           self._dir))
                name_btn.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)
                name_btn.configure(font=("Arial", 16))
            elif len(self.student_rframe.winfo_children()) <= 10:
                name_btn = tk.Button(self.student_rframe, text=new_student.name,
                                     command=lambda: self.show_submissions(name_btn.cget("text"), name_btn,
                                                                           self._dir))
                name_btn.configure(font=("Arial", 16))
                name_btn.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)
            # self.submissions_box.insert(tk.END, f"Name:{new_student.name}\nSubmissions: {new_student.submissions}")

    # TODO: Fix redundant method calls (show_submissions, view)
    def show_submissions(self, name, btn, _dir):
        self.view(name, btn, _dir)

    def view(self, name, btn, _dir):
        view_win_root = tk.Toplevel(self)
        tk.Label(view_win_root, text=name).pack()
        for obj in student_list:
            if obj.name == btn.cget("text"):
                btn_dict = {}
                path_list = []
                for i in range(len(obj.submissions)):
                    btn_dict[i] = Button2(view_win_root)
                for i, imag in enumerate(obj.submissions):
                    try:
                        filepath = f"{_dir}/{imag}"
                        img = Image.open(filepath)
                        path_list.append(img.fp.name)
                        new_img = img.resize((100, 100), Image.ANTIALIAS)
                        newest_img = ImageTk.PhotoImage(new_img)
                        setattr(btn_dict.get(i), "photo", newest_img)
                        # setattr(btn_dict.get(i), "filep", filepath)
                        btn_dict.get(i).configure(image=newest_img,
                                                  command=lambda i=i: self.delete(path_list[i], btn_dict.get(i),
                                                                                  view_win_root, student_list))
                        # btn_dict.get(i).path = filepath  # assign to class variable to resolve issue
                        btn_dict.get(i).pack()
                    except:
                        continue

    def delete(self, path_list, btn: Button2, root, stu_list):
        # print(f'Filepath of photo deleted: {btn_fp}')
        print(f'List of recorded button image filepaths: {path_list}')
        try:
            shutil.move(path_list, deleted_files)
            for student in stu_list:
                for sub in student.submissions:
                    if sub == path_list.split("/")[-1]:
                        print(f'Deleted: {path_list.split("/")[-1]}')
                        student.submissions.pop(student.submissions.index(sub))
                        print(student.submissions)
            btn.destroy()
            btn.update()
            root.update()

        except shutil.Error:
            print(f"File: {path_list} already deleted")

    def save(self, ass_name, stu_list, _dir):
        pdf = FPDF()
        while pdf.page_no() == 0:
            print("0 pages add title page")
            pdf.add_page()
            pdf.set_font("times", "B", 45)
            pdf.write(10, f"Assignment: {ass_name}\nDate: {date.today()}")
        for student in stu_list:
            for sub in student.submissions:
                pdf.add_page()
                pdf.set_font("times")
                pdf.write(10, f"Student:\n{student.name}")
                pdf.image(f"{_dir}/{sub}", w=50, h=50, link=f"{_dir}/{sub}")
        pdf.output(f"{ass_name}.pdf")

        self.create_warning(f"PDF for {ass_name} has been created")

    @staticmethod
    def create_warning(msg):
        create_warn = tk.Toplevel()
        create_warn.grab_set()  # Disables other windows while warning is shown
        create_warn.wm_title("WARNING")
        create_warn.geometry("225x60+910+400")
        warn_text = tk.Label(create_warn, text=msg, font=("Arial", 14))
        warn_text.pack()
        ok_btn = tk.Button(create_warn, text="Ok", command=create_warn.destroy)
        ok_btn.pack()


# intro = SetupWin()
# mw = MainPage("C:/Users/Chi/Desktop/test_img", "test")
