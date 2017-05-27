import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class Exercise_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.exercise_page_init()

    def exercise_page_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Exercise_page_ui.ui", None)
        self.setCentralWidget(form)

        # set QLineEdit
        self.exercise_search_textEdit = form.findChild(QLineEdit, "exercise_search_textEdit")

        #set QPushButton
        self.exercise_search_bt = form.findChild(QPushButton, "exercise_search_bt")
        self.exercise_back_bt = form.findChild(QPushButton, "exercise_back_bt")
        self.exercise_add_bt = form.findChild(QPushButton, "exercise_add_bt")
        self.exercise_delete_bt = form.findChild(QPushButton, "exercise_delete_bt")



        ####################
        #connect QPushButton
        self.exercise_back_bt.clicked.connect(self.back_main)



    def back_main(self):
        self.parent.changePage("Main_Page")

