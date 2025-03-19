import sqlite3
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListWidget,QPushButton
from  PyQt5.QtGui import QIcon
class Ecommerce(QWidget):
    def __init__(self):
        super().__init__()
        self.setDesign()

    def setDesign(self):
        self.setWindowTitle("My Ecommerce")
        self.setWindowIcon(QIcon("attachment_145482488.jpg"))
        self.setGeometry(300, 250, 700, 700)
        #For creating a list
        self.vl=QVBoxLayout()
        self.product_list=QListWidget()
        self.vl.addWidget(self.product_list)

        #For adding cart button
        self.add_to_cart=QPushButton("Add Cart")
        self.add_to_cart.clicked.connect(self.add_cart)
        self.vl.addWidget(self.add_to_cart)

        #For view cart button
        self.view_to_cart=QPushButton("View Cart")
        self.view_to_cart.clicked.connect(self.view_cart)
        self.vl.addWidget(self.view_to_cart)
        self.load_product()
        self.setLayout(self.vl)


    def load_product(self):
        conn=sqlite3.connect("myproject.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM Products")
        products=cur.fetchall()
        conn.close()
        self.product_list.clear()

        for product in products:
            self.product_list.addItem(f"{product[0]}-{product[1]}-{product[2]}-Rs.{product[3]:.2f}-{product[4]}")

    def add_cart(self):
        pass

    def view_cart(self):
        pass





if __name__=="__main__":
    a=QApplication(sys.argv)
    w=Ecommerce()
    w.show()
    sys.exit(a.exec_())