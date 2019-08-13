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
    def cart_display(self):
        with open("Add_to_cart.json", "r") as File:
            self.data1 = json.load(File)
        print(self.data["Menu"])                  # Print the Menu
        t = input("Enter u r choice:")              # Ask for choice
        # self.s1,self.s3,self.s5,self.s7="","","",""
        # self.s2,self.s4,self.s6,self.s8=0,0,0,0
        self.d = dict()
        while (t != "Exit"):                # until user write Exit
            self.s1=""
            self.s2=0
            if(t in self.data):             # If choice of user is in data eg. Roti
                print(self.data[t])         # print data. submenu of Roti.

                t1 = input(t + " type:")    # Ask type of that data eg. if user write 1. so itmeans Plain roti
                self.s1=self.s1+self.data[t][t1] # Write the name of data. eg. self.data["Roti"]["1"]=Plain

                t2=input("Quantity of " + t+" :")
                self.s2=self.s2+int(t2)

                self.data1[self.s1] = self.s2  # Add data in Dictionarty eg. Plain:2
                print(self.data["Menu"])
                t = input("Enter u r choice:")




        if (t == "Exit"):
            with open("Add_to_cart.json","w") as File1:
                json.dump(self.data1,File1)

obj=Cart()
#obj.Read_file()
#obj.cart_display()



