from PySide6.QtCore import Qt, QPoint, QRectF, QRect, QPointF
from PySide6.QtGui import QBrush, QColor, QPen, QPainterPath
from PySide6.QtWidgets import QGraphicsItem, QGraphicsPathItem


class VAP_Vein(QGraphicsItem):

    def __init__(self, pixmapItem, point_list, lenght, midPoint, idn=None, color=Qt.blue, penThickness=0):
        super().__init__()
        self.idn = idn
        self.point_list = point_list
        if idn==161:
            print("dur")
        self.lenght = lenght
        self.imageCenterPoint = point_list[int(len(point_list)/2)]
        self.mapped_point_list = [pixmapItem.mapToScene(QPointF(ix, iy)) for ix, iy in self.point_list]
        self.sceneCenterPoint = pixmapItem.mapToScene(QPointF(self.imageCenterPoint[0], self.imageCenterPoint[1]))
        self.showPath = True
        self.showId = True
        self.showLenght = True
        self.color = color
        self.penThickness = penThickness
        self.update()

    def updateIt(self):
        self.update(self.boundingRect())

    def boundingRect(self):
        pf = QPointF(0.5+self.mapped_point_list[0].x(), 0.5+self.mapped_point_list[0].y())
        rect = QRectF(pf, pf)
        for point in self.mapped_point_list:
            pf = QPointF(0.5 + point.x(), 0.5 + point.y())
            rect = rect.united(QRectF(pf, pf))
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

        pen.setWidth(1)
        pen.setColor(Qt.yellow)
        painter.setPen(pen)
        #if self.showLenght and self.idn == 0:
        if self.showLenght:
            painter.drawText(self.sceneCenterPoint, str(self.idn) + ":" + str(int(self.lenght)))
            painter.setBrush(self.color)
            painter.drawRect(self.sceneCenterPoint.x(), self.sceneCenterPoint.y(), 1, 1)

        #for i in range(len(self.mapped_point_list) - 1):
        #    painter.drawRect(self.mapped_point_list[i].x(), self.mapped_point_list[i].y(), 1, 1)
            #painter.d(self.mapped_point_list[i], self.mapped_point_list[i + 1])

