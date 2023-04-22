from PySide6.QtGui import QImage
from PySide6.QtWidgets import QMessageBox, QMainWindow

from System import ImageProcessing
from System.ImageOperation import ImageOperation
from Windows.MainWindow_UI import Ui_MainWindow


class MainWindow_Controller():
    def __init__(self, mainWindow:QMainWindow ,ui:Ui_MainWindow):
        self.mainWindow=mainWindow
        self.ui = ui
        self.qimage_byte=None
        return

    def pbtn_menu_loadImage_clicked(self):
        imagePath= ImageOperation.LoadImages(self.ui.wgt_main)
        self.ui.gv_image.setImage(imagePath)
        qimage= QImage(imagePath)
        self.ui.gv_image.setImageBackground(qimage)
        self.qimage_byte=None
        return

    def pbtn_menu_denoise_clicked(self):
        if (self.ui.gv_image.hasPhoto()):
            self.qimage_byte = ImageProcessing.DenoiseImage(self.ui.gv_image.imagePath)
            image_byte=self.qimage_byte
            qimage = QImage(image_byte.tobytes(), image_byte.shape[1], image_byte.shape[0], QImage.Format_Grayscale8)
            self.ui.gv_image.setImageBackground(qimage)
        return

    def pbtn_menu_segment_clicked(self):
        if (self.ui.gv_image.hasPhoto()):
            if self.qimage_byte is None:
                self.qimage_byte = ImageProcessing.DenoiseImage(self.ui.gv_image.imagePath)
            self.qimage_byte=ImageProcessing.Segment(self.qimage_byte)
            image_byte = self.qimage_byte
            qimage = QImage(image_byte.tobytes(), image_byte.shape[1], image_byte.shape[0],  QImage.Format_Grayscale8)
            self.ui.gv_image.setImageBackground(qimage)
        return

    def pbtn_menu_skeletonize_clicked(self):
        if (self.ui.gv_image.hasPhoto() and self.qimage_byte is not None):
            image_byte=ImageProcessing.Skeletonize()
            qimage = QImage(image_byte.tobytes(), image_byte.shape[1], image_byte.shape[0],  QImage.Format_Grayscale8)
            self.ui.gv_image.setImageBackground(qimage)
        return

    def pbtn_menu_analyse_clicked(self):
        return

    def pbtn_menu_report_clicked(self):
        return

    def pbtn_menu_close_clicked(self):
        confirm = QMessageBox.question(self.mainWindow, "Confirmation", "Are you sure you want to close the application?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.mainWindow.close()
        return
