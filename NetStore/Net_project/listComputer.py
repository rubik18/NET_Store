'''
Created on Dec 26, 2020

@author: Tham Dinh
'''

from tkinter import *
from doctest import master
from tkinter import Toplevel


from Net_project.main import *
from Net_project.customer_login import *
from Net_project.InputNewSer import *
from Net_project.InputService import *
from Net_project.payBill import *
from Net_project.service_store import *
# from Net_project.listComputer import *
from Net_project.login import *

from PIL import Image, ImageTk
import mysql.connector
from pygame import image
from click.decorators import command
from numpy import column_stack



def main():
    global idToPay

    root = Tk()
    app = list_Computer(root)
    root.mainloop()

class list_Computer :
    def __init__(self,master):
        self.master = master
        self.master.title("Cyber Dragon // List Computer")
        self.master.geometry('1000x650+0+0')
        self.master.config(bg='#5ffd97')
        
        ##############################################
        self.canvas = Canvas(self.master,  background="#5ffd97")
        self.vsb = Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side=BOTTOM, fill=BOTH,expand=True)
        #########################################################
        
        
        ########################################################
        self.frame = Frame(self.canvas, bg ='#5ffd97')
        self.frame.place()
        
        #############################################
        self.canvas.create_window((25,0), window=self.frame, anchor="nw", 
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

#         self.populate()
        #################################################
        mbFrame = Frame(self.frame,relief='ridge',bg='#09f1f7')
        mbFrame.place( width=70,height=30)
        self.btnHome = Button(mbFrame , text = 'Home',font = ('Courier',12,'bold') , width = 10,cursor='hand2',fg = 'black',bg = '#37b525',activebackground= '#27f709',activeforeground = '#f91d78',command= self.goHome)
        self.btnHome.place(width = 70, height = 30)
        
        ####################################################
        headingFrame1 = Frame(self.frame,bg='#5ffd97', bd=5)
        headingFrame1.grid(row=0,column=0,pady=40)
        headingLabel = Label(headingFrame1, text="List Computer",font = ('Courier',40,'bold'),bg = '#5ffd97',fg ='black')
        headingLabel.grid(row=0,column=0,pady = 0)
        headingLabel2 = Label(headingFrame1, text="We are here to serve you ",font = ('Courier',20,'bold'),bg = '#5ffd97',fg ='black')
        headingLabel2.grid(row=1,column=0)
        
#        ############---------them may tinh-------############
#         mbFrame = Frame(self.master,relief='ridge',bg='#09f1f7')
#         mbFrame.place(relx=0,rely=0, relwidth=0.14,relheight=0.05)
#         mb=  Menubutton ( mbFrame, text="Input Service",font = ('Courier',11,'bold'), fg='black', cursor = 'hand2',bg = '#f998ea',activebackground= '#1dc9ea',direction=RIGHT)
#         mb.place(x=4.5, y =3)
#         mb.menu =  Menu ( mb, tearoff = 0,font = ('Courier',11,'bold'), fg='black', bg = '#f998ea',activebackground= '#1dc9ea' )
#         mb["menu"] =  mb.menu
#         
#         mayoVar = IntVar()
#         ketchVar = IntVar()
#         
#         mb.menu.add_checkbutton ( label="Old Service",variable=mayoVar,command = self.goInputService)
#         mb.menu.add_checkbutton ( label="New Service",variable=ketchVar, command = self.goInputNewService )
#         ###########################--------------##############################

        self.bodyDad = LabelFrame(self.frame, width=1000,bg ='#5ffd97' ,bd=0)
        self.bodyDad.grid(row =2,column = 0)
        
#         self.bodyDad.config(yscrollcommand = self.scrollbar.set) 
        #######################################################################
        
        global mydb, mycursor

        idToPay='345'
        mypass = "root"
        mydatabase="db"
        
        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="root",
          password="",
          database = "netdata"
        )
        
        mycursor = mydb.cursor()
        sql = "SELECT * FROM `computer`"
#         print(sql)
        try:
            mycursor.execute(sql)
            result = mycursor.fetchall()
