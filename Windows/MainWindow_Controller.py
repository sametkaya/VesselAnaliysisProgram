from PySide6.QtGui import QImage

from System import ImageProcessing
from System.ImageOperation import ImageOperation
from Windows.MainWindow_UI import Ui_MainWindow


class MainWindow_Controller():
    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        return

    def pbtn_menu_loadImage_clicked(self):
        imagePath= ImageOperation.LoadImages(self.ui.wgt_main)
        self.ui.gv_image.setImage(imagePath)
        qimage= QImage(imagePath)
        self.ui.gv_image.setImageBackground(qimage)
        return

    def pbtn_menu_segment_clicked(self):
        if (self.ui.gv_image.hasPhoto()):
            image_byte=ImageProcessing.DenoiseImage(self.ui.gv_image.imagePath)
            image_byte=ImageProcessing.Segment(image_byte)
            qimage = QImage(image_byte.tobytes(), image_byte.shape[1], image_byte.shape[0],  QImage.Format_Grayscale8)
            self.ui.gv_image.setImageBackground(qimage)
        return
