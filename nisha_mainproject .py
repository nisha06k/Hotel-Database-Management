from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import hotelDatabase
import datetime
import time
from datetime import datetime, timedelta

#Frontend
#================================================================================

class Hotel:

    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management Systems")
        self.root.geometry("1350x630+0+0")
       
        
#=============================Variables===========================================
        MainFrame =Frame(self.root)
        MainFrame.grid()
        
        global hd
        CusID =StringVar()
        Firstname =StringVar()
        Surname =StringVar()
        Age=StringVar()
        DOB =StringVar()
        Gender=StringVar()
        Email=StringVar()
        Mobile=StringVar()
        ProveOfID =StringVar()
        Nationality=StringVar()
        Address =StringVar()
        PostCode =StringVar()
        DateIn=StringVar()
        DateOut=StringVar()
        RoomType=StringVar()
        RoomNo=StringVar()
        Meal=StringVar()
        TotalCost=StringVar()
        SubTotal=StringVar()
        PaidTax=StringVar()
        TotalDays=StringVar()

        
        DateIn.set(time.strftime("%d/%m/%Y")) 
        DateOut.set(time.strftime("%d/%m/%Y"))
        x = random.randint(109, 8746)
        randomRef = str(x)
        CusID.set("Hotel"+ randomRef)



