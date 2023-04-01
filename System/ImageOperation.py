import os

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
        image = None

        if dlg.exec_() == QFileDialog.Accepted:
            image = dlg.selectedFiles()[0]
            print("Selected file:", image)


        return image
