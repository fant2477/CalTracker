import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class Edit_Profile_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.edit_profile_page_init()

    def edit_profile_page_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Edit_page_ui.ui", None)
        self.setCentralWidget(form)

        # set QLineEdit
        self.EditPro_name_textEdit = form.findChild(QLineEdit, "EditPro_name_textEdit")
        self.EditPro_userName_textEdit = form.findChild(QLineEdit, "EditPro_userName_textEdit")
        self.EditPro_passWord_textEdit = form.findChild(QLineEdit, "EditPro_passWord_textEdit")
        self.EditPro_setGoal_textEdit = form.findChild(QLineEdit, "EditPro_setGoal_textEdit")
        self.EditPro_weight_textEdit = form.findChild(QLineEdit, "EditPro_weight_textEdit")
        self.EditPro_height_textEdit = form.findChild(QLineEdit, "EditPro_height_textEdit")
        self.EditPro_age_textEdit = form.findChild(QLineEdit, "EditPro_age_textEdit")

        #set QPushButton
        self.EditPro_save_bt = form.findChild(QPushButton, "EditPro_save_bt")
        self.EditPro_back_bt = form.findChild(QPushButton, "EditPro_back_bt")





        #connect QPushButton
        self.EditPro_back_bt.clicked.connect(self.back_main)



    def back_main(self):
        self.parent.changePage("Main_Page")

