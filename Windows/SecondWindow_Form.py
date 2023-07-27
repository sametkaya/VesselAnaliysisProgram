from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QDialog

from Windows.Custom.VAP_QGraphicsView import VAP_QGraphicsView
from Windows.SecondWindow_Controller import SecondWindow_Controller
from Windows.SecondWindow_UI  import Ui_SecondWindow


class SecondWindow_Form(QMainWindow):
    def __init__(self,mainWndw):
        super(SecondWindow_Form, self).__init__()
        self.ui = Ui_SecondWindow()
        self.mainWndw=mainWndw
        self.gv_image=self.mainWndw.ui.gv_image.scene.vap_image
        self.ui.setupUi(self)
        self.cntrlr = SecondWindow_Controller(self,self.ui,self.mainWndw)
        self.initilizeComponent()
        return

    def initilizeComponent(self):
        # region buttons click
        self.ui.pbtn_create_pdf.clicked.connect(self.cntrlr.pbtn_create_pdf_clicked)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MySecondWindow = SecondWindow_Form()
    MySecondWindow.show()
    sys.exit(app.exec())