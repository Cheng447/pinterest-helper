import tkinter as tk
from tkinter import filedialog
import os
import wget
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path='C:/Users/b3689/Downloads/edgedriver_win64/msedgedriver.exe'
service = Service(executable_path="path")
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service,options=options,keep_alive=True)
driver.get("https://www.pinterest.co.kr/")

class pinterest_helper(tk.Tk):
    def __init__(self):

        self.picture:list[str]=[] 

        super().__init__()

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

        self.label1=tk.Label(self,text='account',fg='#a3a7cc',bg='#1e191c',font=('Arial',10,'bold'))
        self.label1.place(x=60,y=35)
        
        self.label2=tk.Label(self,text='password',fg='#a3a7cc',bg='#1e191c',font=('Arial',10,'bold'))
        self.label2.place(x=56,y=60)
        
        self.entry1=tk.Entry(self,width=25)
        self.entry1.place(x=125,y=35)

        self.entry2=tk.Entry(self,width=25)
        self.entry2.place(x=125,y=60)

        self.login_botton=tk.Button(self,text='login',bd=3,command=self.login)
        self.login_botton.place(x=192,y=87)

        self.entry3=tk.Entry(self,width=25,textvariable=self.sv)
        self.entry3.place(x=125,y=120)

        self.open_button=tk.Button(self, text="open file",bd=3,command=self.open_file_manager)
        self.open_button.place(x=185,y=150)

        self.entry4=tk.Entry(self,width=25,textvariable=self.sv2)
        self.entry4.place(x=125,y=190)

        self.download_button=tk.Button(self,text="download",bd=3,command=self.download)
        self.download_button.place(x=185,y=220)

        self.swipes=tk.Label(self,text='picture(s)',fg='#a3a7cc',bg='#1e191c',font=('Arial',10,'bold'))
        self.swipes.place(x=68,y=260)
        
        self.entry5=tk.Entry(self,width=25)
        self.entry5.place(x=130,y=260)

    def open_file_manager(self):
        selected_path = filedialog.askdirectory()
        if selected_path:
            self.sv.set(f"{selected_path}")

    def download(self):
        count=0
        teb=self.entry4.get()
        search=driver.find_element(By.XPATH,'//input[@type="text"]') 
        search.send_keys(f'{teb}')
        search.send_keys(Keys.RETURN)
        WebDriverWait(driver,2).until(
            EC.presence_of_all_elements_located((By.XPATH,'//img[@class="hCL kVc L4E MIw"]'))
        )
        for _ in range(0,10):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(1)
        images=driver.find_elements(By.XPATH,'//img[@class="hCL kVc L4E MIw"]')
        path=self.entry3.get()
        os.mkdir(f'{path}/{self.entry4.get()}')
        
        for image in images[0:int(self.entry5.get())]:
            sava_as=os.path.join(f"{path}/{self.entry4.get()}",teb+str(count)+'.jpg')
            wget.download(image.get_attribute("src"),sava_as)
            count+=1

    def login(self):
        search=driver.find_element(By.XPATH,'//button[@type="button"]')
        time.sleep(2)
        search.send_keys(Keys.RETURN)
        account=self.entry1.get()
        password=self.entry2.get()
        account_login= driver.find_element(By.XPATH,'//input[@id="email"]')
        password_login= driver.find_element(By.XPATH,'//input[@id="password"]')
        account_login.send_keys(f'{account}')
        password_login.send_keys(f'{password}')
        login_button=driver.find_element(By.XPATH,'//button[@type="submit"]')
        login_button.send_keys(Keys.RETURN)

ph=pinterest_helper()

if __name__=="__main__":
    ph.mainloop()
