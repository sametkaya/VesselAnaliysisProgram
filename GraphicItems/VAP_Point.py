from PySide6.QtCore import Qt, QPoint, QRectF, QRect, QPointF
from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtWidgets import QGraphicsItem



class VAP_Point(QGraphicsItem):

    pointMarkerPen = QPen(Qt.SolidLine)
    pointCenterPen = QPen(Qt.SolidLine)
    def __init__(self, pixmapItem, ix, iy, idn=None, color=Qt.green, width=10, height=10, penThickness=1):
        super().__init__()

        self.idn = idn
        self.imagePoint= QPoint(ix, iy)
        self.centerPoint = pixmapItem.mapToScene(QPointF(ix, iy))
        self.width = width
        self.height = height
        self.color = color
        self.penThickness = penThickness
        self.showMarker = True
        self.showCenter = True
        self.update()

    def updateIt(self):
        self.update(self.boundingRect())

    def boundingRect(self):

        return QRectF(0.5+ self.centerPoint.x() - self.width / 2, 0.5+self.centerPoint.y() - self.height / 2, self.width, self.height)

    def paint(self, painter, option, widget):
        #pen = QPen(Qt.SolidLine)
        #pen.setWidth(self.penThickness)
        #pen.setColor(self.color)
        #painter.setPen(pen)
        if self.showMarker:

            VAP_Point.pointMarkerPen.setWidth(self.penThickness)
            VAP_Point.pointMarkerPen.setColor(self.color)
            painter.setPen(VAP_Point.pointMarkerPen)
            painter.drawEllipse(self.boundingRect())
        if self.showCenter:
            #pen = QPen(Qt.SolidLine)
            VAP_Point.pointCenterPen.setWidth(self.penThickness)
            VAP_Point.pointCenterPen.setColor(self.color)
            VAP_Point.pointCenterPen.setWidth(0)
            painter.setPen(VAP_Point.pointCenterPen)
            #painter.setPen(pen)
            painter.setBrush(self.color)
            painter.drawRect(self.centerPoint.x(), self.centerPoint.y(), 1, 1)
