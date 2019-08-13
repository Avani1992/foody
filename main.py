import os
import sys

from menu import *
from Order import *
from Payment import *
from Cart import *

class main:

    def display_menu(self,a):
        if(a[1]=="1"):                  # If user write 1 goto the  Menu class.
            obj1 = Menu()
            obj1.Read_file()
            obj1.menu_display()
        elif(a[1]=="2"):                 # If user write 2 goto the cart class.
            obj2=Cart()
            obj2.Read_file()
            obj2.cart_display()
        elif(a[1]=="3"):                # If user write 3 goto the Payment class.
            obj1=Payment()
            obj1.Read_file()
            obj1.payment_display()
        elif (a[1] == "4"):             # If user write 4 goto the Oreder class.
            obj1 = Order()
            obj1.order_display()

obj=main()

obj.display_menu(sys.argv)


