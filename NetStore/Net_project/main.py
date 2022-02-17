
'''
Created on Dec 21, 2020

@author: Tham Dinh
'''
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import random
import time
import datetime
from doctest import master
from tkinter import Toplevel
from click.decorators import command
from Net_project.login  import *
from Net_project.service_store import *
from Net_project.listComputer import *
from Net_project.customer_login import *
def main():
    root = Tk()
    app = main_net(root)
    root.mainloop()
    
            
class main_net(tkinter.Tk):
      # Create Canvas 
    def __init__(self,master):
        self.master = master
        self.master.title("Cyber Dragon")
        self.master.geometry('1000x650+0+0')
        self.master.config(bg='#ffba83')
        self.frame = Frame(self.master, bg ='#ffba83')
        self.frame.pack()
        
        ######################################################
        # Take n greater than 0.25 and less than 5
        
        
        ########################################################
        
        headingFrame1 = Frame(self.frame,bg='#ffba83', bd=30)
        headingFrame1.grid(row=0,column=0,pady=40)
        headingLabel = Label(headingFrame1, text="Welcome to Cyber Dragon",font = ('Courier',40,'bold'),bg = '#ffba83',fg ='black',bd = 10)
        headingLabel.grid(row=0,column=0,pady = 0)
        headingLabel2 = Label(headingFrame1, text='"The relentless Pursuit of Perfection"',font = ('Courier',20,'bold'),bg = '#ffba83',fg ='black')
        headingLabel2.grid(row=1,column=0)
#         
         
        #==============================================================
        self.LoginFrame1 = LabelFrame(self.frame, width=1350,font=('arial',20,'bold'),bg ='#ffba83',bd = 0)
        self.LoginFrame1.grid(row=2,column=0)
#            
        #================================Buttons=============================
           
   
         
        self.btnLogin = Button(self.LoginFrame1 , text = 'List Computer',font = ('arial',17,'bold') , width = 15,cursor='hand2',bg='#27f709',bd = 15,command=self.goListComputer)
        self.btnLogin.grid(row=0,column =0,pady = 10)
        
        self.btnLogin = Button(self.LoginFrame1 , text = 'Service Store',font = ('arial',17,'bold') , width = 15,cursor='hand2',bg='#27f709',bd=15,command = self.goService)
        self.btnLogin.grid(row=1,column =0,pady = 10)
        
        self.btnExit = Button(self.LoginFrame1 , text = 'Logout',font = ('arial',17,'bold') , width = 15, cursor='hand2',bg='#27f709',bd=15, command = self.iExit)
        self.btnExit.grid(row=2,column =0,pady=10)
        #================================Buttons=============================
        #show/hiden pasword
#     def showi(self):
#         self.txtPassword=Entry(self.LoginFrame1,font =('arial',20,'bold'))
    
    def iExit(self):
#         self.master.destroy()
        self.newWindow = Toplevel(self.master)
        self.app = login(self.newWindow)
            
    def Login_System(self):
        u = (self.Username.get())
        p = (self.Password.get())    
    def goListComputer(self):
        self.newWindow = Toplevel(self.master)
        self.app = list_Computer(self.newWindow)
    def goService(self):
        self.newWindow = Toplevel(self.master)
        self.app = service(self.newWindow)
                     
         
if  __name__== '__main__' :
    main()
  
      
        
        
        
        
        
        
        
        
        
        
        
        
        

