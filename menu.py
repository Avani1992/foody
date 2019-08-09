import os
import sys
import json

a={"1":"GulabJamun","2":"Ice-Cream","3":"Lassi","4":"Rasgulla"}
class Menu:
       with open("foody1.json","r") as File1:
          data=json.load(File1)
       with open("foody1.json", "w") as File:
          data["Dessert"] = a
          json.dump(data, File)


       #print(data)
       #File1.close()
       def menu_display(self):
           print(Menu.data["Menu"])
           t=input("Enter u r selection:")



           while(t!="Exit"):

              if(t=="1"):
               print(Menu.data["Roti"])

               # t1=input("Roti type:")
               # t2=input("Quantity of Roti:")
               t = input("Enter your selection:")
              elif (t == "2"):
               print(Menu.data["Sabji"])

               # t1 = input("Sabjitype:")
               # t2 = input("Quantity of Sabji:")
               t = input("Enter your selection:")
              elif (t == "3"):
               print(Menu.data["Salad"])

               # t1 = input("Salad type:")
               # t2 = input("Quantity of Salad:")
               t = input("Enter your selection:")
              elif (t == "4"):
               print(Menu.data["South-Indian"])
               # t1 = input("Dish type:")
               # t2 = input("Quantity of Dish:")
               t = input("Enter your selection:")





obj=Menu()

