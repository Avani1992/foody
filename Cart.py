import os
import sys
import json

class Cart:
    def Read_file(self):
        with open("foody1.json", "r") as File1:
            self.data = json.load(File1)
            # print(self.data)

    #print(data)
    # File1.close()
    def select(self,a):   # To place the order..
      if(a[2]=="select"):
        with open("Add_to_cart.json", "r") as File:
            self.data1 = json.load(File)
        print("Welcome to Cart.py...")
        print("------------------------")
        print("Menu: ",self.data["Menu"])                  # Print the Menu
        print("Write 'Exit'' for back to main menu...")
        t = input("Enter Item name:")              # Ask for choice

        self.d = dict()
        while (t != "Exit"):                # until user write Exit
            self.s1=""
            self.s2=0
            if(t in self.data):             # If choice of user is in data eg. Roti
                print(t+" Types: ",self.data[t])         # print data. submenu of Roti.

                t1 = input(t + " type(e.g : write Key for Item):")    # Ask type of that data eg. if user write 1. so itmeans Plain roti
                self.s1=self.s1+self.data[t][t1] # Write the name of data. eg. self.data["Roti"]["1"]=Plain

                t2=input("Quantity of " + t+" :")
                self.s2=self.s2+int(t2)

                self.data1[self.s1] = self.s2  # Add data in Dictionarty eg. Plain:2
                print("----------------------------------------")
                print("Menu: ",self.data["Menu"])
                print("Write 'Exit'' for back to main menu...")
                t = input("Enter Item name:")

        if (t == "Exit"):
            with open("Add_to_cart.json","w") as File1:
                json.dump(self.data1,File1)
            print("---------------------------------------------")
            print("Pls Write 'Cart display' to see the order..")
            print("----------------------------------------------")
    def cart_display(self,a):           # to display the order which is place by the user...
        if(a[2]=="display"):
          with open("Add_to_cart.json","r") as file1:
            self.data=json.load(file1)
        print("U r order: ")
        print("------------ ")
        for i,j in self.data.items():
              print(i,j)

        print("---------------------------------------------")
        print("Pls Write 'Payment displaybill' to see  the TotalBill..")
        print("----------------------------------------------")

obj=Cart()
#obj.Read_file()
#obj.cart_display()



