from PySide6.QtCore import QPoint
from PySide6.QtGui import QImage, Qt
from PySide6.QtWidgets import QMessageBox, QMainWindow

from GraphicItems.CustomRectItem import CustomRectItem
from GraphicItems.VAP_Point_Graph import VAP_Point_Graph
from GraphicItems.VAP_Vein_Graph import VAP_Vein_Graph
from System import ImageProcessing
from System.ImageOperation import ImageOperation
from System.ImageProcessing import GetImageFormats
from Windows.Custom.VAP_QGraphicsView import VAP_QGraphicsView
from Windows.MainWindow_UI import Ui_MainWindow


class MainWindow_Controller():
    def __init__(self, mainWindow:QMainWindow ,ui:Ui_MainWindow):
        self.mainWindow=mainWindow
        self.ui = ui
        self.pdf_document=None
        self.page_index=0
        return

    def radioBtn_imgPrcssng_clicked(self):
        self.ui.stack_wdgt_left_menu_btns.setCurrentIndex(0)
        return

    def radioBtn_deepLearning_clicked(self):
        self.ui.stack_wdgt_left_menu_btns.setCurrentIndex(1)
        return
        
    def pbtn_menu_loadImage_clicked(self):
        imagePath= ImageOperation.LoadImages(self.ui.wgt_main)
        image_raw, image_gray = ImageProcessing.GetImageFormats(imagePath)
        self.ui.gv_image.scene.SetImage(imagePath, image_raw, image_gray)

        self.ui.gv_image.scene.Update_Branch_Points(False, False, False)
        self.ui.gv_image.scene.Update_Tip_Points(False, False, False)
        self.ui.gv_image.scene.Update_Branch_Paths(False, False, False)
        #ipad=r"C:\Users\skaya\PycharmProjects\VesselAnaliysisProgram\Images\iskelet.png"
        #image_raw, image_byte8 = GetImageFormats(ipad)
        #self.ui.gv_image.scene.SetImage(ipad, image_raw, image_byte8)

        return

    def pbtn_menu_denoise_clicked(self):
        if (self.ui.gv_image.scene.vap_image.HasImage()):
            image_byte8 = ImageProcessing.DenoiseImage(self.ui.gv_image.scene.vap_image.image_byte8)
            image_byte8= image_byte8.reshape(image_byte8.shape[0], image_byte8.shape[1])
            self.ui.gv_image.scene.vap_image.SetProcessImage(image_byte8)
            #image_byte= self.ui.gv_image.scene.image_byte8
            #qimage = QImage(image_byte.tobytes(), image_byte.shape[1], image_byte.shape[0], QImage.Format_Grayscale8)
            #self.ui.gv_image.setImageBackground(qimage)

        return

    def pbtn_menu_segment_clicked(self):
        if (self.ui.gv_image.scene.vap_image.HasImage()):
            image_byte8 = ImageProcessing.Segment(self.ui.gv_image.scene.vap_image.image_byte8)
            #self.ui.gv_image.scene.qimage_byte = ImageProcessing.BinaryClosing(self.qimage_byte)
            image_byte8 = ImageProcessing.RemoveSmallObject(image_byte8)
            self.ui.gv_image.scene.vap_image.SetProcessImage(image_byte8)
            self.ui.gv_image.scene.vap_image.image_segmented_byte8 = image_byte8
            vascularAreaFraction,whitePixelCount,blackPixelCount= ImageProcessing.GetVascularAreaFractionValues(image_byte8)
            self.ui.gv_image.scene.vap_image.vascularAreaFraction = vascularAreaFraction
            self.ui.gv_image.scene.vap_image.whitePixelCount = whitePixelCount
            self.ui.gv_image.scene.vap_image.blackPixelCount =blackPixelCount
            #image_byte = self.ui.gv_image.scene.qimage_byte
            #qimage = QImage(image_byte.tobytes(), image_byte.shape[1], image_byte.shape[0],  QImage.Format_Grayscale8)
            #self.ui.gv_image.setImageBackground(qimage)
        return

    def pbtn_menu_skeletonize_clicked(self):
        if (self.ui.gv_image.scene.vap_image.HasImage()):
            image_byte8 = ImageProcessing.Skeletonize(self.ui.gv_image.scene.vap_image.image_byte8)
            self.ui.gv_image.scene.vap_image.SetProcessImage(image_byte8)
            self.ui.gv_image.scene.vap_image.image_skeletonized_byte8 = image_byte8
            #image_byte = self.qimage_byte
            #qimage = QImage(image_byte.tobytes(), image_byte.shape[1], image_byte.shape[0],  QImage.Format_Grayscale8)
            #self.ui.gv_image.setImageBackground(qimage)
        return

    def pbtn_menu_analyse_clicked(self):
        if (self.ui.gv_image.scene.vap_image.HasImage()):

            vap_vein_list= ImageProcessing.find_branch_pts2(self.ui.gv_image.scene.vap_image.image_byte8)
            self.ui.gv_image.scene.AddVeins(vap_vein_list)

            vap_point_branch_list = ImageProcessing.find_branch_pts(self.ui.gv_image.scene.vap_image.image_byte8)
            self.ui.gv_image.scene.AddBranchPoints(vap_point_branch_list)

            vap_point_tip_list = ImageProcessing.find_tips(self.ui.gv_image.scene.vap_image.image_byte8)
            self.ui.gv_image.scene.AddTipPoints(vap_point_tip_list)
        return

    def chbx_analyse_showBranchPoints_clicked(self):
        isVisible = self.ui.chbx_analyse_showBranchPoints.isChecked()
        showMarker = self.ui.chbx_analyse_showBranchPointMarker.isChecked()
        showCenter = self.ui.chbx_analyse_showBranchPointCenter.isChecked()


        self.ui.gv_image.scene.Update_Branch_Points(isVisible,showCenter,showMarker)


    def chbx_analyse_showTipPoints_clicked(self):
        isVisible = self.ui.chbx_analyse_showTipPoints.isChecked()
        showMarker = self.ui.chbx_analyse_showTipPointMarker.isChecked()
        showCenter = self.ui.chbx_analyse_showTipPointCenter.isChecked()

        self.ui.gv_image.scene.Update_Tip_Points(isVisible,showCenter,showMarker)


    def chbx_analyse_showBranchPaths_clicked(self):
        isVisible = self.ui.chbx_analyse_showBranchPaths.isChecked()
        showId = self.ui.chbx_analyse_showBranchPathId.isChecked()
        showLenght = self.ui.chbx_analyse_showBranchPathLenght.isChecked()

        self.ui.gv_image.scene.Update_Branch_Paths(isVisible, showId, showLenght)



    def pbtn_menu_report_clicked(self):
        MySecondWindow = SecondWindow_Form(self)
        MySecondWindow.show()

        return

    def pbtn_menu_close_clicked(self):
        confirm = QMessageBox.question(self.mainWindow, "Confirmation", "Are you sure you want to close the application?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.mainWindow.close()
        return

    def load_pdf(self,file_name):
        if file_name:
            self.pdf_document = fitz.open(file_name)
            self.show_page()

    def show_page(self):
        if not self.pdf_document:
            return

        page = self.pdf_document.load_page(self.page_index)
        image = page.get_pixmap()
        qt_image = QImage(image.samples, image.width, image.height, image.stride, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)

        # Calculate the scale factor to fit the page to the view
        scale_factor = min(self.ui.pdf_view.width() / pixmap.width(), self.ui.pdf_view.height() / pixmap.height()) * 1.5
        scaled_pixmap = pixmap.scaled(pixmap.width() * scale_factor, pixmap.height() * scale_factor, Qt.KeepAspectRatio)

        # Calculate the center position to display the page in the view
        center_x = (self.ui.pdf_view.width() - scaled_pixmap.width()) / 2
        center_y = (self.ui.pdf_view.height() - scaled_pixmap.height()) / 2

        top_left_x = center_x if center_x > 0 else 0
        top_left_y = center_y if center_y > 0 else 0

        self.ui.scene.clear()
        self.ui.scene.addPixmap(scaled_pixmap)
        self.ui.pdf_view.setSceneRect(top_left_x, top_left_y, scaled_pixmap.width(), scaled_pixmap.height())

    def previous_page(self):
        if self.page_index > 0:
            self.page_index -= 1
            self.show_page()

    def next_page(self):
        if self.pdf_document and self.page_index < len(self.pdf_document) - 1:
            self.page_index += 1
            self.show_page()
