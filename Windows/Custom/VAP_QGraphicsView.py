from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QPixmap

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from Windows.Custom.VAP_Scene import VAP_Scene


class VAP_QGraphicsView(QtWidgets.QGraphicsView):



    photoClicked = QtCore.Signal(QtCore.QPoint)


    def __init__(self, parent):
        super(VAP_QGraphicsView, self).__init__(parent)
        self.setAutoFillBackground(True)
        pal = QPalette()
        pal.setColor(QPalette.Window, "#3a3a3a")
        self.setPalette(pal)
        #self.image = QImage()
        self.imagePath = None
        self.zoom = 0
        self.isEmpty = True
        self.scenes = []
        self.scenes.append(VAP_Scene(self))
        self.scene = self.scenes[0]

        self.setScene(self.scene)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor("#3a3a3a")))
        #self.setFrameShape(QtWidgets.QFrame.NoFrame)


    def fitInView(self, scale=True):
        rect = QtCore.QRectF(self.scene.vap_image.image_qimage.rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if self.scene.HasImage():
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self.zoom = 0

    #def setImage(self, imagePath):
    #    self.scene.SetImage(imagePath)
        #self.image = QImage(imagePath)
        #self.imagePath = imagePath
    #    self.setImageBackground(self.scene.image_pixmap)

    def setImageBackground(self, qimage=None):
        self.scene.vap_image.image_pixmap = qimage
        pixmap = QPixmap.fromImage(self.image)
        self.zoom = 0
        if pixmap and not pixmap.isNull():
            self.isEmpty = False
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self.scene.vap_image.image_pixmap.setPixmap(pixmap)
        else:
            self.isEmpty = True
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self.scene.vap_image.image_pixmap.setPixmap(QtGui.QPixmap())

        self.fitInView()

    def wheelEvent(self, event):
        if self.scene.vap_image.HasImage():
            if event.angleDelta().y() > 0:
                factor = 1.25
                self.zoom += 1
            else:
                factor = 0.8
                self.zoom -= 1
            if self.zoom > 0:
                self.scale(factor, factor)
            elif self.zoom == 0:
                self.fitInView()
            else:
                self.zoom = 0
                self.fitInView()

    def toggleDragMode(self):
        if self.dragMode() == QtWidgets.QGraphicsView.ScrollHandDrag:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        elif not self.scene.vap_image.image_pixmap.pixmap().isNull():
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

    def mousePressEvent(self, event):
        if self.scene.vap_image.image_pixmap.isUnderMouse():
            self.photoClicked.emit(self.mapToScene(event.pos()).toPoint())
        super(VAP_QGraphicsView, self).mousePressEvent(event)