#========================================retreving data from backend================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hotel Management Systems", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return




        
        def addData():
            if(len(CusID.get())!=0):
                hotelDatabase.addHotelRec(CusID.get(), Firstname.get(),  Surname.get(),  Gender.get(), Address.get(), Mobile.get(),
                                     Nationality.get(), DateIn.get(), DateOut.get(), TotalCost.get())
                lstHotel.delete(0,END)            
                lstHotel.insert(END,(CusID.get(), Firstname.get(),  Surname.get(),  Gender.get(), Address.get(), Mobile.get(),
                                     Nationality.get(), DateIn.get(), DateOut.get(), TotalCost.get()))

               

        def DisplayData():
            lstHotel.delete(0,END)
            for row in hotelDatabase.viewData():
                lstHotel.insert(END,row,str(""))

        
        def HotelRec(event):
            global hd
            searchHdb = lstHotel.curselection()[0]
            hd = lstHotel.get(searchHdb )

            self.txtCusID.delete(0,END)
            self.txtCusID.insert(END,hd[1])
            self.txtFirstname.delete(0,END)
            self.txtFirstname.insert(END,hd[2])
            self.txtSurname.delete(0,END)
            self.txtSurname.insert(END,hd[3])
            self.cboGender.delete(0,END)
            self.cboGender.insert(END,hd[4])
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END,hd[5])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,hd[6])            
            self.cboNationality.delete(0,END)
            self.cboNationality.insert(END,hd[7])
            self.txtDateIn.delete(0,END)
            self.txtDateIn.insert(END,hd[8]) 
            self.txtDateOut.delete(0,END)
            self.txtDateOut.insert(END,hd[9])
            self.txtTotalCost.delete(0,END)
            self.txtTotalCost.insert(END,hd[10]) 
            
        
        def Reset():
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            Gender.set("")
            TotalCost.set("")
            Nationality.set("")         
            ProveOfID.set("")
            TotalDays.set("")
            self.txtDOB.delete(0,END)
            self.txtEmail.delete(0,END) 
            self.txtCusID.delete(0,END) 
            self.txtFirstname.delete(0,END)
            self.txtSurname.delete(0,END)
            self.txtAge.delete(0,END)
            self.txtAddress.delete(0,END) 
            self.txtPostCode.delete(0,END)    
            self.txtMobile.delete(0,END)            
            self.txtDateIn.delete(0,END)
            self.txtDateOut.delete(0,END)
            self.txtPaidTax.delete(0,END)
            self.txtSubTotal.delete(0,END)
            self.txtTotalCost.delete(0,END)
            DateIn.set(time.strftime("%d/%m/%Y")) 
            DateOut.set(time.strftime("%d/%m/%Y"))
            x = random.randint(109, 8746)
            randomRef = str(x)
            CusID.set("Hotel"+ randomRef)
 

        def DeleteData():
            if(len(CusID.get())!=0):
                hotelDatabase.deleteRec(hd[0])
                Reset()
                DisplayData()

        def searchDatabase():
            lstHotel.delete(0,END)
            for row in hotelDatabase.searchData(CusID.get(),Firstname.get(),Surname.get(),Gender.get(),Address.get(),Mobile.get(),
                                      Nationality.get(),DateIn.get(),DateOut.get(),TotalCost.get()):
                lstHotel.insert(END,row,str(""))


        def update():
            if(len(CusID.get())!=0):
                hotelDatabase.deleteRec(hd[0])
            if(len(CusID.get())!=0):                
                hotelDatabase.addHotelRec(CusID.get(),Firstname.get(),Surname.get(),Gender.get(),Address.get(),Mobile.get(),
                                      Nationality.get(),DateIn.get(),DateOut.get(),TotalCost.get())           
                lstHotel.delete(0,END)            
                lstHotel.insert(END,(CusID.get(),Firstname.get(),Surname.get(),Gender.get(),Address.get(),Mobile.get(),
                                      Nationality.get(),DateIn.get(),DateOut.get(),TotalCost.get()))

        def TotalCostandAddData():
            addData()

            
            InDate = DateIn.get()
            OutDate = DateOut.get()
            InDate = datetime.strptime(InDate, "%d/%m/%Y")
            OutDate = datetime.strptime(OutDate, "%d/%m/%Y")
            TotalDays.set(abs((OutDate - InDate).days))          
            
            if (Meal.get() == "Breakfast" and RoomType.get()=="AC"):

                q1 =float(17)
                q2 =float(34)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="Rs"+ str('%.2f'%((q5)*0.09))
                ST="Rs"+ str('%.2f'%((q5)))
                TT =  "Rs"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Breakfast" and  RoomType.get() =="NON-AC"):
                
                q1 =float(35)
                q2 =float(43)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="Rs"+ str('%.2f'%((q5)*0.09))
                ST="Rs"+ str('%.2f'%((q5)))
                TT =  "Rs"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
           

            elif (Meal.get() == "Lunch" and  RoomType.get() =="AC"):
                
                q1 =float(29)
                q2 =float(37)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="Rs"+ str('%.2f'%((q5)*0.09))
                ST="Rs"+ str('%.2f'%((q5)))
                TT =  "Rs"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Lunch" and  RoomType.get() =="NON-AC"):
                
                q1 =float(37)
                q2 =float(43)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="Rs"+ str('%.2f'%((q5)*0.09))
                ST="Rs"+ str('%.2f'%((q5)))
                TT =  "Rs"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
           

            elif (Meal.get() == "Dinner" and  RoomType.get() =="AC"):
                
                q1 =float(28)
                q2 =float(37)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="Rs"+ str('%.2f'%((q5)*0.09))
                ST="Rs"+ str('%.2f'%((q5)))
                TT =  "Rs"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "Dinner" and  RoomType.get() =="NON-AC"):
                
                q1 =float(30)
                q2 =float(43)
                q3 =float(TotalDays.get())
                q4 =float(q1 + q2)
                q5 = float(q3 * q4)
                Tax="Rs"+ str('%.2f'%((q5)*0.09))
                ST="Rs"+ str('%.2f'%((q5)))
                TT =  "Rs"+ str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)

            

        #=======================================Top Frame===========================================================

        TopFrame = Frame(MainFrame, bd=10, relief=RIDGE, bg="cadet blue")
        TopFrame.pack(side=TOP,fill=X)

        #=======================================================left frame========================================

        LeftFrame = Frame(TopFrame, bd=5, width=400, height=550, padx=0, relief=RIDGE, bg="powder blue")
        LeftFrame.pack(side=LEFT,fill = X)
        
        
        self.lblCusID =Label(LeftFrame, font=('arial',12,'bold'), text="Customer Ref:", padx=2, bg="powder blue")
        self.lblCusID.grid(row=0,column=0, sticky =W)
        self.txtCusID =Entry(LeftFrame, font=('arial',12,'bold'),textvariable =CusID,width =18)
        self.txtCusID.grid(row=0,column=1,pady=3, padx=20)

        self.lblFirstname =Label(LeftFrame, font=('arial',12,'bold'),text="Firstname:",padx=2, bg="powder blue")
        self.lblFirstname.grid(row=1,column=0, sticky =W)
        self.txtFirstname =Entry(LeftFrame, font=('arial',12,'bold'),textvariable =Firstname,width =18)
        self.txtFirstname.grid(row=1,column=1,pady=3, padx=20)
        

        self.lblSurname =Label(LeftFrame, font=('arial',12,'bold'),text="Surname:",padx=1, bg="powder blue")
        self.lblSurname.grid(row=2,column=0, sticky =W)
        self.txtSurname =Entry(LeftFrame, font=('arial',12,'bold'),textvariable =Surname,width =18)
        self.txtSurname.grid(row=2,column=1,pady=3, padx=20)
        

        self.lblAge =Label(LeftFrame, font=('arial',12,'bold'),text="Age:",padx=1, bg="powder blue")
        self.lblAge.grid(row=3,column=0, sticky =W)
        self.txtAge =Entry(LeftFrame, font=('arial',12,'bold'),textvariable=Age,width =18)
        self.txtAge.grid(row=3,column=1,pady=3, padx=20)



        
        self.lblDOB =Label(LeftFrame, font=('arial', 12,'bold'), text="Date of Birth:",padx=2,pady=2, bg="powder blue")
        self.lblDOB.grid(row=4, column=0,sticky=W)
        self.txtDOB=Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = DOB, width =18)
        self.txtDOB.grid(row=4, column=1, pady=3, padx=20)

        self.lblGender =Label(LeftFrame, font=('arial',12,'bold'),text="Gender:",padx=2,pady=2,bg="powder blue")
        self.lblGender.grid(row=5,column=0, sticky =W)
        self.cboGender =ttk.Combobox(LeftFrame, textvariable=Gender, state='readonly',font=('arial',12,'bold'),width =16)
        self.cboGender['value'] = ('','Male', 'Female', 'other')
        self.cboGender.current(0)
        self.cboGender.grid(row=5,column=1,pady=3,padx=20)


        self.lblEmail =Label(LeftFrame, font=('arial', 12,'bold'), text="Email:",padx=2,pady=2, bg="powder blue")
        self.lblEmail.grid(row=6, column=0,sticky=W)
        self.txtEmail=Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = Email, width =18)
        self.txtEmail.grid(row=6, column=1, pady=3, padx=20)


        self.lblMobile =Label(LeftFrame, font=('arial', 12,'bold'), text="Phone Number:",padx=2,pady=2, bg="powder blue")
        self.lblMobile.grid(row=7, column=0,sticky=W)
        self.txtMobile=Entry(LeftFrame,font=('arial', 12,'bold'),textvariable = Mobile,width =18)
        self.txtMobile.grid(row=7, column=1, pady=3, padx=20)



        self.lblProveOfID =Label(LeftFrame, font=('arial', 12,'bold'),text="ID Proof:",padx=2,pady=2, bg="powder blue")
        self.lblProveOfID .grid(row=8, column=0,sticky=W)
        self.cboProveOfID =ttk.Combobox(LeftFrame,textvariable= ProveOfID, state='readonly', font=('arial', 12,'bold'),width=16)
        self.cboProveOfID['value'] = ('','Aadhaar card', 'Driving Licence', 'Student ID', 'Pain card', 'Passport')
        self.cboProveOfID.current(0)
        self.cboProveOfID.grid(row=8,column=1,pady=3,padx=2)

        self.lblNationality =Label(LeftFrame,font=('arial',12,'bold'),text="Nationality:",padx=2,pady=2, bg="powder blue")
        self.lblNationality .grid(row=9, column=0,sticky=W)
        self.cboNationality =ttk.Combobox(LeftFrame,textvariable= Nationality, state='readonly', font=('arial', 12,'bold'),width=16)                                        
        self.cboNationality['value']=('', 'India','British','Nigeria','Kenya','Iran','Morocco','Canada', 'France','Norway', 'chinna')
        self.cboNationality.current(0)
        self.cboNationality.grid(row=9,column=1,pady=3,padx=2)

        self.lblAddress =Label(LeftFrame, font=('arial',12,'bold'),text="Address:",padx=1,bg="powder blue")
        self.lblAddress.grid(row=10,column=0, sticky =W)
        self.txtAddress =Entry(LeftFrame, font=('arial',12,'bold'),textvariable=Address,width =18)
        self.txtAddress.grid(row=10,column=1,pady=3, padx=20)

        self.lblPostCode =Label(LeftFrame, font=('arial',12,'bold'),text="Pin Code:",padx=1,bg="powder blue")
        self.lblPostCode.grid(row=11,column=0, sticky =W)
        self.txtPostCode =Entry(LeftFrame, font=('arial',12,'bold'),textvariable=PostCode,width =18)
        self.txtPostCode.grid(row=11,column=1,pady=3, padx=20)

    

        self.lblDateIn =Label(LeftFrame,font=('arial', 12,'bold'),text="Check In Date:",padx=1,pady=2, bg="powder blue")                                   
        self.lblDateIn.grid(row=12, column=0,sticky=W)
        self.txtDateIn =Entry(LeftFrame, font=('arial', 12,'bold'),textvariable = DateIn, width =18)
        self.txtDateIn.grid(row=12, column=1, pady=3, padx=20)
        

        self.lblDateOut=Label(LeftFrame,font=('arial',12,'bold'),text="Check Out Date:",padx=1,pady=2, bg="powder blue")                                     
        self.lblDateOut.grid(row=13, column=0,sticky=W)
        self.txtDateOut =Entry(LeftFrame,font=('arial', 12,'bold'),textvariable = DateOut,width =18)
        self.txtDateOut.grid(row=13, column=1, pady=3, padx=20)


        self.lblRoomType=Label(LeftFrame, font=('arial', 12,'bold'), text="Room Type:",padx=2,pady=2, bg="powder blue")
        self.lblRoomType.grid(row=14, column=0,sticky=W)
        self.cboRoomType=ttk.Combobox(LeftFrame,textvariable=RoomType, state='readonly',font=('arial', 12,'bold'), width=16)                                        
        self.cboRoomType['value']=('','AC','NON-AC')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14, column=1, pady=3, padx=2)

        
        self.lblRoomNo =Label(LeftFrame, font=('arial', 12,'bold'), text="Room No:",padx=2,pady=2, bg="powder blue")
        self.lblRoomNo.grid(row=15, column=0,sticky=W)
        self.cboRoomNo=ttk.Combobox(LeftFrame,textvariable=RoomNo, state='readonly',font=('arial', 12,'bold'), width=16)                                        
        self.cboRoomNo['value']=('','101','102','103','104','105','106', '107', '108', '109', '1010', '201','202','203','204','205','206', '207', '208', '209', '2010')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=15, column=1, pady=3, padx=2)

        self.lblMeal =Label(LeftFrame, font=('arial', 12,'bold'), text="Meal:",padx=1,pady=2, bg="powder blue")
        self.lblMeal.grid(row=16, column=0,sticky=W)
        self.cboMeal=ttk.Combobox(LeftFrame,textvariable=Meal, state='readonly',font=('arial', 12,'bold'), width=16)                                        
        self.cboMeal['value']=('','Breakfast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=16, column=1, pady=3, padx=2)

 #==============================================Right frame ================================================================================================================       
        RightFrame = Frame(TopFrame, bd=5,relief=RIDGE, bg="cadet blue")
        RightFrame.pack(side=RIGHT,fill=X)
       

 #======================================Receipt and Right frame 1=========================================
        RightFrame1 = Frame(RightFrame, bd=5, padx=0,pady=0, relief=RIDGE, bg="cadet blue")
        RightFrame1.grid(row=0,column=0,sticky="w")



        self.lblLabel = Label(RightFrame1, font=('arial', 12, 'bold'),padx=6, pady=10, bg="cadet blue",
        text="Customer Ref\tFirstname\tSurname\tGender\tAddress\tMobile\tNationality\tDateIn\tDateOut\tTotalCost\t")
        self.lblLabel.grid(row = 0, column=0,columnspan=16)


#=========================================right frame 2====================================================
        RightFrame2 = Frame(RightFrame, bd=5, width=800, height=100, padx=3,pady=0, relief=RIDGE,  bg="powder blue")
        RightFrame2.grid(row=1,column=0,sticky="w")

        #==============Scrollbar in right farme 2==================================
        scrollbar = Scrollbar(RightFrame2)              
        scrollbar.grid(row=0, column=1, sticky ='ns')

        lstHotel = Listbox(RightFrame2, width = 105, height=14, font=('arial', 12,'bold'), yscrollcommand=scrollbar.set)
        lstHotel.bind('<<ListboxSelect>>', HotelRec)
        lstHotel.grid(row=0, column=0, padx=0, sticky='nsew')
        scrollbar.config(command = lstHotel.yview)
     
       
 #=========================================Right Frame 3========================================================

       


        RightFrame3 = Frame(RightFrame, bd=5, width=800, height=400, padx=3,pady=0, relief=RIDGE,  bg="cadet blue")
        RightFrame3.grid(row=3,column=0,sticky="w")


        
        self.lblDays= Label(RightFrame3,font=('arial', 14,'bold'), text="No. of Days:", bd=7, fg="black", bg="cadet blue",)
        self.lblDays.grid(row=0,column=0, sticky=W)
        self.txtDays  = Entry(RightFrame3,font=('arial', 14,'bold'), textvariable=TotalDays, bg="White", width=76, justify=LEFT)                               
        self.txtDays.grid(row=0,column=1)

        self.lblPaidTax = Label(RightFrame3,font=('arial', 14,'bold'), text="Paid Tax:", bd=7, fg="black", bg="cadet blue",)
        self.lblPaidTax.grid(row=1,column=0, sticky=W)
        self.txtPaidTax  = Entry(RightFrame3,font=('arial', 14,'bold'), textvariable=PaidTax, bg="White", width=76, justify=LEFT)                               
        self.txtPaidTax.grid(row=1,column=1)

        self.lblSubTotal = Label(RightFrame3,font=('arial', 14,'bold'), text="Sub Total:", bd=7, fg="black", bg="cadet blue",)
        self.lblSubTotal.grid(row=2,column=0, sticky=W)
        self.txtSubTotal= Entry(RightFrame3,font=('arial', 14,'bold'), textvariable=SubTotal, bg="White", width=76, justify=LEFT)                                  
        self.txtSubTotal.grid(row=2,column=1)

        self.lblTotalCost = Label(RightFrame3,font=('arial', 14,'bold'), text="Total Cost:", fg="black",  bd=7, bg="cadet blue",)
        self.lblTotalCost.grid(row=3,column=0, sticky=W)
        self.txtTotalCost = Entry(RightFrame3,font=('arial', 14,'bold'), textvariable=TotalCost,  bg="White", width=76)                                  
        self.txtTotalCost.grid(row=3,column=1)


   #==========================================Buttom Frame===================================================================================================

        BottomFrame = Frame(MainFrame, bd=10, relief=RIDGE, bg="cadet blue")
        BottomFrame.pack(side=BOTTOM,fill=X)

        
        self.btnTotalandAddData=Button(BottomFrame, pady=1, bd=4, bg="light green", fg="black",font=('arial', 16,'bold'),
            width=13,height=2,text="AddNew/Total ",command=TotalCostandAddData).grid(row=0, column=0,padx=4, pady=1)

        self.btnDisplay=Button(BottomFrame,pady=1, bd=4, bg="light green", fg="black",font=('arial', 16,'bold'),
                            width=13,height=2,text="Display", command=DisplayData).grid(row=0, column=1,padx=4, pady=1)

        self.btnUpdate=Button(BottomFrame,pady=1, bd=4, bg="light green", fg="black",font=('arial', 16,'bold'),
                            width=13,height=2,text="Update",command=update).grid(row=0, column=2,padx=4, pady=1)

        self.btnDelete=Button(BottomFrame,pady=1, bd=4, bg="light green", fg="black",font=('arial', 16,'bold'),
                    width=13,height=2, text="Delete", command=DeleteData).grid(row=0, column=3,padx=4, pady=1)


        self.btnSearch=Button(BottomFrame,pady=1, bd=4, bg="light green", fg="black",font=('arial', 16,'bold'),
                            width=13,height=2,text="Search", command=searchDatabase).grid(row=0, column=5,padx=3, pady=1)

        self.btnReset=Button(BottomFrame,pady=1, bd=4, bg="light green", fg="black",font=('arial', 16,'bold'),
                            width=13,height=2,text="Reset",command=Reset).grid(row=0, column=4,padx=4, pady=1)

        self.btnExit=Button(BottomFrame,pady=1, bd=4, bg="light green", fg="black",font=('arial', 16,'bold'),
                    width=13,height=2, text="Exit", command=iExit).grid(row=0, column=6,padx=4, pady=1)





root = Tk()
application = Hotel (root)
root.mainloop()
