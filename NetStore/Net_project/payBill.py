'''
Created on Dec 27, 2020

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



from Net_project.main import *
from Net_project.customer_login import *
from Net_project.InputNewSer import *
from Net_project.InputService import *
from Net_project.payBill import *
from Net_project.service_store import *
from Net_project.listComputer import *
from Net_project.login import *

from Net_project.listComputer import *

def main():
    root = Tk()
    app = Bill(root)
    root.mainloop()
    
            
class Bill(tkinter.Tk):
      # Create Canvas 
    def __init__(self,master):
        self.master = master
        self.master.title("Cyber Dragon // Pay Bill")
        self.master.geometry('1000x650+0+0')
        self.master.config(bg='#c8d2dc')

        self.canvas = Canvas(self.master, background="#c8d2dc")
        self.vsb = Scrollbar(self.master, orient="vertical", command=self.canvas.yview)

        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.frame = Frame(self.canvas, bg ='#c8d2dc')
        self.frame.pack()

        self.canvas.create_window((140, 0), window=self.frame, anchor="nw",
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

        ######################################################
        
        headingFrame1 = Frame(self.frame,bg='#c8d2dc')
        headingFrame1.grid(row=0,column=0,pady=10)
        headingLabel = Label(headingFrame1, text="Welcome to Cyber Dragon",font = ('Courier',30,'bold'),bg = '#c8d2dc',fg ='black',bd = 10)
        headingLabel.grid(row=0,column=0,pady = 0)
        headingLabel2 = Label(headingFrame1, text='"The relentless Pursuit of Perfection"',font = ('Courier',15,'bold'),bg = '#c8d2dc',fg ='black')
        headingLabel2.grid(row=1,column=0)
        ######################################################33
        self.idLabel = LabelFrame(self.frame)
        self.idLabel.grid(row=1, column=0,pady=10)
        self.idCp = StringVar(self.idLabel, '')
        self.lblId = Label(self.idLabel, text="Id : ", font=('arial', 15, 'bold'), bg='#e870d1', fg='black')
        self.lblId.grid(row=0, column=0)
        self.txtIdCoPay = Entry(self.idLabel, font=('arial', 15, 'bold'), textvariable=self.idCp, width=5)
        self.txtIdCoPay.grid(row=0, column=2)
        ####___________________________________####!!!!!!!!!!!!!
        self.subFrame2 = LabelFrame(self.frame, width=1000, font=('arial', 20, 'bold'), relief='ridge', bg='yellow',
                                    bd=5)
        self.subFrame2.grid(row=2, column=0, pady=30)
        self.btnLogin = Button(self.subFrame2, text='Submit', font=('arial', 13, 'bold'), width=15, cursor='hand2',
                               fg='black', bg='#27f709', activebackground='#37b525',command=self.payCus)
        self.btnLogin.grid(row=3, column=0)
        self.btnExit = Button(self.subFrame2, text='Exit', font=('arial', 13, 'bold'), width=15, cursor='hand2',
                              fg='black', bg='#05bde0', activebackground='#01a4c3', command=self.iExit)
        self.btnExit.grid(row=3, column=2)

        def pickId(self):
            id = self.txtIdPay.get()
            global mydb, mycursor
            mypass = "root"
            mydatabase = "db"

            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="netdata"
            )
            mycursor = mydb.cursor()

            sql1 = "SELECT * FROM `bill` WHERE `bill`.`id_computer`='"+id+"' AND `bill`.`paid` IS NULL"
            idBi = ''
            try:
                mycursor.execute(sql1)
                result = mycursor.fetchall()
                idBi = str(result[0][0])
                print(idBi)
                # sql2 =
            except:
                messagebox.showerror("Error", "Invalid, please try again!!!")




        ########################################################
    def payCus(self):



        # ----!!---!!!----!!!!!-----------!!!!!!!!!!!!
        self.subFrame1 = LabelFrame(self.frame, font=('arial', 20, 'bold'), bg='#ffba83', bd=10)
        self.subFrame1.grid(row=2, column=0)

        self.subFrame2 = LabelFrame(self.frame, font=('arial', 20, 'bold'), relief='ridge', bg='yellow', bd=5)
        self.subFrame2.grid(row=3, column=0, pady=30)
        # ================================Buttons=============================
        self.nameFrame = Label(self.subFrame1, text='        CYBER DRAGON BILL', font=('Courier', 15, 'bold'),
                               bg='#ffba83', fg='black')
        self.nameFrame.grid(row=0, column=1)
        self.tName = StringVar(self.subFrame1, '')
        self.nameFrame = Label(self.subFrame1, text='      Customer : ', font=('Courier', 15, 'bold'), bg='#ffba83',
                               fg='black')
        self.nameFrame.grid(row=1, column=1)
        self.nameFrame2 = Label(self.subFrame1, text='',textvariable=self.tName, font=('Courier', 15, 'bold'), bg='#ffba83',
                               fg='black')
        self.nameFrame2.grid(row=1, column=2)

        self.tStart = StringVar(self.subFrame1, '')
        self.tEnd = StringVar(self.subFrame1, '')
        self.ttotalTime = StringVar(self.idLabel, '')
        self.tim1 = Label(self.subFrame1, text='Start time : ',  bd=0, font=('Times New Roman', 13),
                          bg='#ffba83',
                          fg='black')
        self.tim1.grid(row=2, column=0)
        self.tim1a = Label(self.subFrame1, text='13h00 Saturday,Dec 26,2020 ',textvariable=self.tStart, bd=0, font=('Times New Roman', 13),
                           bg='#ffba83', fg='black')
        self.tim1a.grid(row=2, column=1)
        self.tim2 = Label(self.subFrame1, text='End time : ', bd=0, font=('Times New Roman', 13), bg='#ffba83',
                          fg='black')
        self.tim2.grid(row=3, column=0)
        self.tim2a = Label(self.subFrame1, text='16h45 Saturday,Dec 26,2020 ',textvariable=self.tEnd, bd=0, font=('Times New Roman', 13),
                           bg='#ffba83', fg='black')
        self.tim2a.grid(row=3, column=1)

        self.tim3 = Label(self.subFrame1, text='Time : ', bd=0, font=('Times New Roman', 13), bg='#ffba83',
                          fg='black')
        self.tim3.grid(row=4, column=0)
        self.tim3a = Label(self.subFrame1, text='3h45',textvariable=self.ttotalTime, bd=0, font=('Times New Roman', 13), bg='#ffba83',
                           fg='black')
        self.tim3a.grid(row=4, column=1)

        self.hea = Label(self.subFrame1, text='Name', bd=0, font=('Times New Roman', 11), bg='#ffba83', fg='black')
        self.hea.grid(row=5, column=0)
        self.hea1 = Label(self.subFrame1, text='Quantity', font=('Times New Roman', 11), bd=0, bg='#ffba83',
                          fg='black')
        self.hea1.grid(row=5, column=1)
        self.hea2 = Label(self.subFrame1, text='Price', bd=0, font=('Times New Roman', 11), bg='#ffba83',
                          fg='black')
        self.hea2.grid(row=5, column=2)
        self.hea3 = Label(self.subFrame1, text='Amount', bd=0, font=('Times New Roman', 11), bg='#ffba83',
                          fg='black')
        self.hea3.grid(row=5, column=3)

        self.cac0 = Label(self.subFrame1, text='---------------------------', bd=0, bg='#ffba83', fg='black')
        self.cac0.grid(row=6, column=0)
        self.cac1 = Label(self.subFrame1, text='--------------------------------------------------------------',
                          bd=0,
                          bg='#ffba83', fg='black')
        self.cac1.grid(row=6, column=1)
        self.cac2 = Label(self.subFrame1, text='---------------------------', bd=0, bg='#ffba83', fg='black')
        self.cac2.grid(row=6, column=2)
        self.cac3 = Label(self.subFrame1, text='---------------------------', bd=0, bg='#ffba83', fg='black')
        self.cac3.grid(row=6, column=3)
        ###!!!!!!________________________!!!!!####

        id = str(self.txtIdCoPay.get())
        global mydb, mycursor, sum3
        sum3 = 0
        name=''
        start=''
        end=''
        totalTime=''
        sum1 = 0
        mypass = "root"
        mydatabase = "db"
        sum1 = 0
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="netdata"
        )
        mycursor = mydb.cursor()
        sql1 = "SELECT `user`.`user_name`, `bill`.* , SEC_TO_TIME(TIME_TO_SEC(`bill`.`end_at`)-TIME_TO_SEC(`bill`.`start_at`)) as time, `service`.`tenDV`,`service_bill`.`soluong_mua`,`service`.`gia`, `service`.`gia` * `service_bill`.`soluong_mua` as tongDV FROM `bill` , `service_bill`,`service` ,`user` WHERE `user`.`id`=`bill`.`id_user` AND `bill`.`id_bill`=`service_bill`.`id_pay`AND `service`.`idDV` = `service_bill`.`id_DV` AND `bill`.`id_computer`='"+id+"' AND `bill`.`paid` IS NULL"
        print(sql1)
        try:
            mycursor.execute(sql1)
            result = mycursor.fetchall()
            name = str(result[0][0])
            start = str(result[0][4])
            end = str(result[0][5])
            totalTime = str(result[0][7])
            self.ttotalTime.set(totalTime)
            self.tEnd.set(end)
            self.tStart.set(start)
            self.tName.set(name)


            print(len(result))
            for i in range(0,len(result)):
                sNa = str(result[i][8])
                sQu = str(result[i][9])
                sPr = str(result[i][10])
                sAm = str(result[i][11])
                self.sName = StringVar(self.subFrame1, '')
                self.sQuan = StringVar(self.subFrame1, '')
                self.sPrice = StringVar(self.subFrame1, '')
                self.sAmount = StringVar(self.subFrame1, '')
                print(sNa,)
                linee = i+8
                self.sName.set(sNa)
                self.sQuan.set(sQu)
                self.sPrice.set(sPr)
                self.sAmount.set(sAm)
                self.hea = Label(self.subFrame1, text='Nước cam ép',textvariable=self.sName, bd=0, font=('Times New Roman', 11), bg='#ffba83',
                                 fg='black')

                self.hea.grid(row=linee, column=0)
                self.hea1 = Label(self.subFrame1, text='2 x',textvariable=self.sQuan, font=('Times New Roman', 11), bd=0, bg='#ffba83',
                                  fg='black')
                self.hea1.grid(row=linee, column=1)
                self.hea2 = Label(self.subFrame1, text='15000',textvariable=self.sPrice, bd=0, font=('Times New Roman', 11), bg='#ffba83',
                                  fg='black')
                self.hea2.grid(row=linee, column=2)
                self.hea3 = Label(self.subFrame1, text='30000',textvariable=self.sAmount, bd=0, font=('Times New Roman', 11), bg='#ffba83',
                                  fg='black')
                self.hea3.grid(row=linee, column=3)
                sum1 += int(result[i][11])
        except:
            messagebox.showerror("Error", "Invalid, please try again!!!")



        ###########################################################
        self.totalSer = StringVar(self.subFrame1, '')
        self.priceTime = StringVar(self.subFrame1, '')
        self.sumPriceTime = StringVar(self.subFrame1, '')
        self.sumEnd = StringVar(self.subFrame1, '')
        self.ttotalTime2 = StringVar(self.subFrame1, '')
        m = 10000
        mi = str(m)

        k = int(totalTime[0:-6]) + int(totalTime[-5:-3]) / 60
        print(totalTime[0:-6])
        print(totalTime[-5:-3])
        tim =str(round(k,2))
        self.ttotalTime2.set(tim)
        sum2 = round(k,2) * m
        self.sumPriceTime.set(sum2)
        self.priceTime.set(mi)
        self.totalSer.set(sum1)

        sum3 = sum1 + sum2
        self.sumEnd.set(sum3)
        #########
        self.cac0 = Label(self.subFrame1, text='---------------------------', bd=0, bg='#ffba83', fg='black')
        self.cac0.grid(row=13, column=0)
        self.cac1 = Label(self.subFrame1, text='--------------------------------------------------------------',
                              bd=0, bg='#ffba83', fg='black')
        self.cac1.grid(row=13, column=1)
        self.cac2 = Label(self.subFrame1, text='---------------------------', bd=0, bg='#ffba83', fg='black')
        self.cac2.grid(row=13, column=2)
        self.cac3 = Label(self.subFrame1, text='---------------------------', bd=0, bg='#ffba83', fg='black')
        self.cac3.grid(row=13, column=3)

        self.cac0 = Label(self.subFrame1, text='Total service', font=('Times New Roman', 11), bd=0, bg='#ffba83',
                          fg='black')
        self.cac0.grid(row=14, column=0)
        self.cac3 = Label(self.subFrame1, text='130000',textvariable=self.totalSer , font=('Times New Roman', 11), bd=0, bg='#ffba83', fg='black')
        self.cac3.grid(row=14, column=3)

        self.hea = Label(self.subFrame1, text='Amount Time', bd=0, font=('Times New Roman', 11), bg='#ffba83',
                         fg='black')
        self.hea.grid(row=15, column=0)
        self.hea1 = Label(self.subFrame1, text='3h45',textvariable=self.ttotalTime2, font=('Times New Roman', 11), bd=0, bg='#ffba83', fg='black')
        self.hea1.grid(row=15, column=1)
        self.hea2 = Label(self.subFrame1, text='15000',textvariable=self.priceTime, bd=0, font=('Times New Roman', 11), bg='#ffba83', fg='black')
        self.hea2.grid(row=15, column=2)
        self.hea3 = Label(self.subFrame1, text='60000',textvariable=self.sumPriceTime, bd=0, font=('Times New Roman', 11), bg='#ffba83', fg='black')
        self.hea3.grid(row=15, column=3)

        self.cac0 = Label(self.subFrame1, text='Total ',font = ('Times New Roman',11),bd=0,bg ='#ffba83',fg ='black')
        self.cac0.grid(row=16, column=0)
        self.cac3 = Label(self.subFrame1, text='200000',textvariable=self.sumEnd, font=('Times New Roman', 11), bd=0, bg='#ffba83', fg='black')
        self.cac3.grid(row=16, column=3)

        self.cac0 = Label(self.subFrame1, text='Discount ', font=('Times New Roman', 11), bd=0, bg='#ffba83',
                          fg='black')
        self.cac0.grid(row=17, column=0)
        self.cac1 = Label(self.subFrame1, text='0% ', font=('Times New Roman', 11), bd=0, bg='#ffba83', fg='black')
        self.cac1.grid(row=17, column=1)
        self.cac1 = Label(self.subFrame1, text='None', font=('Times New Roman', 11), bd=0, bg='#ffba83',
                          fg='black')
        self.cac1.grid(row=17, column=2)
        self.cac3 = Label(self.subFrame1, text='0', font=('Times New Roman', 11), bd=0, bg='#ffba83', fg='black')
        self.cac3.grid(row=17, column=3)

        self.cac0 = Label(self.subFrame1, text='---------------------------', bd=0, bg='#ffba83', fg='black')
        self.cac0.grid(row=18, column=0)
        self.cac1 = Label(self.subFrame1, text='--------------------------------------------------------------', bd=0,
                          bg='#ffba83', fg='black')
        self.cac1.grid(row=18, column=1)
        self.cac2 = Label(self.subFrame1, text='---------------------------', bd=0, bg='#ffba83', fg='black')
        self.cac2.grid(row=18, column=2)
        self.cac3 = Label(self.subFrame1, text='---------------------------', bd=0, bg='#ffba83', fg='black')
        self.cac3.grid(row=18, column=3)

        self.cac0 = Label(self.subFrame1, text='Total ', font=('Times New Roman', 13), bd=0, bg='#ffba83', fg='black')
        self.cac0.grid(row=19, column=0)
        self.cac3 = Label(self.subFrame1, text='200000',textvariable=self.sumEnd, font=('Times New Roman', 13), bd=0, bg='#ffba83', fg='black')
        self.cac3.grid(row=19, column=3)

        self.btnLogin = Button(self.subFrame2, text='Submit', font=('arial', 13, 'bold'), width=15, cursor='hand2',
                               fg='black', bg='#27f709', activebackground='#37b525',command=self.subMit)
        self.btnLogin.grid(row=3, column=0)
        self.btnExit = Button(self.subFrame2, text='Exit', font=('arial', 13, 'bold'), width=15, cursor='hand2',
                              fg='black', bg='#05bde0', activebackground='#01a4c3', command=self.iExit)
        self.btnExit.grid(row=3, column=2)

        
        
        #================================Buttons=============================
        #show/hiden pasword
#     def showi(self):
#         self.txtPassword=Entry(self.LoginFrame1,font =('arial',20,'bold'))
    #########-------thanh scroll----------############
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    ########################################################
    def subMit(self):
        id = str(self.txtIdCoPay.get())
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="netdata"
        )
        mycursor = mydb.cursor()
        sql1 = "UPDATE `bill` SET `paid` = '"+str(sum3)+"' WHERE `bill`.`id_computer` = '"+id+"' AND `bill`.`paid` IS NULL"
        try:
            mycursor.execute(sql1)
            mydb.commit()
            messagebox.showinfo("OK", "Bill payment is successful ! ")
        except:
            messagebox.showerror("Error", "Invalid, please try again!!!")
    def iExit(self):
        self.master.destroy()
#         self.newWindow = Toplevel(self.master)
#         self.app = login(self.newWindow)
            
    
                     
         
if  __name__== '__main__' :
    main()
  
      
        
        
        
        
        
        
        
        
        
        
        
        
        

