from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title('Hospital Management System')
        self.root.geometry('1540x800+0+0')
        self.NameOftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberOfTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffects=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedications=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()



        lbtitile=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbtitile.pack(side=TOP,fill=X)
        #"===========================Data Frame==============="
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)

        #"===========================button Frame==============="
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

#"===========================Details Frame==============="
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        #"===========================Data Frame Left==============="

        lblNameTable=Label(DataframeLeft,text="Name of The Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTable.grid(row=0,column=0)

        comNameTable=ttk.Combobox(DataframeLeft,textvariable=self.NameOftablets,state="readonly",font=("times new roman",12,"bold"),width=33)

        comNameTable["values"]=("Nice","Corono Vaccine","Acetminophen","Adderall","Amlodine","Ativan")
        
        comNameTable.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Referance No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtref.grid(row=1,column=1)
        
        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNoofTables=Label(DataframeLeft,font=("arial",12,"bold"),text="No of Tablets:",padx=2,pady=4)
        lblNoofTables.grid(row=3,column=0,sticky=W)
        txtNoofTables=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtNoofTables.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=4)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtLot.grid(row=4,column=1)

        lblissuedate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue date:",padx=2,pady=4)
        lblissuedate.grid(row=5,column=0,sticky=W)
        lblissuedate=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblissuedate.grid(row=5,column=1)

        lblExpdate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp date:",padx=2,pady=4)
        lblExpdate.grid(row=6,column=0,sticky=W)
        lblExpdate=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblExpdate.grid(row=6,column=1)

        lblDailydose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailydose.grid(row=7,column=0,sticky=W)
        lblDailydose=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblDailydose.grid(row=7,column=1)

        lblSideeffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=4)
        lblSideeffect.grid(row=8,column=0,sticky=W)
        lblSideeffect=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblSideeffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2,pady=4)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        lblFurtherinfo=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblFurtherinfo.grid(row=0,column=3)

        lblBloodpressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=4)
        lblBloodpressure.grid(row=1,column=2,sticky=W)
        lblBloodpressure=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblBloodpressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage:",padx=2,pady=4)
        lblStorage.grid(row=2,column=2,sticky=W)
        lblStorage=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="Medicine:",padx=2,pady=4)
        lblMedicine.grid(row=3,column=2,sticky=W)
        lblMedicine=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblMedicine.grid(row=3,column=3)

        lblPatientid=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient id:",padx=2,pady=4)
        lblPatientid.grid(row=4,column=2,sticky=W)
        lblPatientid=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblPatientid.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="NhsNumber:",padx=2,pady=4)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        lblNhsNumber=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=4)
        lblPatientName.grid(row=6,column=2,sticky=W)
        lblPatientName=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblPatientName.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=4)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        lblDateOfBirth=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=4)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        lblPatientAddress=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblPatientAddress.grid(row=8,column=3)

        #"==========Data Frame Right==============="
        self.txtprescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtprescription.grid(row=0,column=0)

        #"==============Buttons================"
        btnprescription=Button(Buttonframe,text="Prescription",bg="Green",fg="White",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnprescription.grid(row=0,column=0)

        btnprescriptionData=Button(Buttonframe,text="Prescription Data",bg="Green",fg="White",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnprescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,text="Update",bg="Green",fg="White",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",bg="Green",fg="White",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text="Clear",bg="Green",fg="White",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",bg="Green",fg="White",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        #==================Scrollbar============================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)

        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameOfTable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=
                                         scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=BOTTOM,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameOfTable",text="Name of the Table")
        self.hospital_table.heading("ref",text="Referance Number.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of the Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issuedate")
        self.hospital_table.heading("expdate",text="Expdate")
        self.hospital_table.heading("dailydose",text="Dailydose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        
        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameOfTable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()

#"==========================Functionality Declaration"
    def iprescription(self):
        if self.NameOftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="Dinesh",password='Dinesh@123',db="hospital",port=3306)
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"),(self.NameOftablets.get(),self.ref.get(),
                                                                                                 self.Dose.get(),self.NumberOfTablets.get(),self.Lot.get(),
                                                                                                 self.Issuedate.get(),self.ExpDate.get(),self.DailyDose.get(),
                                                                                                 self.sideEffects.get(),self.FurtherInformation.get(),
                                                                                                 self.StorageAdvice.get(),self.DrivingUsingMachine,get(),
                                                                                                 self.HowToUseMedications.get(),self.PatientId.get(),
                                                                                                 self.nhsNumber.get(),self.PatientName.get(),self.DateOfBirth.get(),
                                                                                                 self.PatientAddress.get())
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been Inserted")
    def update(self):
        conn=mysql.connector.connect(host="localhost",user="Dinesh",password='Dinesh@123',db="dinesh",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("Update hospital set NameOftablets=%s,ref=%s,Dose=%s,NumberOfTablets=%s,Lot=%s,Issuedate=%s,ExpDate=%s,DailyDose=%s,Storage=%s,NHS Number=%s,Patient Name =%s,Date of Birth=%s,Patient Address=%s")
        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",user="Dinesh",password='Dinesh@123',db="dinesh",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.delete(*self.hospital_table.get_children()))
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.NameOftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])








root=Tk()
ob=Hospital(root)
root.mainloop()
