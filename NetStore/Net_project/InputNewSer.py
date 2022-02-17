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
    app = InputNewSer(root)
    root.mainloop()
class InputNewSer:
    
    
    def __init__(self,master):
        self.master = master
        self.master.title("Cyber Dragon // Add New Product to Stock ")
        self.master.geometry('1000x650+0+0')
        self.master.config(bg='#71ff49')
        self.frame = Frame(self.master, bg ='#71ff49')
        self.frame.pack()
        
        
        
        headingFrame1 = Frame(self.frame,bg='#71ff49', bd=5)
        headingFrame1.grid(row=0,column=0,pady=30)
        headingLabel = Label(headingFrame1, text="Welcome to Cyber Dragon",font = ('Courier',35,'bold'),bg = '#71ff49',fg ='black')
        headingLabel.grid(row=0,column=0,pady = 0)
        headingLabel2 = Label(headingFrame1, text="The relentless Pursuit of Perfection",font = ('Courier',15,'bold'),bg = '#71ff49',fg ='black')
        headingLabel2.grid(row=1,column=0)
#         
        
        #==============================================================
        self.SubFrame1 = LabelFrame(self.frame, width=1350,font=('arial',20,'bold'),relief='ridge',bg='#38ff00',bd=10)
        self.SubFrame1.grid(row=2,column=0)
          
        self.SubFrame2 = LabelFrame(self.frame, width=1000,font=('arial',20,'bold'),relief='ridge',bg='yellow',bd=5)
        self.SubFrame2.grid(row=3,column=0, pady = 10)
        #=========================Label and  Entry ==================
        self.lblTitle = Label(self.SubFrame1, text = 'Add New Product to Stock',font = ('arial',20,'bold'),fg ='white',bg='#38ff00',bd=20)
        self.lblTitle.grid(row =0,column = 1)
        
#         self.lblId = Label(self.SubFrame1,text ="id :",font = ('arial',10,'bold'),bg = '#e870d1',fg = 'black')
#         self.lblId.grid(row=1,column =0)
#         self.txtId = Entry(self.SubFrame1,font =('arial',10,'bold'),textvariable=self.Username,width = 25)
#         self.txtId.grid(row=1,column =1)
        
        global iname,iprice,iquan,iimg
        iname = StringVar(self.SubFrame1, value='')
        iprice = StringVar(self.SubFrame1, value='')
        iquan = StringVar(self.SubFrame1, value='')
        iimg = StringVar(self.SubFrame1, value='')
        self.lblName = Label(self.SubFrame1,text ="Name:",font = ('arial',10,'bold'),bd=22,bg = '#38ff00',fg = 'black')
        self.lblName.grid(row=1,column =0)
        self.txtName = Entry(self.SubFrame1,font =('arial',10,'bold'),textvariable=iname,width = 25)
        self.txtName.grid(row=1,column =1)
        
        self.lblPrice = Label(self.SubFrame1,text ="Price :",font = ('arial',10,'bold'),bg = '#38ff00',fg = 'black')
        self.lblPrice.grid(row=2,column =0)
        self.txtPrice = Entry(self.SubFrame1,font =('arial',10,'bold'),textvariable=iprice,width = 25)
        self.txtPrice.grid(row=2,column =1)
        
#         
        self.lblQuantity = Label(self.SubFrame1,text ="Quantity :",font = ('arial',10,'bold'),bd=22,bg = '#38ff00',fg = 'black')
        self.lblQuantity.grid(row=3,column =0)
        self.txtQuantity = Entry(self.SubFrame1,font =('arial',10,'bold'),textvariable=iquan,width = 25)
        self.txtQuantity.grid(row=3,column =1)
        
        self.lblImg = Label(self.SubFrame1,text ="Image :",font = ('arial',10,'bold'),bg = '#38ff00',fg = 'black')
        self.lblImg.grid(row=4,column =0)
        self.txtImg = Entry(self.SubFrame1,font =('arial',10,'bold'),textvariable=iimg,width = 25)
        self.txtImg.grid(row=4,column =1)
        
        self.lblNone = Label(self.SubFrame1,text ="",font = ('arial',10,'bold'),width = 15,bg = '#38ff00',fg = 'black')
        self.lblNone.grid(row=3,column =2,pady = 0)
        self.lblNone = Label(self.SubFrame1,text ="",font = ('arial',10,'bold'),bg = '#38ff00',fg = 'Cornsilk')
        self.lblNone.grid(row=5,column =0,padx=40)
        #------Checkbox show/hiden pasword--------
#         self.Check = Checkbutton(self.LoginFrame1,text="show",bg = 'cadet blue',activebackground='cadet blue',command=self.showi())
#         self.Check.grid(row=2,column=2,padx=40)
        #================================Buttons=============================
          
  
        
        self.btnLogin = Button(self.SubFrame2 , text = 'Submit',font = ('arial',13,'bold') , width = 15,cursor='hand2',fg = 'black',bg = '#df4efd',activebackground= '#cd05f7', command = self.Submit)
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
    def Submit(self):
        name = str(self.txtName.get())
        price = str(self.txtPrice.get())
        quan = str(self.txtQuantity.get())
        img = str(self.txtImg.get())
        
        
        mypass = "root"
        mydatabase="db"
        
        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="root",
          password="",
          database = "netdata"
        )
        
        mycursor = mydb.cursor()
        sql = "INSERT INTO `service` (`idDV`, `tenDV`, `gia`, `soluong`, `img`) VALUES (NULL, '"+name+"', '"+price+"', '"+quan+"', '"+img+"')"
        print(sql)
        
        
        if(name==''or price=='' or quan=='' or img==''):
            messagebox.showerror("Error","Don't leave any fields blank, please try again!")
        else:
            mycursor.execute(sql)
            mydb.commit()
            messagebox.showinfo("OK","Add product  successful !")
            
            iname.set('')
            iprice.set('')
            iquan.set('')
            iimg.set('')
#         except:
#             messagebox.showerror("Error","Invalid login, please try again")
#         result = mycursor.fetchall()
#         if(result == []):
#             messagebox.showerror("Error","Invalid login, please try again")
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
  
      
        
        
        
        
        
        
        
        
        
        
        
        
        

