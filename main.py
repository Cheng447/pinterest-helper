import tkinter as tk
from tkinter import filedialog
import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 

path='C:/Users/b3689/Downloads/edgedriver_win64/msedgedriver.exe'
service = Service(executable_path="path")
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service,options=options,keep_alive=True)
driver.get("https://www.pinterest.co.kr/")
WebDriverWait(driver,10).until(
    lambda x: x.find_element(By.CLASS_NAME,'tBJ dyH iFc sAJ xnr tg7 H2s')
)

login.send_keys(Keys.RETURN)


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

        self.sn='Enter what you want to search'

        self.sv=tk.StringVar()
        self.sv.set("enter your path")

        self.sv2=tk.StringVar()
        self.sv2.set(self.sn)

        self.entry3=tk.Entry(self,width=25,textvariable=self.sv)
        self.entry3.pack(pady=(60,0))

        self.open_button=tk.Button(self, text="open file",command=self.open_file_manager,bd=3)
        self.open_button.pack(pady=15)

        self.entry4=tk.Entry(self,width=25,textvariable=self.sv2)
        self.entry4.pack()

        self.download_button=tk.Button(self,text="download",bd=3,command=self.download)
        self.download_button.pack(pady=15)

        
    def open_file_manager(self):
        selected_path = filedialog.askdirectory()
        if selected_path:
            self.sv.set(f"{selected_path}")

    def download(self):
        tag=self.entry2.get()
        search=driver.find_element(By.XPATH,'searchBoxInput//*[@id="searchBoxContainer"]/div/div/div[2]/input')
        search.send_keys(Keys.RETURN)

    def login(self):
        ...

ph=pinterest_helper()

if __name__=="__main__":
    ph.mainloop()