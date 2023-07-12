import csv
import os

import skimage
from PySide6.QtCore import QFileInfo
from PySide6.QtWidgets import QFileDialog, QWidget

from Datas.Data import Data

from System.FileSystem import FileSystem


class ImageOperation(object):

    @staticmethod
    def LoadImages(parentWidget:QWidget):

        dlg = QFileDialog(parentWidget)
        dlg.setFileMode(QFileDialog.ExistingFiles)
        dlg.setWindowTitle("Load Images")
        dlg.setOption(QFileDialog.DontUseNativeDialog, True)
        dlg.setNameFilter("Image Files (*.jpg *.png *.tif *.tiff)")
        imagePath = None

        if dlg.exec_() == QFileDialog.Accepted:
            imagePath = dlg.selectedFiles()[0]
            print("Selected file:", imagePath)


        return imagePath
    @staticmethod
    def SaveInfos(vap_image):
        folder_dialog = QFileDialog()
        folder_dialog.setFileMode(QFileDialog.Directory)
        folder_dialog.setOption(QFileDialog.ShowDirsOnly, True)

        if folder_dialog.exec_() == QFileDialog.Accepted:
            # Get the selected folder path
            selected_folder = os.path.normpath(folder_dialog.selectedFiles()[0])

            image_report_name = os.path.splitext(vap_image.image_raw_name)[0]
            report_folder = os.path.join(selected_folder, image_report_name)
            # Create the folder if it doesn't exist
            if not os.path.exists(report_folder):
                os.makedirs(report_folder)


            # Create a CSV file inside the folder



            csv_file_path = os.path.join(report_folder, image_report_name+".csv")
            csv_file = open(csv_file_path, 'w', newline='')
            csv_writer = csv.writer(csv_file)
            field = ["vaf(%)", "branch_points_count", "tip_point_count", "vein_count", "total_vein_length", "average_vein_length" ]
            csv_writer.writerow(field)

            row = [vap_image.vascularAreaFraction, len(vap_image.branchPoints), len(vap_image.tipPoints), len(vap_image.vap_veins),
                   vap_image.total_vein_length, vap_image.average_vein_length]
            csv_writer.writerow(row)

            field = ["id", "length", "p1.x, p1.y","p1_type", "p2.x, p2.y","p2_type"]
            csv_writer.writerow(field)
            for vap_vein in vap_image.vap_veins:
                vap_points = []
                vap_points.extend(vap_vein.tip_points)
                vap_points.extend(vap_vein.branch_points)
                if (len(vap_points)==1):
                    vap_points.append(vap_vein.vap_point_list[-1])
                try:
                    row = [vap_vein.idn, vap_vein.length, str(vap_points[0].x)+","+str(vap_points[0].y),vap_points[0].vp_type.name, str(vap_points[1].x)+","+str(vap_points[1].y),vap_points[1].vp_type.name]
                except:
                    print("An exception occurred")
                csv_writer.writerow(row)

            csv_file.close()
            if (vap_image.image_raw is not None):
                skimage.io.imsave(os.path.join(report_folder, image_report_name + "_raw.png"),vap_image.image_raw)
            if (vap_image.image_gray is not None):
                skimage.io.imsave(os.path.join(report_folder, image_report_name + "_gray.png"),
                                      vap_image.image_gray)
            if(vap_image.image_segmented_byte8 is not None):
                skimage.io.imsave(os.path.join(report_folder, image_report_name+"_segmented.png"), vap_image.image_segmented_byte8)
            if (vap_image.image_skeletonized_byte8 is not None):
                skimage.io.imsave(os.path.join(report_folder, image_report_name + "_skeletonized.png"),vap_image.image_skeletonized_byte8)


