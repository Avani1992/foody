import os
import sys
import json
from Payment import *

class Order:
    def order_display(self,a):
      if(a[2]=="display"):
        with open("Order.json","r")as File:
            self.data=json.load(File)
        File.close()

        while(self.data):
            print("U r order is Confirmed..")
            print("U r order code is: ",self.data)
            print("It takes some processing time..")
            print("Thank you..")
            self.d=dict()
            with open("Add_to_cart.json","w") as File:       # When the order is confirmed delete all the data from Add_to_cart.json.
                json.dump(self.d,File)
            break
        else:
            print("Pls pay the bill First...")
    def cancelorder(self,a):
        if(a[2]=="cancelorder"):
            print("U r order is cancelled..")