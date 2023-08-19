import tkinter as tk
from tkinter import filedialog
import os
import requests

class pinterest_helper(tk.Tk):
    def __init__(self):

        super().__init__()
        self.title('pinterest_helper(for download picture)')
        self.geometry("400x300+700+300")
        self.iconbitmap('download_icon_128877.ico')
        self.resizable(False,False)
        self.configure(background='#1e191c')
        self.open_button=tk.Button(self, text="open file",command=self.open_file_manager)
        self.open_button.pack(padx=20, pady=20)
        
    def open_file_manager(self):
        selected_path = filedialog.askdirectory()
        if selected_path:
            print("Selected Path:", selected_path)

ph=pinterest_helper()
if __name__=="__main__":
    ph.mainloop()








