import tkinter as tk
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')



class MainWindow(tk.Tk):

    '''Main Window GUI. Students and their 
    associated assignment submissions are aggregated'''

    def __init__(self, dir: str, assignment_name: str):
        tk.Tk.__init__(self)

        # Window setup
        self.geometry("650x700+910+400")
        self.title("Main Window")
        self.dir = dir
        self.assignment_name = assignment_name
        
        # Setup watchdog observer to monitor changes in the directory specified in setup window
        event_handler = LoggingEventHandler()
        observer = Observer()
        observer.schedule(event_handler, self.dir, recursive=True)
        observer.start()

        # GUI frames for app layout
        self.left_frame = tk.Frame(self)
        self.right_frame = tk.Frame(self)
        self.middle_frame = tk.Frame(self)
        self.left_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.right_frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        self.middle_frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        
        self.input_frame = tk.Frame(self.left_frame, pady=20, bg="blue")
        self.input_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=False)
        self.assignment_label = tk.Label(self.input_frame, text=self.assignment_name)
        self.assignment_label.pack()

        self.mainloop()

MainWindow("C:/Users/Chi/Desktop/test_img", "test assignment 1")

    
