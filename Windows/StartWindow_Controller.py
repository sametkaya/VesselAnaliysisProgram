from PySide6.QtWidgets import QMainWindow

from Windows.MainWindow_DL_Form import MainWindow_DL_Form
from Windows.MainWindow_Form import MainWindow_Form
from Windows.StartWindow_UI import Ui_StartWindow


class StartWindow_Controller():
    def __init__(self,startWindow:QMainWindow, ui:Ui_StartWindow):
        self.startWindow=startWindow
        self.ui=ui
        return

    def pbtn_deepLearning_clicked(self):
        MyMainWindow = MainWindow_DL_Form()
        MyMainWindow.show()
        self.startWindow.close()
        return

    def pbtn_imagePrcssng_clicked(self):
        MyMainWindow = MainWindow_Form()
        MyMainWindow.show()
        self.startWindow.close()
        return

