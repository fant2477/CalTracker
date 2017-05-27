import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from Dia_add_food import *
from Dia_add_exercise import *

class Main_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.mainPageInit()

    def mainPageInit(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/MainPageUI.ui", None)
        self.setCentralWidget(form)


        # set QPushButton
        self.Main_profile_bt = form.findChild(QPushButton, "Main_profile_bt")
        self.Main_food_bt = form.findChild(QPushButton, "Main_food_bt")
        self.Main_ex_bt = form.findChild(QPushButton, "Main_ex_bt")
        self.Main_sum_bt = form.findChild(QPushButton, "Main_sum_bt")
        self.Main_food_add_bt = form.findChild(QPushButton, "Main_food_add_bt")
        self.Main_ex_add_bt = form.findChild(QPushButton, "Main_ex_add_bt")



        # set QLabel
        self.Main_goal = form.findChild(QLabel, "Main_goal")
        self.Main_food_cal = form.findChild(QLabel, "Main_food_cal")
        self.Main_ex_cal = form.findChild(QLabel, "Main_ex_cal")
        self.Main_sum_cal = form.findChild(QLabel, "Main_sum_cal")


        #####################
        # connect QPushButton
        self.Main_profile_bt.clicked.connect(self.go_edit_profile)
        self.Main_food_bt.clicked.connect(self.go_food)
        self.Main_ex_bt.clicked.connect(self.go_exercise)

        # connect QPushButton dialog
        self.Main_food_add_bt.clicked.connect(self.dia_add_food)
        self.Main_ex_add_bt.clicked.connect(self.dia_add_exercise)



    def go_edit_profile(self):
        self.parent.changePage("Edit_Profile_Page_UI")


    def go_food(self):
        self.parent.changePage("Food_Page_UI")


    def go_exercise(self):
        self.parent.changePage("Exercise_Page_UI")


    def dia_add_food(self):

        d = Dia_add_food()
        d.dia_add_food_init(self)



    def dia_add_exercise(self):
        d = Dia_add_exercise()
        d.dia_add_ex_init(self)






