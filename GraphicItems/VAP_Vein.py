from PySide6.QtCore import Qt, QPoint, QRectF, QRect, QPointF
from PySide6.QtGui import QBrush, QColor, QPen, QPainterPath, QFont
from PySide6.QtWidgets import QGraphicsItem, QGraphicsPathItem


class VAP_Vein(QGraphicsItem):
    pointMarkerPen = QPen(Qt.SolidLine)
    lenghtDotDigit =3
    def __init__(self, pixmapItem, point_list, lenght, midPoint, idn=None, color=Qt.blue, penThickness=0):
        super().__init__()

        self.idn = idn
        self.point_list = point_list
        self.lenght = lenght

        self.imagePathCenterPoint = midPoint
        self.mapped_point_list = [pixmapItem.mapToScene(QPointF(ix, iy)) for ix, iy in self.point_list]
        self.scenePathCenterPoint = pixmapItem.mapToScene(QPointF(self.imagePathCenterPoint[0], self.imagePathCenterPoint[1]))

        self.showId = True
        self.showLenght = True
        self.showInfo = self.showId or self.showLenght
        self.lenghtDotDigit = round(lenght, VAP_Vein.lenghtDotDigit)
        self.color = color
        self.penThickness = penThickness
        self.font = QFont()
        self.font.setPointSize(self.penThickness+3)
        self.update()

    def updateIt(self):
        self.update(self.boundingRect())

    def boundingRect(self):
        pf = QPointF(0.5+self.mapped_point_list[0].x(), 0.5+self.mapped_point_list[0].y())
        rect = QRectF(pf.x(), pf.y(), 1, 1)
        for point in self.mapped_point_list[1:]:
            pf = QPointF(0.5 + point.x(), 0.5 + point.y())
            rect = rect.united(QRectF(pf.x(), pf.y(), 1, 1))
        return rect

    def paint(self, painter, option, widget):

        pen = QPen(Qt.SolidLine)
        pen.setWidth(self.penThickness)
        pen.setColor(self.color)
        painter.setPen(pen)
        painter.setBrush(self.color)
        #painter.drawPath(self.path)
        for point in self.mapped_point_list:
            painter.drawRect(point.x(), point.y(), 1, 1)



        #if self.showLenght and self.idn == 0:
        if self.showInfo:
            painter.setFont(self.font)
            pen.setColor(Qt.yellow)
            painter.setPen(pen)

            text = ""
            if self.showId:
                text = str(self.idn)
            if self.showLenght:
                if self.showId:
                    text = text + "->"+str(self.lenghtDotDigit)
                else:
                    text = str(self.lenghtDotDigit)
            painter.drawText(self.scenePathCenterPoint, text)
            pen.setWidth(0)
            painter.setPen(pen)
            painter.setBrush(self.color)
            painter.drawRect(self.scenePathCenterPoint.x(), self.scenePathCenterPoint.y(), 1, 1)

        #for i in range(len(self.mapped_point_list) - 1):
        #    painter.drawRect(self.mapped_point_list[i].x(), self.mapped_point_list[i].y(), 1, 1)
            #painter.d(self.mapped_point_list[i], self.mapped_point_list[i + 1])

