'''
Created on Dec 24, 2020

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
    app =  InputSer(root)
    root.mainloop()
class InputSer:
    
    
    def __init__(self,master):
        self.master = master
        self.master.title("Cyber Dragon // Add product to stock")
        self.master.geometry('1000x650+0+0')
        self.master.config(bg='#f9bde5')
        self.frame = Frame(self.master, bg ='#f9bde5')
        self.frame.pack()
        
        self.Username = StringVar
        self.Password = StringVar
        
        headingFrame1 = Frame(self.frame,bg='#f9bde5', bd=5)
        headingFrame1.grid(row=0,column=0,pady=30)
        headingLabel = Label(headingFrame1, text="Welcome to Cyber Dragon",font = ('Courier',35,'bold'),bg = '#f9bde5',fg ='black')
        headingLabel.grid(row=0,column=0,pady = 0)
        headingLabel2 = Label(headingFrame1, text="The relentless Pursuit of Perfection",font = ('Courier',15,'bold'),bg = '#f9bde5',fg ='black')
        headingLabel2.grid(row=1,column=0)
#         
        
        #==============================================================
        self.SubFrame1 = LabelFrame(self.frame, width=1350,font=('arial',20,'bold'),relief='ridge',bg='#e870d1',bd=10)
        self.SubFrame1.grid(row=2,column=0)
          
        self.SubFrame2 = LabelFrame(self.frame, width=1000,font=('arial',20,'bold'),relief='ridge',bg='yellow',bd=5)
        self.SubFrame2.grid(row=3,column=0, pady = 10)
        #=========================Label and  Entry ==================
        self.lblTitle = Label(self.SubFrame1, text = 'Add product to stock',font = ('arial',30,'bold'),fg ='white',bg='#e870d1',bd=20)
        self.lblTitle.grid(row =0,column = 1)
        
        self.lblId = Label(self.SubFrame1,text ="id :",font = ('arial',20,'bold'),bd=22,bg = '#e870d1',fg = 'black')
        self.lblId.grid(row=1,column =0)
        self.txtId = Entry(self.SubFrame1,font =('arial',20,'bold'),textvariable=self.Username)
        self.txtId.grid(row=1,column =1)
#         
        self.lblQuantity = Label(self.SubFrame1,text ="Quantity :",font = ('arial',20,'bold'),bd=22,bg = '#e870d1',fg = 'black')
        self.lblQuantity.grid(row=2,column =0)
        self.lblNone = Label(self.SubFrame1,text ="",font = ('arial',20,'bold'),bd=22,bg = '#e870d1',fg = 'black')
        self.lblNone.grid(row=3,column =0,pady = 0)
        
        self.txtQuantity = Entry(self.SubFrame1,font =('arial',20,'bold'),textvariable=self.Password)
        self.txtQuantity.grid(row=2,column =1)
        
        self.lblNone = Label(self.SubFrame1,text ="",font = ('arial',20,'bold'),bd=22,bg = '#e870d1',fg = 'Cornsilk')
        self.lblNone.grid(row=2,column =2,padx=40)
        #------Checkbox show/hiden pasword--------
#         self.Check = Checkbutton(self.LoginFrame1,text="show",bg = 'cadet blue',activebackground='cadet blue',command=self.showi())
#         self.Check.grid(row=2,column=2,padx=40)
        #================================Buttons=============================
          
  
        
        self.btnLogin = Button(self.SubFrame2 , text = 'Submit',font = ('arial',13,'bold') , width = 15,cursor='hand2',fg = 'black',bg = '#27f709',activebackground= '#37b525', command = self.addNum)
        self.btnLogin.grid(row=3,column =0)
        self.btnExit = Button(self.SubFrame2 , text = 'Exit',font = ('arial',13,'bold') , width = 15,cursor='hand2',fg = 'black',bg = '#05bde0',activebackground= '#01a4c3', command = self.iExit)
        self.btnExit.grid(row=3,column =2) 
#         self.btnReset = Button(self.LoginFrame2 , text = 'Reset',font = ('arial',13,'bold') , width = 15)
#         self.btnReset.grid(row=3,column =1)
          
        
        #================================Buttons=============================
#     def showi(self):
#         self.txtPassword=Entry(self.LoginFrame1,font =('arial',20,'bold'))
#
    def iExit(self):
        self.master.destroy()    
    def addNum(self):
        
        id = str(self.txtId.get())
        quan = str(self.txtQuantity.get())

        if ( id =='' or quan ==''):
            messagebox.showerror("Error","Invalid login, please try again")
        mypass = "root"
        mydatabase="db"
        
        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="root",
          password="",
          database = "netdata"
        )
        
        mycursor = mydb.cursor()
        sql1 = "SELECT `soluong` FROM `service` WHERE `idDV`= "+id
        print(sql1)
        mycursor.execute(sql1)
        result = mycursor.fetchall()
        print(result)
        if(result == []):
            messagebox.showerror("Error","Invalid login, please try again")
        else:
            quantity=int(quan)
            for i in result:
                quantity+=i[0]
            sql = "UPDATE `service` SET `soluong`="+str(quantity)+" WHERE `idDV`="+id
            print(sql)
            try:
                mycursor.execute(sql)
                mydb.commit()
                messagebox.showinfo("OK","Update successful !")
            except:
                messagebox.showerror("Error","Invalid login, please try again")
            
        
        
        
#        
#         for row in result:
#             if(row[3] == str(password)):
#                 self.newWindow = Toplevel(self.master)
# #                 self.app = main_net(self.newWindow)
#             else:
#                 messagebox.showerror("Error","Invalid login, please try again")    
                
    def new_window(self):
        self.newWindow = Toplevel(self.master)
#         self.app = main_net(self.newWindow)
                     
        
if  __name__== '__main__' :
    main()
  
      
        
        
        
        
        
        
        
        
        
        
        
        
        

