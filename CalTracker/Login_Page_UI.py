import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class Login_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.loginPageInit()

    def loginPageInit(self):
        loader = QUiLoader()
        form = loader.load("./UIDesigner/LoginPageUI.ui", None)
        self.setCentralWidget(form)

        self.login_button = form.findChild(QPushButton, "login_button")
        self.login_button.clicked.connect(self.login)

        self.register_button = form.findChild(QPushButton, "register_button")
        self.register_button.clicked.connect(self.register)


    def login(self):
        self.parent.loginAs("user object")
        self.parent.changePage("Main_Page")
    def register(self):
        pass