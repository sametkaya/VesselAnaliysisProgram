from System.ImageOperation import ImageOperation
from Windows.MainWindow_UI import Ui_MainWindow


class MainWindow_Controller():
    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        return

    def pbtn_menu_loadImage_clicked(self):
        ImageOperation.LoadImages(self.ui.wgt_main)

        return


