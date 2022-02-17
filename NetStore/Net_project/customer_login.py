'''
Created on Jan 10, 2021

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
    app = cus_login(root)
    root.mainloop()
class cus_login:
    
    
    def __init__(self,master):
        self.master = master
        self.master.title("Cyber Dragon :> Customer Login")
        self.master.geometry('1000x650+0+0')
        self.master.config(bg='#09f1f7')
        self.frame = Frame(self.master, bg ='#09f1f7')
        self.frame.pack()

        headingFrame1 = Frame(self.frame,bg='#09f1f7', bd=5)
        headingFrame1.grid(row=0,column=0,pady=10)
        headingLabel = Label(headingFrame1, text="Welcome to Cyber Dragon",font = ('Courier',35,'bold'),bg = '#09f1f7',fg ='black')
        headingLabel.grid(row=0,column=0,pady = 0)
        headingLabel2 = Label(headingFrame1, text="The relentless Pursuit of Perfection",font = ('Courier',15,'bold'),bg = '#09f1f7',fg ='black')
        headingLabel2.grid(row=1,column=0)
        
        mbFrame = Frame(self.master,relief='ridge',bg='#09f1f7')
        mbFrame.place(x=0,y=0, width=70,height=30)
        self.btnHome = Button(mbFrame , text = 'Home',font = ('Courier',12,'bold') , width = 10,cursor='hand2',fg = 'black',bg = '#37b525',activebackground= '#27f709',activeforeground = '#f91d78',command= self.goHome)
        self.btnHome.place(width = 70, height = 30)
        
        self.idLabel = LabelFrame(self.frame)
        self.idLabel.grid(row=1,column = 0)
        self.idC = StringVar(self.idLabel,'')
        self.lblId = Label(self.idLabel,text ="Id : ",font = ('arial',15,'bold'),bg = '#e870d1',fg = 'black')
        self.lblId.grid(row=0,column =0)
        self.txtId = Entry(self.idLabel,font =('arial',15,'bold'),textvariable=self.idC,width = 5)
        self.txtId.grid(row=0,column =2)
        #==============================================================
        self.LoginFrame0 = LabelFrame(self.frame, width=1350,font=('arial',20,'bold'),relief='ridge',bg='yellow',bd=5)
        self.LoginFrame0.grid(row=2,column=0,pady = 10)
        #=========================Login or Sign up ==================
        self.btnLogin = Button(self.LoginFrame0 , text = 'Login',font = ('arial',13,'bold') , width = 15,cursor='hand2',fg = 'black',bg = '#27f709',activebackground= '#37b525',command = self.login)
        self.btnLogin.grid(row=1,column =0)
        self.btnExit = Button(self.LoginFrame0 , text = 'Sign up',font = ('arial',13,'bold') , width = 15,cursor='hand2',fg = 'black',bg = '#05bde0',activebackground= '#01a4c3',command = self.sign)
        self.btnExit.grid(row=1,column =2)
        
    ############-------form login-----###################   
    def login(self):  
        
         
        self.LoginFrame1 = LabelFrame(self.frame, width=1350,font=('arial',20,'bold'),relief='ridge',bg='#e870d1',bd=10)
        self.LoginFrame1.grid(row=3,column=0)
        
          
        self.LoginFrame2 = LabelFrame(self.frame, width=1000,font=('arial',20,'bold'),relief='ridge',bg='yellow',bd=5)
        self.LoginFrame2.grid(row=4,column=0, pady = 10)
        
        
        self.Username = StringVar(self.LoginFrame1,'')
        self.Password = StringVar(self.LoginFrame1,'')
        self.lblTitle = Label(self.LoginFrame1, text = 'Customer Login',font = ('arial',30,'bold'),fg ='white',bg='#e870d1',bd=20)
        self.lblTitle.grid(row =0,column = 1)
        
        self.lblUsername = Label(self.LoginFrame1,text ="Username :",font = ('arial',20,'bold'),bd=22,bg = '#e870d1',fg = 'black')
        self.lblUsername.grid(row=1,column =0)
        self.txtUsername = Entry(self.LoginFrame1,font =('arial',20,'bold'),textvariable=self.Username)
        self.txtUsername.grid(row=1,column =1)
#         
        self.lblPassword = Label(self.LoginFrame1,text ="Password :",font = ('arial',20,'bold'),bd=22,bg = '#e870d1',fg = 'black')
        self.lblPassword.grid(row=2,column =0,pady = 10)
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
        
        
        
     #############----------form  Sign up-----###################   
    def sign(self):
        self.LoginFrame1 = LabelFrame(self.frame, width=1350,font=('arial',20,'bold'),relief='ridge',bg='#e870d1',bd=10)
        self.LoginFrame1.grid(row=3,column=0)
          
        self.LoginFrame2 = LabelFrame(self.frame, width=1000,font=('arial',20,'bold'),relief='ridge',bg='yellow',bd=5)
        self.LoginFrame2.grid(row=4,column=0, pady = 10)
        
        self.signUsername = StringVar(self.LoginFrame1,'')
        self.signPassword = StringVar(self.LoginFrame1,'')
        self.signFullname = StringVar(self.LoginFrame1,'')
        self.lblTitle = Label(self.LoginFrame1, text = 'Customer Sign up',font = ('arial',28,'bold'),fg ='white',bg='#e870d1',bd=20)
        self.lblTitle.grid(row =0,column = 1)
        
        self.lblFullname = Label(self.LoginFrame1,text ="Fullname :",font = ('arial',20,'bold'),bd=15,bg = '#e870d1',fg = 'black')
        self.lblFullname.grid(row=1,column =0)
        self.signtxtFullname = Entry(self.LoginFrame1,font =('arial',20,'bold'),textvariable=self.signFullname)
        self.signtxtFullname.grid(row=1,column =1)
        
        self.lblUsername = Label(self.LoginFrame1,text ="Username :",font = ('arial',20,'bold'),bd=15,bg = '#e870d1',fg = 'black')
        self.lblUsername.grid(row=2,column =0)
        self.signtxtUsername = Entry(self.LoginFrame1,font =('arial',20,'bold'),textvariable=self.signUsername)
        self.signtxtUsername.grid(row=2,column =1)
#
        
        
        self.lblPassword = Label(self.LoginFrame1,text ="Password :",font = ('arial',20,'bold'),bd=15,bg = '#e870d1',fg = 'black')
        self.lblPassword.grid(row=3,column =0)
        self.lblPassword = Label(self.LoginFrame1,text ="",font = ('arial',20,'bold'),bd=15,bg = '#e870d1',fg = 'black')
        self.lblPassword.grid(row=4,column =0,pady = 0)
        
        self.signtxtPassword = Entry(self.LoginFrame1,show='*',font =('arial',20,'bold'),textvariable=self.signPassword)
        self.signtxtPassword.grid(row=3,column =1)
#         self.lblPassword = Label(self.LoginFrame1,text ="",font = ('arial',20,'bold'),bd=15,bg = '#e870d1',fg = 'Cornsilk')
#         self.lblPassword.grid(row=3,column =2,padx=40)
        #------Checkbox show/hiden pasword--------
        self.var = BooleanVar()
        self.Check = Checkbutton(self.LoginFrame1,text="show",bg = 'cadet blue',activebackground='cadet blue',variable=self.var, command=self.sign_onClick)
        self.Check.grid(row=3,column=2,padx=40)
        #================================Buttons=============================
        self.btnLogin = Button(self.LoginFrame2 , text = 'Sign up',font = ('arial',13,'bold') , width = 15,cursor='hand2',fg = 'white',bg = '#37b525',activebackground= '#27f709', command = self.Sign_up)
        self.btnLogin.grid(row=3,column =0)
     
        
    #########------show password-----###############
    def onClick(self):
        self.ic =StringVar(self.LoginFrame1,self.txtPassword.get())
        print(self.ic)
        if self.var.get() == True:
            
            self.txtPassword = Entry(self.LoginFrame1,font =('arial',20,'bold'),textvariable=self.ic)
            self.txtPassword.grid(row=2,column =1)
        else:
            self.txtPassword = Entry(self.LoginFrame1,show='*',font =('arial',20,'bold'),textvariable=self.ic)
            self.txtPassword.grid(row=2,column =1)
    
    def sign_onClick(self):
        self.signic =StringVar(self.LoginFrame1,self.signtxtPassword.get())
        print(self.signic)
        if self.var.get() == True:
            
            self.signtxtPassword = Entry(self.LoginFrame1,font =('arial',20,'bold'),textvariable=self.signic)
            self.signtxtPassword.grid(row=3,column =1)
        else:
            self.signtxtPassword = Entry(self.LoginFrame1,show='*',font =('arial',20,'bold'),textvariable=self.signic)
            self.signtxtPassword.grid(row=3,column =1)
    #########------show password-----###############
    
    def Login_System(self):
        
        account = str(self.txtUsername.get())
        password = str(self.txtPassword.get())
        idC = str(self.txtId.get())
        
        mypass = "root"
        mydatabase="db"
        
        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="root",
          password="",
          database = "netdata"
        )
        if(account=='' or password=='' or idC=='' ):
            messagebox.showerror("Error","Don't leave any fields blank, please try again!")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM `user` WHERE user_name = '"+ account +"'"
        print(sql)
        global idUser
        mycursor.execute(sql)
        result = mycursor.fetchall()
        if(result == []):
            messagebox.showerror("Error","Invalid login, please try again")
        for row in result:
            if(row[3] == str(password)):
                idUser = str(row[0])
                #--------turn on computer---------#
                sql2 = "UPDATE `computer` SET `tinh_trang` = '"+idC+"' WHERE `computer`.`id` ="+ idC
                print(sql2)
                mycursor.execute(sql2)
                mydb.commit()
                #--------tao hoa don-----------# 
                sql3 = "INSERT INTO `bill` (`id_bill`, `id_user`, `id_computer`, `start_at`, `end_at`, `paid`) VALUES (NULL, '"+idUser+"', '"+idC+"', current_timestamp(), current_timestamp(), NULL);;"
                print(sql3)
                mycursor.execute(sql3)
                mydb.commit() 
                #-----------quay ve trang list Computer-----#
                self.newWindow = Toplevel(self.master)
                self.app = list_Computer(self.newWindow) 
            else:
                messagebox.showerror("Error","Invalid login, please try again")    
    
    def goHome(self):
        self.newWindow = Toplevel(self.master)
        self.app = main_net(self.newWindow)
                
#     def new_window(self):
#         self.newWindow = Toplevel(self.master)
#         self.app = main_net(self.newWindow)
    def Sign_up(self):   
        name = str(self.signtxtFullname.get())
        account = str(self.signtxtUsername.get())
        password = str(self.signtxtPassword.get())
        
        idCup = str(self.txtId.get())
        
        mypass = "root"
        mydatabase="db"
        
        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="root",
          password="",
          database = "netdata"
        )
        global idUserup
        mycursor = mydb.cursor()
        sql = "INSERT INTO `user` (`id`, `user_name`, `full_name`, `password`, `deleted_at`, `level`, `total_time`) VALUES (NULL, '" + account +"', '"+name+"', '" +password +"',  NULL, NULL, NULL)"
        print(sql)
        if(name==''or account=='' or password=='' or idCup=='' ):
            messagebox.showerror("Error","Don't leave any fields blank, please try again!")
        else:
            mycursor.execute(sql)
            mydb.commit()
            messagebox.showinfo("OK","Sign up account  successful !") 
            #---------turn on computer-------------#
            sql2 = "UPDATE `computer` SET `tinh_trang` = '"+idCup+"' WHERE `computer`.`id` ="+ idCup
            mycursor.execute(sql2)
            mydb.commit()
            #-------------tao hoa don---------------#
            sql3 = "SELECT * FROM `user` WHERE `user`.`user_name` = '" + account +"' and `user`.`full_name` = '"+name+"' and `user`.`password` ='" +password +"'"
            mycursor.execute(sql3)
            re = mycursor.fetchall()
            idUserup = str(re[0][0])
            print (idUserup)
            sql4 = "INSERT INTO `bill`(`id_bill`, `id_user`, `id_computer`, `start_at`, `end_at`, `paid`) VALUES(NULL, '"+idUserup+"', '"+idCup+"', current_timestamp(), current_timestamp(), NULL);"

            print(sql4)
            mycursor.execute(sql4)
            mydb.commit()     
            #-------------quay lai trang list computer-----#
            self.newWindow = Toplevel(self.master)
            self.app = list_Computer(self.newWindow)   
#             self.master.destroy()      
        
if  __name__== '__main__' :
    main()
  
      
        
        
        
        
        
        
        
        
        
        
        
        
        

