# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.wgt_main = QWidget(MainWindow)
        self.wgt_main.setObjectName(u"wgt_main")
        self.wgt_main.setStyleSheet(u"#frm_main{\n"
"background-color : #282828;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.wgt_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frm_main = QFrame(self.wgt_main)
        self.frm_main.setObjectName(u"frm_main")
        self.frm_main.setStyleSheet(u"")
        self.lyt_main = QVBoxLayout(self.frm_main)
        self.lyt_main.setObjectName(u"lyt_main")
        self.lyt_main.setContentsMargins(15, 15, 15, 15)
        self.frm_middle_content = QFrame(self.frm_main)
        self.frm_middle_content.setObjectName(u"frm_middle_content")
        self.frm_middle_content.setStyleSheet(u"#frm_left_menu{\n"
"background-color:#5d5d5d;\n"
"border: 1px solid white;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#frm_right_scene{\n"
"background-color:#5d5d5d;\n"
"border: 1px solid white;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#frm_left_menu_buttons QPushButton{\n"
" background-color: #FE6E00;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:20px;\n"
" border-color: white;\n"
"\n"
"}\n"
"\n"
"#frm_left_menu_buttons QPushButton:hover{\n"
" background-color: #FF8303;\n"
"\n"
"\n"
"}")
        self.lyt_middle_content = QHBoxLayout(self.frm_middle_content)
        self.lyt_middle_content.setSpacing(15)
        self.lyt_middle_content.setObjectName(u"lyt_middle_content")
        self.frm_left_menu = QFrame(self.frm_middle_content)
        self.frm_left_menu.setObjectName(u"frm_left_menu")
        self.frm_left_menu.setMinimumSize(QSize(120, 0))
        self.frm_left_menu.setMaximumSize(QSize(140, 16777215))
        self.lyt_left_menu = QVBoxLayout(self.frm_left_menu)
        self.lyt_left_menu.setObjectName(u"lyt_left_menu")
        self.lyt_left_menu.setContentsMargins(6, 6, 6, 6)
        self.frm_left_menu_buttons = QFrame(self.frm_left_menu)
        self.frm_left_menu_buttons.setObjectName(u"frm_left_menu_buttons")
        self.frm_left_menu_buttons.setFrameShape(QFrame.StyledPanel)
        self.frm_left_menu_buttons.setFrameShadow(QFrame.Raised)
        self.lyt_left_menu_buttons = QVBoxLayout(self.frm_left_menu_buttons)
        self.lyt_left_menu_buttons.setObjectName(u"lyt_left_menu_buttons")
        self.lyt_left_menu_buttons.setContentsMargins(0, 0, 0, 0)
        self.pbtn_menu_loadImage = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_loadImage.setObjectName(u"pbtn_menu_loadImage")
        self.pbtn_menu_loadImage.setMinimumSize(QSize(60, 40))
        self.pbtn_menu_loadImage.setStyleSheet(u"")

        self.lyt_left_menu_buttons.addWidget(self.pbtn_menu_loadImage)

        self.pbtn_menu_denoise = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_denoise.setObjectName(u"pbtn_menu_denoise")
        self.pbtn_menu_denoise.setMinimumSize(QSize(60, 40))

        self.lyt_left_menu_buttons.addWidget(self.pbtn_menu_denoise)

        self.pbtn_menu_segment = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_segment.setObjectName(u"pbtn_menu_segment")
        self.pbtn_menu_segment.setMinimumSize(QSize(60, 40))

        self.lyt_left_menu_buttons.addWidget(self.pbtn_menu_segment)

        self.pbtn_menu_skeletonize = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_skeletonize.setObjectName(u"pbtn_menu_skeletonize")
        self.pbtn_menu_skeletonize.setMinimumSize(QSize(60, 40))

        self.lyt_left_menu_buttons.addWidget(self.pbtn_menu_skeletonize)

        self.pbtn_menu_analyse = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_analyse.setObjectName(u"pbtn_menu_analyse")
        self.pbtn_menu_analyse.setMinimumSize(QSize(60, 40))

        self.lyt_left_menu_buttons.addWidget(self.pbtn_menu_analyse)

        self.pbtn_menu_report = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_report.setObjectName(u"pbtn_menu_report")
        self.pbtn_menu_report.setMinimumSize(QSize(60, 40))

        self.lyt_left_menu_buttons.addWidget(self.pbtn_menu_report)

        self.pbtn_menu_close = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_close.setObjectName(u"pbtn_menu_close")
        self.pbtn_menu_close.setMinimumSize(QSize(60, 40))

        self.lyt_left_menu_buttons.addWidget(self.pbtn_menu_close)


        self.lyt_left_menu.addWidget(self.frm_left_menu_buttons, 0, Qt.AlignTop)


        self.lyt_middle_content.addWidget(self.frm_left_menu)

        self.frm_right_scene = QFrame(self.frm_middle_content)
        self.frm_right_scene.setObjectName(u"frm_right_scene")
        self.lyt_right_scene = QVBoxLayout(self.frm_right_scene)
        self.lyt_right_scene.setObjectName(u"lyt_right_scene")
        self.frm_right_scene_content = QFrame(self.frm_right_scene)
        self.frm_right_scene_content.setObjectName(u"frm_right_scene_content")
        self.frm_right_scene_content.setFrameShape(QFrame.StyledPanel)
        self.frm_right_scene_content.setFrameShadow(QFrame.Raised)
        self.lyt_right_scene_content = QVBoxLayout(self.frm_right_scene_content)
        self.lyt_right_scene_content.setObjectName(u"lyt_right_scene_content")
        self.wgts_sceneContent = QStackedWidget(self.frm_right_scene_content)
        self.wgts_sceneContent.setObjectName(u"wgts_sceneContent")
        self.page_report = QWidget()
        self.page_report.setObjectName(u"page_report")
        self.verticalLayout_4 = QVBoxLayout(self.page_report)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_2 = QPushButton(self.page_report)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.wgts_sceneContent.addWidget(self.page_report)
        self.page_image_processing = QWidget()
        self.page_image_processing.setObjectName(u"page_image_processing")
        self.lyt_image_processing = QVBoxLayout(self.page_image_processing)
        self.lyt_image_processing.setObjectName(u"lyt_image_processing")
        self.lyt_image_processing.setContentsMargins(0, 0, 0, 0)
        self.frm_image_processing_content = QFrame(self.page_image_processing)
        self.frm_image_processing_content.setObjectName(u"frm_image_processing_content")
        self.frm_image_processing_content.setFrameShape(QFrame.StyledPanel)
        self.frm_image_processing_content.setFrameShadow(QFrame.Raised)
        self.lyt_image_processing_content = QVBoxLayout(self.frm_image_processing_content)
        self.lyt_image_processing_content.setObjectName(u"lyt_image_processing_content")
        self.lyt_image_processing_content.setContentsMargins(0, 0, 0, 0)
        self.frm_image = QFrame(self.frm_image_processing_content)
        self.frm_image.setObjectName(u"frm_image")
        self.frm_image.setMinimumSize(QSize(550, 500))
        self.frm_image.setFrameShape(QFrame.StyledPanel)
        self.frm_image.setFrameShadow(QFrame.Raised)
        self.lyt_image = QVBoxLayout(self.frm_image)
        self.lyt_image.setObjectName(u"lyt_image")
        self.lyt_image.setContentsMargins(0, 0, 0, 0)

        self.lyt_image_processing_content.addWidget(self.frm_image, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.lyt_image_processing.addWidget(self.frm_image_processing_content)

        self.wgts_sceneContent.addWidget(self.page_image_processing)

        self.lyt_right_scene_content.addWidget(self.wgts_sceneContent)


        self.lyt_right_scene.addWidget(self.frm_right_scene_content)


        self.lyt_middle_content.addWidget(self.frm_right_scene)


        self.lyt_main.addWidget(self.frm_middle_content)


        self.verticalLayout_2.addWidget(self.frm_main)

        MainWindow.setCentralWidget(self.wgt_main)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pbtn_menu_loadImage.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.pbtn_menu_denoise.setText(QCoreApplication.translate("MainWindow", u"Denoise", None))
        self.pbtn_menu_segment.setText(QCoreApplication.translate("MainWindow", u"Segment", None))
        self.pbtn_menu_skeletonize.setText(QCoreApplication.translate("MainWindow", u"Skeletonize", None))
        self.pbtn_menu_analyse.setText(QCoreApplication.translate("MainWindow", u"Analyse", None))
        self.pbtn_menu_report.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.pbtn_menu_close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

