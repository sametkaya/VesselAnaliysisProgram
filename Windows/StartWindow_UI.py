# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartWindow_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        if not StartWindow.objectName():
            StartWindow.setObjectName(u"StartWindow")
        StartWindow.resize(520, 266)
        StartWindow.setMinimumSize(QSize(520, 266))
        StartWindow.setMaximumSize(QSize(520, 266))
        StartWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget = QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setStyleSheet(u"background-color:rgb(171, 171, 171)")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vrtcl_frm_left = QFrame(self.horizontalWidget)
        self.vrtcl_frm_left.setObjectName(u"vrtcl_frm_left")
        self.verticalLayout_2 = QVBoxLayout(self.vrtcl_frm_left)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_namePrjct = QLabel(self.vrtcl_frm_left)
        self.lbl_namePrjct.setObjectName(u"lbl_namePrjct")
        font = QFont()
        font.setFamilies([u"Sitka"])
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(True)
        self.lbl_namePrjct.setFont(font)
        self.lbl_namePrjct.setStyleSheet(u"color: rgb(0, 85, 127);\n"
"color: rgb(59, 59, 59);")

        self.verticalLayout_2.addWidget(self.lbl_namePrjct)

        self.lbl_logo = QLabel(self.vrtcl_frm_left)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setStyleSheet(u"image: url(:/bv_logo/logo/app_icon.png);")

        self.verticalLayout_2.addWidget(self.lbl_logo)


        self.horizontalLayout.addWidget(self.vrtcl_frm_left)

        self.vrtcl_frm_right = QFrame(self.horizontalWidget)
        self.vrtcl_frm_right.setObjectName(u"vrtcl_frm_right")
        self.verticalLayout = QVBoxLayout(self.vrtcl_frm_right)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vrtcl_wdgt_buttons = QWidget(self.vrtcl_frm_right)
        self.vrtcl_wdgt_buttons.setObjectName(u"vrtcl_wdgt_buttons")
        self.vrtcl_wdgt_buttons.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(72, 72, 72);\n"
"	 border-style: solid;\n"
" 	border-width:1px;\n"
" 	border-color: white;\n"
"	color: white\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(56, 56, 56);\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.vrtcl_wdgt_buttons)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, -1, -1, -1)
        self.pbtn_imagePrcssng = QPushButton(self.vrtcl_wdgt_buttons)
        self.pbtn_imagePrcssng.setObjectName(u"pbtn_imagePrcssng")
        self.pbtn_imagePrcssng.setMinimumSize(QSize(120, 40))
        self.pbtn_imagePrcssng.setMaximumSize(QSize(120, 40))
        self.pbtn_imagePrcssng.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pbtn_imagePrcssng)

        self.pbtn_deepLearning = QPushButton(self.vrtcl_wdgt_buttons)
        self.pbtn_deepLearning.setObjectName(u"pbtn_deepLearning")
        self.pbtn_deepLearning.setMinimumSize(QSize(120, 40))
        self.pbtn_deepLearning.setMaximumSize(QSize(120, 40))
        self.pbtn_deepLearning.setLayoutDirection(Qt.LeftToRight)
        self.pbtn_deepLearning.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pbtn_deepLearning)


        self.verticalLayout.addWidget(self.vrtcl_wdgt_buttons)


        self.horizontalLayout.addWidget(self.vrtcl_frm_right)


        self.horizontalLayout_2.addWidget(self.horizontalWidget)

        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)

        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle(QCoreApplication.translate("StartWindow", u"Brain Vasculyzer", None))
        self.lbl_namePrjct.setText(QCoreApplication.translate("StartWindow", u"Brain Vasculyzer", None))
        self.lbl_logo.setText("")
        self.pbtn_imagePrcssng.setText(QCoreApplication.translate("StartWindow", u"Image Processing", None))
        self.pbtn_deepLearning.setText(QCoreApplication.translate("StartWindow", u"Deep Learning", None))
    # retranslateUi

