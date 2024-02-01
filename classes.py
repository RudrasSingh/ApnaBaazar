from database import *
from tkinter import messagebox as ms
from qrc import genQR

class ItemEntry:

    def __init__(self,pname,pcateg,pcode,sprice,quantity):
        self.name = pname
        self.category = pcateg
        self.pcode = pcode
        self.price = sprice
        self.quantity = quantity

    def add_item(self):
        try:
            sqlInsert(cur.execute("INSERT INTO INVENTORY VALUES(?,?,?,?,?)",(self.pcode,self.name,self.category,self.price,self.quantity)))
            
        except Exception as e:
            ms.showerror("Failed",e)


    def bar_scan(self):
        pass
        #scan and return a value and used by using .set method

    def update_item(self):
        try:
            sqlInsert(cur.execute("UPDATE INVENTORY SET PNAME = ?,PCATEGORY = ?,PSELL = ?,PQUANTITY = ? WHERE PCODE = ?",(self.name,self.category,self.price,self.quantity,self.pcode)))
            ms.showinfo("Successful","Item Updated!")
        except Exception as e:
            ms.showerror("Failed",e)


class ImportGoods:

    def __init__(self,sname,phone,supp_of,quantity,desc_order):
        self.name = sname
        self.phone = phone
        self.supplying = supp_of
        self.quantity =  quantity
        self.order_desc = desc_order

    def set_order(self):
        try:    
            #email sequence
            import smtplib
            by_NAME = sqlAccess(cur.execute("SELECT NAME FROM ADMIN"))[0][0]
            by_PHONE = sqlAccess(cur.execute("SELECT PHONE FROM ADMIN"))[0][0]
            to = sqlAccess(cur.execute("SELECT MAIL FROM SUPPLIER WHERE NAME = ?",(self.name,)))[0][0]
            sqlInsert(cur.execute("INSERT INTO IMPORTING VALUES (?,?,?,?)",(self.name,self.phone,self.supplying,self.quantity)))
            content = f"***ORDER FOR GOODS***\nMr/Ms {self.name} are sending you the details of our order,\n Order Category : {self.supplying}\nOrder Quantity: {self.quantity}\nOrder Description:\n{self.order_desc}\nHope to recicve the order soon!\n{by_NAME}\nFor Query Contact: {by_PHONE}"
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('apnaBazaarpvtltd@gmail.com', 'apnabazaar@')
            server.sendmail('apnaBazaarpvtltd@gmail.com',to, content)
            server.close()
            ms.showinfo("Successful","Order Email has been sent successfully!")
        except Exception as e:
            ms.showinfo("Failed",e)
            print(e)


class Employee:

    def __init__(self,ename,eid,userid,epassword,mail,ephone):
        self.name = ename
        self.eid = eid
        self.userid = userid
        self.password = epassword
        self.mail = mail
        self.phone = ephone

    def add_employee(self):
        try:
            sqlInsert(cur.execute("INSERT INTO EMP VALUES(?,?,?,?,?,?)",(self.userid,self.password,self.name,self.phone,self.mail,self.eid)))
            ms.showinfo("Successful","Employee Added successfully!")
        except Exception as e:
            ms.showinfo("Failed",e)

    def update_employee(self):
        try:
            sqlInsert(cur.execute("UPDATE EMP SET ID = ?,PASSWORD = ?,NAME = ?,PHONE = ?,MAIL = ? WHERE EMPID = ?",(self.userid,self.password,self.name,self.phone,self.mail,self.eid,)))
            ms.showinfo("Successful","Employee Updated Successfully")
        except Exception as e:
            ms.showinfo("Failed",e)


class Administrator:

    def __init__(self,ename,userid,epassword,mail,ephone):
        self.name = ename
        self.userid = userid
        self.password = epassword
        self.mail = mail
        self.phone = ephone

    def add_admin(self):
        try:
            sqlInsert(cur.execute("INSERT INTO ADMIN VALUES(?,?,?,?,?)",(self.userid,self.password,self.name,self.phone,self.mail)))
            print(self.userid,self.password,self.name,self.phone,self.mail)
            ms.showinfo("Successful","Admin added successfully!")
        except Exception as e:
            ms.showinfo("Failed",e)

    def update_admin(self):
        try:
            sqlInsert(cur.execute("UPDATE ADMIN SET ID = ?,PASSWORD = ?,NAME = ?,PHONE = ?,MAIL = ? WHERE ID = ?",(self.userid,self.password,self.name,self.phone,self.mail,self.userid)))
            ms.showinfo("Successful","Data updated successfully!")
        except Exception as e:
            ms.showinfo("Failed",e)
            

class Supplier:
    
    def __init__(self,Sname,supplies,address,phone,mail,default):
        self.name = Sname
        self.supplies = supplies
        self.address = address
        self.phone = phone
        self.mail = mail
        self.default = default

    def add_supplier(self):
        try:
            sqlInsert(cur.execute("INSERT INTO SUPPLIER VALUES(?,?,?,?,?,?)",(self.name,self.supplies,self.address,self.phone,self.mail,self.default)))
            ms.showinfo("Successful","Supplier added successfully!")
        except Exception as e:
            ms.showinfo("Failed",e)

    def update_supplier(self):
        try:
            sqlInsert(cur.execute("UPDATE SUPPLIER SET NAME = ?,SUPP_OF = ?,ADDRESS = ?,PHONE = ?,MAIL = ?,DEFAULT = ? WHERE NAME = ?",(self.name,self.supplies,self.address,self.phone,self.mail,self.default,self.name)))
            ms.showinfo("Successful","Admin updated successfully!")
        except Exception as e:
            ms.showinfo("Failed",e)


class Retail:

    def __init__(self,bill_no,cname,cphone,cmail,bill_data):
        self.bill_no = bill_no
        self.cname = cname
        self.cphone = cphone 
        self.cmail = cmail 
        self.bill_data = bill_data

        
    def mailbill(self):
        try:    
            #email sequence
            import smtplib
            from email.mime.text import MIMEText
            content = f"BILL FOR YOUR PURCHASE\nMr/Ms {self.cname} are sending you your bill,\n\n{self.bill_data}\n\n Thanks For shopping with us! Looking forward to see you soon."
            msg = MIMEText(content)
            sent_from = "apnaBazaarpvtltd@gmail.com"
            passwd = "xxxxxxx"
            sent_to = self.cmail
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(sent_from,passwd)
            server.sendmail(sent_from,sent_to,msg.as_string())
            server.quit()
            ms.showinfo("Successful","Bill-Email has been sent successfully!")
        except Exception as e:
            ms.showinfo("Failed",e)
        
    def whatsapp_bill(self):
        import pywhatkit as pwk
        from datetime import datetime
        phone = '+91'+self.cphone
        hour = int(datetime.now().strftime("%H"))
        minute = int(datetime.now().strftime("%M"))
        message = f"BILL FOR YOUR PURCHASE\nMr/Ms {self.cname} are sending you your bill,\n\n {self.bill_data}\n\n Thanks For shopping with us! Looking forward to see you soon."
        pwk.sendwhatmsg(f'{phone}',message,hour,minute+3,60)






#some functions=============================
def prePurchase(bill_no):

    file = open(f"bill_gen/{bill_no}.txt",'r')
    bill = file.read()
    return bill 



