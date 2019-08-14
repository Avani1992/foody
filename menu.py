import os
import sys
import json



class Menu:
        def Read_file(self):
           with open("foody1.json","r") as File1:    # read the json file
             self.data=json.load(File1)              # store data of json file in self.data which is in dictionary form.
             #print(self.data)
        def update_data(self,a):                    # update the data(enter new item) only admin do these.
            if(a[1]=="update"):                     # check if update is passed from CLI
                obj=Menu()
                obj.Read_file()                       # read the json file for data
                obj.Write_file(sys.argv)            # call the Write_file for enter the new data
        def Write_file(self,a):
            with open("foody1.json", "w") as File:  # open foody1.json as write mode so we can write new data
               self.s=dict()
               self.l2=list()
               self.s1=dict()
               for i in range (0,len(self.data["Menu"])):
                  self.l2.append(self.data["Menu"][i]) # store item name in list from Menu key.
               #print("L2 is: ",self.l2)

               self.l1=a[3].split(",")              # split the value using ',' which is passed threw CLI

               for i in range(0,len(self.l1)):
                  self.s[i+1]= self.l1[i]           # store the value in key:value pair in dict form.
               self.data[a[2]]=self.s               # give the key name which is passed from CLI in second possition  and assign value.
               self.length=len(self.data["Menu"])
               if(a[2] not  in  self.data["Menu"]): # check key is present in Menu or not.
                   self.l2.append(a[2])           # If key is not in Menu append it in Menu.
               self.data["Menu"]=self.l2
               print("Menu Updated...Check it in foody1.json...")



               json.dump(self.data, File)           # dump the data into json file for newly enter data. so json file is updated with new data.

        def delete_data(self,a):                    # Delete the item from Menu.
            if(a[1]=="delete"):                     # check if delete is passed from CLI
                obj=Menu()
                obj.Read_file()                     # call the Read_file function.

                if(a[2] in self.data):              # check that Passed data from CLI in 2 position is present in stored data .
                    del self.data[a[2]]             # if it present in stored data delete it from that dictionary.
                    #print(self.data)
                if (a[2]  in self.data["Menu"]):    # check if passed data in Menu list
                     self.data["Menu"].remove(a[2]) # If it is in Menu remove it from Menu list.
                with open("foody1.json", "w") as File:# open the json file again in write mode
                  json.dump(self.data,File)             # dump the updated data in json file. so now deleted item is not in dictionary.
                print("Item Deleted...check it in foody1.json..")

        def menu_display(self):                         # Display the menu and submenu.
           print("Welcome to the Menu.py...")
           print("-------------------------------")
           print("Menu: ",self.data["Menu"])                     # display Main Menu.
           print("Write 'Exit' for back to Main Menu")
           t=input("Enter Main Item name:")              # Take input from user from CLI..

           while(t!="Exit"):                            # check until user enter Exit.
               if(t in self.data):                      # check entered value from user is present in stored data.
                  print(t+" Type:" ,self.data[t])                   # If it is display that data which is submenu.
                  print("--------------------------------------------------------------------------------")
                  print("Menu: ", self.data["Menu"])  # display Main Menu.
                  print("Write 'Exit' for back to Main Menu")
                  t = input("Enter Main Item name:")
               else:
                   print("Enter Wrong Item name..")
                   t = input("Enter Main Item name:")

           while(t=="Exit"):
               print("---------------------------------------------")
               print("Pls Write 'Cart select' to place the order..")
               print("----------------------------------------------")
               break

obj=Menu()
obj.Read_file()
#obj.menu_display()
#obj.Write_file(sys.argv)

obj.update_data(sys.argv)
obj.delete_data(sys.argv)
#obj.menu_display()


