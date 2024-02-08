from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow

from Windows.StartWindow_Controller import StartWindow_Controller
from Windows.StartWindow_UI import Ui_StartWindow

class StartWindow_Form(QMainWindow):
    def __init__(self):
        super(StartWindow_Form, self).__init__()
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)
        self.cntrlr = StartWindow_Controller(self,self.ui)
        self.initilizeComponent()
        return

    def initilizeComponent(self):
        self.ui.pbtn_deepLearning.clicked.connect(self.cntrlr.pbtn_deepLearning_clicked)
        self.ui.pbtn_imagePrcssng.clicked.connect(self.cntrlr.pbtn_imagePrcssng_clicked)
        return
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyStartWindow = StartWindow_Form()
    MyStartWindow.show()
    sys.exit(app.exec())