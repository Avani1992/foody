import os
import sys
import json
from Cart import *

class Payment:
    def Read_file(self):
        with open("Add_to_cart.json","r") as File:
            self.data=json.load(File)

        #print(self.data)
        File.close()
        with open("foody1.json","r") as File1:
            self.data1=json.load(File1)
        File1.close()
    def payment_display(self,a):
      if(a[2]=="displaybill"):
        print("Welcome to Payment.py..")
        print("---------------------------")
        self.q1,self.sum=0,0
        print("Item" + "      " + " Quantity"+"    "+"Price"+"    "+"Total")
        print("-------------------------------------")
        for i,j in self.data.items():                 # Data Entered by user as their order store in Add_to _cart.json
             for ele in self.data1.values():        # here ele=values of all key of data1.
                    if(type(ele)!=list):            # chect the type of ele. If it is not list then proceed.so check only it in dict. which we want.
                        if(i in ele.values()):      # If user data is in ele's value.
                           self.key=list(ele.keys())             # list of keys for data items eg. for Roti=[1,2,3,4]
                           self.value=list(ele.values())      #  list of values for data items eg. for Roti=[Plain,Naan,etc]

                           self.p1=self.key[self.value.index(i)]       # Find the key from value using index of that value eg. key for Plain roti
                           self.q1=int(j * int(self.p1) * 10)          # Mutliply key with 10.
                           print(i+"      "+str(j)+"         "+str((int(self.p1))*10)+"        "+str(self.q1)  )
                           self.sum=self.sum+self.q1


        print("--------------------------------")
        print("Total Amount is:",self.sum)
        if(self.sum==0):
            print("Pls Place the order")
        else:
         print("For Payment Write 'paybill' ")
         print("For update(Add/Delete) items Write 'updateorder' ")

    def updateorder(self,a):
        if(a[2]=="updateorder"):
            t=input("R u want to change the order(Yes/No): ")
            if(t=="Yes"):
                t1=input("R u want to add some items(Yes/No)?: ")
                if(t1=="Yes"):
                    print("Add items from Cart select")
                    obj=Cart()
                    obj.Read_file()             # If user wants to add item in oreder back to the cart for display menu and add item in cart.
                    obj.select(sys.argv)
                    obj1=Payment()
                    obj1.Read_file()
                    obj1.payment_display(sys.argv)      # After adding item in cart further ask for payment option

                elif(t1=="No"):
                    t1=input("R u want to delete some items(Yes/No)?:")
                    if(t1=="Yes"):
                        with open("Add_to_cart.json", "r") as File:
                            self.data = json.load(File)
                        print(" U r Order:")
                        print("---------------")
                        for i,j in self.data.items():
                            print(i,j)
                        print("------------------------")
                        t2=input("Enter item name which u want to delete:")
                        if(t2 in self.data):            # check if the item is in data which user wants to delete
                            del self.data[t2]       # If it is delete it from data

                        with open("Add_to_cart.json", "w") as File2:        # updata the json file for updated data
                                json.dump(self.data,File2)
                        print(" U r order is Updated.check it in Payment displaybill.. ")


    def Bill_pay(self,a):
     if(a[2]=="paybill"):

        print("Payment Mode:")
        self.d=dict()
        self.d[1]="Paytm"
        self.d[2]="NetBanking"
        self.d[3]="Creditcard"
        self.d[4]="Debitcard"
        print(self.d)
        t=input("Enter Payment Mode:")
        if(t=='1'):
            t=input("Enter u r Paytm four digit code:")
            while(str(len(t))):
             if(str(len(t))==str(4)):
                self.payment="Done"
                self.ordercode="1234"
                print("U r payment is Done..")
                break
             else:
                print("Enter Correct Pin..")
                print("----------------------------")
                t = input("Enter u r Paytm four digit code:")
        elif(t=="2"):
            print("Enter u r NetBanking Details:")
            t=input("Username: ")
            t1=input("Password: ")
            while (str(len(t1))):
             if(str(len(t1))==str(4)):
                self.payment="Done"
                self.ordercode="4567"
                print("U r payment is Done..")
                break
            else:
                print("Enter Correct Password:")
                print("--------------------------")
                t1=input("Password: ")
        elif(t=="3" or t=="4"):
            t=input("Enter Card Details:")
            t=input("enter 3 digit pin:")
            while (str(len(t))):
             if(str(len(t))==str(3)):
                self.payment="Done"
                self.ordercode="6789"
                print("U r payment is Done..")
                break
            else:
                print("Enter Correct Pin..")
                print("-------------------------")
                t=input("Enter 3 digit pin: ")
        while(self.payment=="Done"):
            with open("Order.json","w") as File1:          # Whwn payment is done add ordercode to the json file
                json.dump(self.ordercode,File1)
            File1.close()
            print("-------------------------------------------------------------")
            print("Pls Write 'Order display' to get the confirmation of order..")
            print("--------------------------------------------------------------")
            break




