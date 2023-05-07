from PySide6 import QtWidgets
from PySide6.QtGui import QImage, QPixmap, Qt

from GraphicItems.VAP_Point import VAP_Point
from GraphicItems.VAP_Vein import VAP_Vein


class VAP_Scene(QtWidgets.QGraphicsScene):


    def __init__(self, parent):
        super(VAP_Scene, self).__init__(parent)
        self.image_path=""
        self.photo = QtWidgets.QGraphicsPixmapItem()
        self.addItem(self.photo)
        self.qimage_byte = None
        self.is_empty = True
        self.veins = []
        self.branchPoints = []
        self.tipPoints = []

    def SetImage(self, imagePath):
        self.image = QImage(imagePath)
        self.imagePath = imagePath
        pixmap = QPixmap.fromImage(self.image)
        self.photo.setPixmap(pixmap)

        self.is_empty= False

    def AddVeins(self, branch_paths):
        for path in branch_paths:
            vvein = VAP_Vein(self.photo, path[5], path[1], path[4], path[0])
            self.addItem(vvein)
            self.veins.append(vvein)

    def AddBranchPoints(self, branch_points_dict):
        for point in branch_points_dict:
            vpoint = VAP_Point(self.photo, branch_points_dict[point][0][1], branch_points_dict[point][0][0], color=Qt.red)
            self.addItem(vpoint)
            self.branchPoints.append(vpoint)

    def AddTipPoints(self, tip_points_dict):
        for point in tip_points_dict:
            vpoint = VAP_Point(self.photo, tip_points_dict[point][1], tip_points_dict[point][0], color=Qt.green)
            self.addItem(vpoint)
            self.tipPoints.append(vpoint)

    def SetVeinsProperties(self, showPath = False, showId = False, showLenght = False, showInfo = False, lenghtDotDigit = 3):

        VAP_Vein.showPath = showPath
        VAP_Vein.showId = showId
        VAP_Vein.showLenght = showLenght
        VAP_Vein.showInfo = showInfo
        VAP_Vein.lenghtDotDigit = lenghtDotDigit
        for vein in self.veins:
            vein.updateIt()