#             print(len(result))
#             print(result)
            #######################################################################

            for i in range (0,len(result)):
                m = int(i/5)
                n = i % 5
#                 print(result[i])
                if(result[i][1]==None):
                    self.x = StringVar( value='OFF')
                    self.bodyBox = LabelFrame(self.bodyDad,font=('arial',20,'bold'),bg='cadet blue')
                    self.bodyBox.grid(row=m,column=n,padx=10,pady=10)
                    load = Image.open("/NetStore/Net_project/Img/computee.jpg")
                    render = ImageTk.PhotoImage(load)
                    img = Label(self.bodyBox, image=render,width=150,height =150,bg='white')
                    img.image = render
                    img.grid(row = 0 , column = 0)
            
                    id_PAY=i
                    self.id = StringVar(value='45')
                    self.id.set(result[i][0])
        #             v = StringVar( value='OFF') 
                    self.mb=  Menubutton ( self.bodyBox, text="",textvariable=self.x,image=render,font = ('Courier',11,'bold'), fg='black', cursor = 'hand2',bg = '#ff7ccb',activebackground= '#f998ea',compound = TOP)
                    self.mb.grid(row = 0,column =0)
                    self.mb.menu =  Menu ( self.mb, tearoff = 0,font = ('Courier',11,'bold'), fg='black', bg = '#ff7ccb',activebackground= '#f998ea' )
                    self.mb["menu"] =  self.mb.menu
                     
                    self.num = Label(self.mb,text = '',textvariable=self.id,font = ('arial',15,'bold'),bg='red',fg='white')
                    self.num.place(x = 0, y = 0)
                    
                    self.onVar = BooleanVar()
                    self.offVar = BooleanVar()
                    self.addVar = BooleanVar()
                     
                    self.mb.menu.add_checkbutton ( label="Turn ON",variable=self.onVar,command = self.onComputer)
#                    
                else:
                    self.bodyBox = LabelFrame(self.bodyDad,font=('arial',20,'bold'),bg='cadet blue')
                    self.bodyBox.grid(row=m,column=n,padx=10,pady=10)
                    load = Image.open("Img/computee.jpg")
                    render = ImageTk.PhotoImage(load)
                    img = Label(self.bodyBox, image=render,width=150,height =150,bg='white')
                    img.image = render
                    img.grid(row = 0 , column = 0)
#                     global id_PAY
                    id_PAY=i
                    id = StringVar(value='45')
                    id.set(result[i][0])
                    self.x = StringVar( value='ON') 
                    self.mb=  Menubutton ( self.bodyBox, text="",textvariable=self.x,image=render,font = ('Courier',11,'bold'), fg='black', cursor = 'hand2',activebackground = '#2cfbe8',bg= '#1dc9ea',compound = TOP)
                    self.mb.grid(row = 0,column =0)
                    self.mb.menu =  Menu ( self.mb, tearoff = 0,font = ('Courier',11,'bold'), fg='black', activebackground = '#2cfbe8',bg= '#1dc9ea' )
                    self.mb["menu"] =  self.mb.menu
                     
                    self.num = Label(self.mb,text = '',textvariable=id,font = ('arial',15,'bold'),bg='red',fg='white')
                    self.num.place(x = 0, y = 0)
                    
                    self.onVar = BooleanVar()
                    self.offVar = BooleanVar()
                    self.addVar = BooleanVar()
                     
                    self.mb.menu.add_checkbutton ( label="Turn OFF and PAY",variable=self.onVar,command = self.gopayBill)
#                     self.mb.menu.add_checkbutton ( label="Pay",variable=self.offVar,command = self.payBill)
                    self.mb.menu.add_checkbutton ( label="Add Service",variable=self.addVar,command = self.goAddSer)#, command = self.goAddSer 
            
            ##################################################################
        except:
            messagebox.showerror("Error","Invalid login, please try again")
        print(idToPay)
        ##############################
    def gopayBill(self): 
