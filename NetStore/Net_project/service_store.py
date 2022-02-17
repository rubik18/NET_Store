'''
Created on Dec 24, 2020

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
from Net_project.listComputer import *
from Net_project.login import *

from PIL import Image, ImageTk
import mysql.connector
from pygame import image

def main():
    root = Tk()
    app = service(root)
    root.mainloop()
class service :
    def __init__(self,master):
        self.master = master
        self.master.title("Cyber Dragon // Servise Store")
        self.master.geometry('1000x650+0+0')
        self.master.config(bg='#e1f72d')
        ############################
        self.canvas = Canvas(self.master,  background="#e1f72d")
        self.vsb = Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side=BOTTOM, fill=BOTH,expand=True)
        ###########################
        self.frame = Frame(self.canvas, bg ='#e1f72d')
        self.frame.pack()
        ########################
        self.canvas.create_window((40,0), window=self.frame, anchor="nw", 
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
        #####################
        headingFrame1 = Frame(self.frame,bg='#e1f72d', bd=5)
        headingFrame1.grid(row=0,column=0,pady=20)
        headingLabel = Label(headingFrame1, text="Servise Store",font = ('Courier',40,'bold'),bg = '#e1f72d',fg ='black')
        headingLabel.grid(row=0,column=0,pady = 0)
        headingLabel2 = Label(headingFrame1, text="We are here to serve you ",font = ('Courier',20,'bold'),bg = '#e1f72d',fg ='black')
        headingLabel2.grid(row=1,column=0)
        
#         btn1 = Button(self.master,text="Nháº­p hÃ ng",font = ('Courier',11,'bold'), fg='#ca0e1f',relief=RAISED,bd = 7, cursor = 'hand2' )
#         btn1.place(relx=0,rely=0, relwidth=0.1,relheight=0.05)
        #-----------------#
        mbFrame = Frame(self.master,relief='ridge',bg='#09f1f7')
        mbFrame.place( width=220,height=30)
        self.btnHome = Button(mbFrame , text = 'Home',font = ('Courier',12,'bold') , width = 10,cursor='hand2',fg = 'black',bg = '#37b525',activebackground= '#27f709',activeforeground = '#f91d78',command= self.new_window)
        self.btnHome.place(width = 70, height = 30)
        #----------------#
        self.idLabel = LabelFrame(self.frame)
        self.idLabel.grid(row=1,column = 0)
        self.idC = StringVar(self.idLabel,'')
        self.lblId = Label(self.idLabel,text ="Id Computer ",font = ('Courier',15),bg = '#e870d1',fg = 'black')
        self.lblId.grid(row=0,column =0)
        self.txtIdCo = Entry(self.idLabel,font =('arial',15,'bold'),textvariable=self.idC,width = 5)
        self.txtIdCo.grid(row=0,column =2)
        
        mb=  Menubutton ( mbFrame, text="Add to stock",relief=RIDGE,font = ('Courier',12,'bold'), fg='black', cursor = 'hand2',bg = '#37b525',activeforeground = '#f91d78',activebackground= '#27f709',direction=RIGHT)
        mb.place(x=70,width = 150, height = 30)
        mb.menu =  Menu ( mb, tearoff = 0,font = ('Courier',11,'bold'), fg='black', bg = '#f998ea',activebackground= '#1dc9ea', cursor = 'hand2' )
        mb["menu"] =  mb.menu
        
        mayoVar = IntVar()
        ketchVar = IntVar()
        
        mb.menu.add_checkbutton ( label="Old Service",command = self.goInputService)
        mb.menu.add_checkbutton ( label="New Service",variable=ketchVar, command = self.goInputNewService )
        
        self.bodyDad = LabelFrame(self.frame, width=1350,bg ='#e1f72d' ,bd=0)
        self.bodyDad.grid(row =2,column = 0)
        ################################
        global mydb, mycursor
        
        mypass = "root"
        mydatabase="db"
        
        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="root",
          password="",
          database = "netdata"
        )
        
        mycursor = mydb.cursor()
        sql = "SELECT * FROM `service`"
#         print(sql)
        
        global list1, lenn,list1a,list2
        list1 = []
        list1a = []
        list2 = []
        
        print(list1)
        
        try:
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print(len(result))
#             print(result)
            lenn = len(result)
            
            for i in range(0,len(result)):
                m = int(i/5)
                n = i % 5
                list2.append(str(result[i][0]))
                
                self.bodyBox = LabelFrame(self.bodyDad,font=('arial',20,'bold'),bg='cadet blue')
                self.bodyBox.grid(row=m,column=n,padx=10,pady=10)
                load = Image.open(result[i][4])
                render = ImageTk.PhotoImage(load)
                img = Label(self.bodyBox, image=render,width=150,height =150,bg='white')
                img.image = render
                img.grid(row = 0 , column = 0)
                
                global aLine1, aPrice, aQuan, aImg
                aLine1 = StringVar(self.bodyBox, value='')
                 
                aPrice = StringVar(self.bodyBox, value='')
                aQuan = StringVar(self.bodyBox, value='')
                aImg = StringVar(self.bodyBox, value='')
                
                m = str(result[i][2])
                isPri = m[0:-3]+'.'+m[-3:]+'đ'
                 
                a = str(result[i][0])+"," +str(result[i][1])
                aPrice.set(isPri  )
                aLine1.set(a[:20])
                aQuan.set( result[i][3] )
                self.num = Label(img,text='',textvariable = aQuan,font = ('arial',15,'bold'),bg = '#0affdd')
                self.num.place(x = 0, y = 0)
                self.boxx = Label(self.bodyBox,text='',textvariable=aLine1,width=17,font = ('arial',10,'bold'),bg = 'cadet blue',fg = 'Cornsilk')
                self.boxx.grid(row=1,column =0)
                self.boxx = Label(self.bodyBox,text ='', textvariable=aPrice,font = ('arial',10,'bold'),bg = 'cadet blue',fg = 'Cornsilk')
                self.boxx.grid(row=2,column =0)
                
                self.nav = LabelFrame(self.bodyBox,bg='cadet blue',bd=0)
                self.nav.grid(row=3,column=0)
                
#                 global count
                self.count = StringVar(self.nav,value='')
#                 print(type(count)) 
                list1a.append(self.count)
                self.inp = Entry(self.nav,textvariable=self.count,font = ('Courier',10,'bold'),justify=CENTER,width = 5,bd=0,bg = 'white',fg='black')
                self.inp.grid(row=0, column =1,padx = 3)
                list1.append(self.inp)
                ##################
                self.cou = Button(self.nav,text='-',font = ('Courier',10,'bold'),width = 3,bd =0,bg = '#ff9a9a',command = self.decre)
                self.cou.grid(row=0,column=0)
                self.cou2 = Button(self.nav,text='+',font = ('Courier',10,'bold'),width = 3,bd=0,bg = '#ff9a9a',command = self.incre)
                self.cou2.grid(row=0, column =2)
                self.subNone = Label(self.nav,bg ='cadet blue',text='')
                self.subNone.grid(row=0,column=3)
                #########################
#                 self.idC = StringVar(self.nav,value='')
#                 list2a.append(self.idC)
#                 self.idCom = Entry(self.nav,textvariable=self.idC,font = ('Courier',13,'bold'),justify=CENTER,width = 3,bd=0,bg = 'white',fg='red')
#                 self.idCom.grid(row=0, column =0)
#                 list2.append(self.idCom)
                self.submity = Button (self.nav,text = 'Add',font = ('arial',10,'bold') ,cursor='hand2',fg = 'black',bg = '#27f709',activebackground= '#37b525',command = self.addi)
                self.submity.grid(row=0,column=4)
            

        ################################
        except:
            print("error")
        ##############################
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))   
        
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = main_net(self.newWindow)
    ##########--up/down quantity-----########   
    def incre(self):
        input=0
        for i in range(lenn):
            if(list1[i].get()!=''):
                input = str(int(list1[i].get())+1)
                list1a[i].set(input)
#                 print(type(list2[i]),list2[i])
#         print(input)
    def decre(self):

        input=0
        for i in range(lenn):
            if(list1[i].get()!='' and int(list1[i].get())>0):
                input = str(int(list1[i].get())-1)
                list1a[i].set(input)
#         print(input) 
    ###########################################   
    def addi(self):
        idCom = self.txtIdCo.get()
        quan=''
        idSe = ''
        for i in range(lenn):
            if(list1[i].get()!=''):
#                 print(list1[i].get(),list2[i].get())
                quan = list1[i].get()
                idSe = list2[i]
                list1a[i].set('')
#                 list2a[i].set('')
        if(idCom=='' or quan==''or quan=='0' ):
            messagebox.showerror("Error","Don't leave the id blank or the quantity you want to add,\n Please try again!")
        
        mypass = "root"
        mydatabase="db"
          
        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="root",
          password="",
          database = "netdata"
        )
        sql = "SELECT * FROM `bill` WHERE `bill`.`id_computer` = "+idCom+" AND `bill`.`paid` IS NULL"
        print(sql)
        mycursor = mydb.cursor()
        try:
            mycursor.execute(sql)
            re = mycursor.fetchall()
            idBil = str(re[0][0])
            sql1 = "INSERT INTO `service_bill` (`id_pay`, `id_DV`, `soluong_mua`) VALUES ('"+idBil+"', '"+idSe+"', '"+quan+"');"
            print(sql1)
            try:
                mycursor.execute(sql1)
                mydb.commit()
                messagebox.showinfo("OK", "Add Service successfully! ")
            except:
                messagebox.showerror("Error","Add Service failed, please try again")
        except:
            messagebox.showerror("Error","Add Service failed, please try again")
#             
#             
    def goInputService(self):
        self.newWindow = Toplevel(self.master)
        self.app = InputSer(self.newWindow)
    def goInputNewService(self):
        self.newWindow = Toplevel(self.master)
        self.app = InputNewSer(self.newWindow)

#     
#         count.set(input) 
    
    
        

     

if  __name__== '__main__' :
    main()
    
    
    
    
    
    
    
    
    