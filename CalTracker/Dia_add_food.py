import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class Dia_add_food:
    def dia_add_food_init(self,dia):
        self.dia_add_food(dia)



    def dia_add_food(self,dia):
        # Dialog box
        self.addDialog = QDialog(dia)
        self.addDialog.setMinimumSize(700, 600)
        layout = QVBoxLayout()

        loader = QUiLoader()
        dialogForm = loader.load("./UIDesigner/Food_add_dialog_ui.ui", None)
        self.addDialog.setWindowTitle("Food Add Dialog")

        layout.addWidget(dialogForm)



        # init all attribute
        # self.typeLabel = dialogForm.findChild(QLabel, "typeLabel")


        # show dialog box
        self.addDialog.setLayout(layout)
        self.addDialog.show()