'''
Created on Dec 21, 2020

@author: Tham Dinh
'''
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime
from doctest import master
from tkinter import Toplevel

from Net_project.main import *
from Net_project.customer_login import *
from Net_project.InputNewSer import *
from Net_project.InputService import *
from Net_project.payBill import *
from Net_project.service_store import *
from Net_project.listComputer import *
from Net_project.login import *

import mysql.connector



def main():
    root = Tk()
    app = login(root)
    root.mainloop()




class login:
    
    
    def __init__(self,master):
        self.master = master
        self.master.title("Cyber Dragon :> Login")
        self.master.geometry('1000x650+0+0')
        self.master.config(bg='#09f1f7')
        self.frame = Frame(self.master, bg ='#09f1f7')
        self.frame.pack()
        
        
        
        headingFrame1 = Frame(self.frame,bg='#09f1f7', bd=5)
        headingFrame1.grid(row=0,column=0,pady=30)
        headingLabel = Label(headingFrame1, text="Welcome to Cyber Dragon",font = ('Courier',35,'bold'),bg = '#09f1f7',fg ='black')
        headingLabel.grid(row=0,column=0,pady = 0)
        headingLabel2 = Label(headingFrame1, text="The relentless Pursuit of Perfection",font = ('Courier',15,'bold'),bg = '#09f1f7',fg ='black')
        headingLabel2.grid(row=1,column=0)
#         
        
        #==============================================================
        self.LoginFrame1 = LabelFrame(self.frame, width=1350,font=('arial',20,'bold'),relief='ridge',bg='#e870d1',bd=10)
        self.LoginFrame1.grid(row=2,column=0)
          
        self.LoginFrame2 = LabelFrame(self.frame, width=1000,font=('arial',20,'bold'),relief='ridge',bg='yellow',bd=5)
        self.LoginFrame2.grid(row=3,column=0, pady = 10)
        #=========================Label and  Entry ==================
        self.Username = StringVar(self.LoginFrame1,'')
        self.Password = StringVar(self.LoginFrame1,'')
        self.lblTitle = Label(self.LoginFrame1, text = 'Login',font = ('arial',30,'bold'),fg ='white',bg='#e870d1',bd=20)
        self.lblTitle.grid(row =0,column = 1)
        
        self.lblUsername = Label(self.LoginFrame1,text ="Username :",font = ('arial',20,'bold'),bd=22,bg = '#e870d1',fg = 'black')
        self.lblUsername.grid(row=1,column =0)
        self.txtUsername = Entry(self.LoginFrame1,font =('arial',20,'bold'),textvariable=self.Username)
        self.txtUsername.grid(row=1,column =1)
#         
        self.lblPassword = Label(self.LoginFrame1,text ="Password :",font = ('arial',20,'bold'),bd=22,bg = '#e870d1',fg = 'black')
        self.lblPassword.grid(row=2,column =0)
        self.lblPassword = Label(self.LoginFrame1,text ="",font = ('arial',20,'bold'),bd=22,bg = '#e870d1',fg = 'black')
        self.lblPassword.grid(row=3,column =0,pady = 0)
        
        self.txtPassword = Entry(self.LoginFrame1,show='*',font =('arial',20,'bold'),textvariable=self.Password)
        self.txtPassword.grid(row=2,column =1)
        
        self.lblPassword = Label(self.LoginFrame1,text ="",font = ('arial',20,'bold'),bd=22,bg = '#e870d1',fg = 'Cornsilk')
        self.lblPassword.grid(row=2,column =2,padx=40)
        #------Checkbox show/hiden pasword--------
        self.var = BooleanVar()
        self.Check = Checkbutton(self.LoginFrame1,text="show",bg = 'cadet blue',activebackground='cadet blue',variable=self.var, command=self.onClick)
        self.Check.grid(row=2,column=2,padx=40)
        #================================Buttons=============================
          
  
        
        self.btnLogin = Button(self.LoginFrame2 , text = 'Login',font = ('arial',13,'bold') , width = 15,cursor='hand2',fg = 'white',bg = '#37b525',activebackground= '#27f709', command = self.Login_System)
        self.btnLogin.grid(row=3,column =0)
          
#         self.btnReset = Button(self.LoginFrame2 , text = 'Reset',font = ('arial',13,'bold') , width = 15)
#         self.btnReset.grid(row=3,column =1)
          
#         self.btnExit = Button(self.LoginFrame2 , text = 'Exit',font = ('arial',13,'bold') , width = 15, command = logout)
#         self.btnExit.grid(row=3,column =2)
        #================================Buttons=============================
#     def showi(self):
#         self.txtPassword=Entry(self.LoginFrame1,font =('arial',20,'bold'))
#    
    def onClick(self):
        self.ic =StringVar(self.LoginFrame1,self.txtPassword.get())
        print(self.ic)
        if self.var.get() == True:
            
            self.txtPassword = Entry(self.LoginFrame1,font =('arial',20,'bold'),textvariable=self.ic)
            self.txtPassword.grid(row=2,column =1)
        else:
            self.txtPassword = Entry(self.LoginFrame1,show='*',font =('arial',20,'bold'),textvariable=self.ic)
            self.txtPassword.grid(row=2,column =1)
            
    def Login_System(self):
        
        account = str(self.txtUsername.get())
        password = str(self.txtPassword.get())
        mypass = "root"
        mydatabase="db"
        
        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="root",
          password="",
          database = "netdata"
        )
        
        mycursor = mydb.cursor()
        sql = "SELECT * FROM `user` WHERE `user`.`user_name` = '"+ account +"'"
        print(sql)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        if(result == []):
            messagebox.showerror("Error","Invalid login, please try again")
        for row in result:
            if(row[3] == str(password)):
#                 self.master.destroy()
                self.newWindow = Toplevel(self.master)
                self.app = main_net(self.newWindow)
                
            else:
                messagebox.showerror("Error","Invalid login, please try again")    
                
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = main_net(self.newWindow)
                     
        
if  __name__== '__main__' :     
    main()
  
      
        
        
        
        
        
        
        
        
        
        
        
        
        

