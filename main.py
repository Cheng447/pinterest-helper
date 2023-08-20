import tkinter as tk
from tkinter import filedialog
import os
import requests

class pinterest_helper(tk.Tk):
    def __init__(self):

        super().__init__()

        '''
        GUI settings
        '''

        self.title('pinterest_helper(for download picture)')
        self.geometry("400x300+700+300")
        self.iconbitmap('download_icon_128877.ico')
        self.resizable(False,False)
        self.configure(background='#1e191c')

        self.sv=tk.StringVar()
        self.sv.set("enter your path")

        self.entry1=tk.Entry(self,width=25,textvariable=self.sv)
        self.entry1.pack(pady=(60,0))

        self.open_button=tk.Button(self, text="open file",command=self.open_file_manager,bd=3)
        self.open_button.pack(pady=15)

        self.entry2=tk.Entry(self,width=25)
        self.entry2.pack()

        self.download_button=tk.Button(self,text="download",bd=3)
        self.download_button.pack(pady=15)

        
    def open_file_manager(self):
        selected_path = filedialog.askdirectory()
        if selected_path:
            self.sv.set(f"{selected_path}")

    def download(self):
        ...

ph=pinterest_helper()

if __name__=="__main__":
    ph.mainloop()