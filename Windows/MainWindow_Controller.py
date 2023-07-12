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

        return

    def pbtn_menu_loadImage_clicked(self):
        imagePath= ImageOperation.LoadImages(self.ui.wgt_main)
        image_raw, image_gray = ImageProcessing.GetImageFormats(imagePath)
        self.ui.gv_image.scene.SetImage(imagePath, image_raw, image_gray)

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

        ImageOperation.SaveInfos(self.ui.gv_image.scene.vap_image)


        return

    def pbtn_menu_close_clicked(self):
        confirm = QMessageBox.question(self.mainWindow, "Confirmation", "Are you sure you want to close the application?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.mainWindow.close()
        return
