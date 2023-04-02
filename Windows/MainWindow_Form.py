from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QGraphicsView

from Windows.Custom.VAP_QGraphicsView import VAP_QGraphicsView
from Windows.MainWindow_Controller import MainWindow_Controller
from Windows.MainWindow_UI import Ui_MainWindow


class MainWindow_Form(QMainWindow):
    def __init__(self):
        super(MainWindow_Form, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cntlr = MainWindow_Controller(self.ui)
        self.initilizeComponent()
        return

    def initilizeComponent(self):
        # region image
        self.ui.gv_image = VAP_QGraphicsView(self.ui.frm_image)
        self.ui.lyt_image.addWidget(self.ui.gv_image)
        self.ui.wgts_sceneContent.setCurrentWidget(self.ui.page_image_processing)


        #endregion


        # region buttons click
        self.ui.pbtn_menu_loadImage.clicked.connect(self.cntlr.pbtn_menu_loadImage_clicked)
        self.ui.pbtn_menu_segment.clicked.connect(self.cntlr.pbtn_menu_segment_clicked)
        # endregion
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyMainWindow = MainWindow_Form()
    MyMainWindow.show()
    sys.exit(app.exec())