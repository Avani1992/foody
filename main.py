import os
import sys

from menu import *
from Order import *
from Payment import *
from Cart import *

class main:

    def display_menu(self,a):
        if(a[1]=="Menu"):                  # If user write 1 goto the  Menu class.
            obj1 = Menu()
            obj1.Read_file()
            obj1.menu_display()
        elif(a[1]=="Cart"):                 # If user write 2 goto the cart class.
            obj2=Cart()
            obj2.Read_file()
            obj2.select(sys.argv)
            obj2.cart_display(sys.argv)
        elif(a[1]=="Payment"):                # If user write 3 goto the Payment class.
            obj1=Payment()
            obj1.Read_file()
            obj1.payment_display(sys.argv)
            obj1.updateorder(sys.argv)
            obj1.Bill_pay(sys.argv)
        elif (a[1] == "Order"):             # If user write 4 goto the Oreder class.
            obj1 = Order()
            obj1.order_display(sys.argv)
            obj1.cancelorder(sys.argv)

obj=main()

obj.display_menu(sys.argv)