#         id = self.id.get()
#         sqli = "UPDATE `computer` SET `tinh_trang` = NULL WHERE `computer`.`id` = "+ id
#         print(sqli)
#         try:
#             mycursor.execute(sqli)
#             mydb.commit()
#         except:
#             messagebox.showerror("Error","Invalid login, please try again")     
        self.newWindow = Toplevel(self.master)
        self.app = readId(self.newWindow)
        
    def goHome(self):
        self.newWindow = Toplevel(self.master)
        self.app = main_net(self.newWindow)    
        
    def goInputService(self):
        self.newWindow = Toplevel(self.master)
        self.app = InputSer(self.newWindow)
    def goInputNewService(self):
        self.newWindow = Toplevel(self.master)
        self.app = InputNewSer(self.newWindow)
    
    
    def getIdPay(self):
        global id_PAY
        return id_PAY
    
    def goAddSer(self):
        self.newWindow = Toplevel(self.master)
        self.app = service(self.newWindow) 
#         global id_PAY
#         id_PAY=500 
#         x = self.getIdPay()
#         print(x)
#     def payBill(self):
#         global id_PAY
#         a = id_PAY
#         if val[a].get()=='ON':
#             print(val.get())
#         print(type(v.get()),v.get())
    def onComputer(self):
        self.newWindow = Toplevel(self.master)
        self.app = cus_login(self.newWindow)
        
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))    

class readId(tkinter.Tk):
    def __init__(self,master):
        self.master = master
        self.master.title("Cyber Dragon // Pay Bill")
        self.master.geometry('220x150+300+300')
        self.master.config()
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.SubFrame1 = LabelFrame(self.frame,bd=0)
        self.SubFrame1.grid(row=0,column=0)
          
        self.SubFrame2 = LabelFrame(self.frame,bd=0)
        self.SubFrame2.grid(row=1,column=0, pady = 10)
        
        self.lblUsername = Label(self.SubFrame1,text ="Are you sure  want to\n turn off the computer and Pay?\n Please retype computer id",
                                 font = ('arial',10,'bold'),fg = 'black')
        self.lblUsername.grid(row=0,column =0, pady = 10)
        self.txtId = Entry(self.SubFrame1,font =('arial',15,'bold'),width=17)
        self.txtId.grid(row=1,column =0)
        
        self.btnLogin = Button(self.SubFrame2 , text = 'OK',font = ('arial',10,'bold') ,cursor='hand2',fg = 'black',bg = '#a5a7a9',activebackground= '#c8d2dc',comman = self.submit)
        self.btnLogin.grid(row=0,column =0)
        self.btnLogin = Label(self.SubFrame2 , text = '')
        self.btnLogin.grid(row=0,column =1)
        self.btnExit = Button(self.SubFrame2 , text = 'Cancel',font = ('arial',10,'bold') ,cursor='hand2',fg = 'black',bg = '#a5a7a9',activebackground= '#c8d2dc',command=self.iExit)
        self.btnExit.grid(row=0,column =2)
        
    def iExit(self):
        self.master.destroy()
    def submit(self):
        global mydb, mycursor
        idToPay = str(self.txtId.get())
        # print(idToPay)
        mypass = "root"
        mydatabase="db"
        
        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="root",
          password="",
          database = "netdata"
        )
        
        mycursor = mydb.cursor()
        
        id = str(self.txtId.get())
        sql1 = "UPDATE `computer` SET `tinh_trang` = NULL WHERE `computer`.`id` = "+ id
        sql2 = "UPDATE `bill` SET `end_at` = CURRENT_TIMESTAMP WHERE `bill`.`id_computer` = " +id +" AND `bill`.`paid` IS NULL"
        print(sql1)
        print(sql2)
        try:
            mycursor.execute(sql1)
            mydb.commit()
            
            mycursor.execute(sql2)
            mydb.commit()
            
            self.newWindow = Toplevel(self.master)
            self.app = Bill(self.newWindow)
            
        except:
            messagebox.showerror("Error","Invalid , please try again")
#         if(result == []):
#             self.newWindow = Toplevel(self.master)
#             self.app = Bill(self.newWindow)
#         else:
#             messagebox.showerror("Error","Invalid Id, please try again")
            
        
        
        
if  __name__== '__main__' :
    main()

    
    
    
    
    
    
    
