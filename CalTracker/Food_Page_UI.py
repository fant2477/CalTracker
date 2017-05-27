import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class Food_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.food_page_init()

    def food_page_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Food_page_ui.ui", None)
        self.setCentralWidget(form)

        # set QLineEdit
        self.food_search_textEdit = form.findChild(QLineEdit, "food_search_textEdit")

        #set QPushButton
        self.food_search_bt = form.findChild(QPushButton, "food_search_bt")
        self.food_back_bt = form.findChild(QPushButton, "food_back_bt")
        self.food_add_bt = form.findChild(QPushButton, "food_add_bt")
        self.food_delete_bt = form.findChild(QPushButton, "food_delete_bt")



        ####################
        #connect QPushButton
        self.food_back_bt.clicked.connect(self.back_main)



    def back_main(self):
        self.parent.changePage("Main_Page")

