import qrcode #generating qr code 
import cv2 #reading webcam
from datetime import datetime
import pyzbar.pyzbar as pyzbar #decoding
import time
from tkinter import messagebox
from database import *
from barcode import Code39 #generating barcode


def scanQR():

    if sqlAccess(cur.execute("SELECT * FROM EMP;")) == []:
        messagebox.showerror("DATABASE EMPTY", "No Employee has been registered yet!")
    else:
        # starting the webcam using opencv 
        cap = cv2.VideoCapture(0)
        names=[]
        #function for writing the data

        def enterData(z):
            if z in names:
                pass
            
            else:
                
                flag = 0
                if len(sqlAccess(cur.execute("SELECT * FROM EMP"))) >2:
                    emplid = sqlAccess(cur.execute("SELECT EMPID FROM EMP;"))
                    empid = []
                    for i in range(0,len(emplid)):
                        empid.append(emplid[i][0])
                        
                    if z in empid:
                        flag = 1

                elif z in sqlAccess(cur.execute("SELECT EMPID FROM EMP;"))[0][0]:
                    flag = 2

                     
                if flag == 1 or 2:
                    date = datetime.now().strftime("%d-%m-%Y")
                    t = datetime.now().strftime("%I:%M %p")            
                    names.append(z)
                    print(z)
                    file = open(f"ATTENDANCE/attendance of {date}.txt","a")
                    z = z[2:]
                    z = str(z[:-1])
                    print(z)
                    naam = sqlAccess(cur.execute("SELECT NAME FROM EMP WHERE EMPID = ?",(z,)))[0][0]
                    print(naam)
                    att = f"{naam} on date {date} and time {t} is PRESENT\n\n"
                    file.write(att)
                else:
                    messagebox.showerror("Attendance Failed", "NOT REGISTERED AS EMPLOYEE! CONTACT YOUR ADMIN!")


        #function to check if the data is present or not
        def checkData(data):
            
            data=str(data)    
            if data in names:
                messagebox.showinfo('Info', 'Already Present')
            else:
                #print(f"{str(len(names)+1)}- {data} - PRESENT")
                enterData(data)
        
        while True:
            _, frame = cap.read() 
            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                checkData(obj.data)
                time.sleep(1)
            
            cv2.imshow("**Take Attendance** press C to close", frame)

            #closing the program when s is pressed
            if cv2.waitKey(1)& 0xFF == ord('c'):
                cv2.destroyAllWindows()
                break
     
    
def genQR(id,file):
    img = qrcode.make(f"{id}")
    img.save(f'id_gen//{file}.jpg')


def scanBar():
    # starting the webcam using opencv 
    cap = cv2.VideoCapture(0)
    barcodes=[]

    def enterData(z):
        if z in barcodes:
            pass
        else:
            z = str(z)
            #print(z)
            z = z[2:]
            z = int(z[:-2])
            barcodes.append(z)
            #print(barcodes)

    #function to check if the data is present or not
    def checkData(data):
        
        data=str(data)    
        if data in barcodes:
            pass
        else:
            enterData(data)
    
    while True:
        _, frame = cap.read() 
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            checkData(obj.data)
            time.sleep(1)
        
        cv2.imshow("**Scan Barcode** Press C to close", frame)

        #closing the program when c is pressed
        if cv2.waitKey(1)& 0xFF == ord('c'):
            cv2.destroyAllWindows()
            break
    return barcodes[0]


def genBar(code,product_name):
    from barcode.writer import ImageWriter
    my_code = Code39(code,writer= ImageWriter())
    my_code.save(f"barcodes/{product_name}")


if __name__=="__main__":
    pass
