from PySide6.QtCore import QPoint
from PySide6.QtGui import QImage, Qt
from PySide6.QtWidgets import QMessageBox, QMainWindow

from GraphicItems.VAP_Point import VAP_Point
from GraphicItems.VAP_Vein import VAP_Vein
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
            self.qimage_byte=self.qimage_byte.reshape( self.qimage_byte.shape[0], self.qimage_byte.shape[1])
            image_byte= self.qimage_byte
            qimage = QImage(image_byte.tobytes(), image_byte.shape[1], image_byte.shape[0], QImage.Format_Grayscale8)
            self.ui.gv_image.setImageBackground(qimage)
        return

    def pbtn_menu_segment_clicked(self):
        if (self.ui.gv_image.hasPhoto()):
            if self.qimage_byte is None:
                self.qimage_byte = ImageProcessing.DenoiseImage(self.ui.gv_image.imagePath)
            self.qimage_byte = ImageProcessing.Segment(self.qimage_byte)
            self.qimage_byte = ImageProcessing.BinaryClosing(self.qimage_byte)
            self.qimage_byte = ImageProcessing.RemoveSmallObject(self.qimage_byte)
            image_byte = self.qimage_byte
            qimage = QImage(image_byte.tobytes(), image_byte.shape[1], image_byte.shape[0],  QImage.Format_Grayscale8)
            self.ui.gv_image.setImageBackground(qimage)
        return

    def pbtn_menu_skeletonize_clicked(self):
        if (self.ui.gv_image.hasPhoto() and self.qimage_byte is not None):
            self.qimage_byte = ImageProcessing.Skeletonize(self.qimage_byte)
            image_byte = self.qimage_byte
            qimage = QImage(image_byte.tobytes(), image_byte.shape[1], image_byte.shape[0],  QImage.Format_Grayscale8)
            self.ui.gv_image.setImageBackground(qimage)
        return

    def pbtn_menu_analyse_clicked(self):
        if (self.ui.gv_image.hasPhoto() and self.qimage_byte is not None):

            branch_paths = ImageProcessing.find_all_branch_paths(self.qimage_byte)
            for path in branch_paths:
                vvein= VAP_Vein(self.ui.gv_image.photo, path[5], path[1], path[4], path[0])
                self.ui.gv_image.scane.addItem(vvein)

            self.branch_dict, _ = ImageProcessing.find_branch_pts(self.qimage_byte)
            for point in self.branch_dict:
                #vpoint= VAP_Point(self.branch_dict[point][0], self.branch_dict[point][1], point)
                vpoint = VAP_Point(self.ui.gv_image.photo, self.branch_dict[point][0][1], self.branch_dict[point][0][0], color=Qt.red)
                self.ui.gv_image.scane.addItem(vpoint)


            self.tip_dict = ImageProcessing.find_tips(self.qimage_byte)

            for point in self.tip_dict:
                # vpoint= VAP_Point(self.branch_dict[point][0], self.branch_dict[point][1], point)
                vpoint = VAP_Point(self.ui.gv_image.photo, self.tip_dict[point][1], self.tip_dict[point][0],color=Qt.green)
                self.ui.gv_image.scane.addItem(vpoint)
                self.ui.gv_image.tips.append(vpoint)



        return

    def pbtn_menu_report_clicked(self):
        for vpoint in self.ui.gv_image.tips:
            vpoint.showMarker = not vpoint.showMarker
            vpoint.updateIt()

        return

    def pbtn_menu_close_clicked(self):
        confirm = QMessageBox.question(self.mainWindow, "Confirmation", "Are you sure you want to close the application?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.mainWindow.close()
        return
