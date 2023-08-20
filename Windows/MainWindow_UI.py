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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGraphicsView,
    QGridLayout, QGroupBox, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(760, 768)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
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
"}")
        self.lyt_middle_content = QHBoxLayout(self.frm_middle_content)
        self.lyt_middle_content.setSpacing(15)
        self.lyt_middle_content.setObjectName(u"lyt_middle_content")
        self.frm_left_menu = QFrame(self.frm_middle_content)
        self.frm_left_menu.setObjectName(u"frm_left_menu")
        self.frm_left_menu.setMinimumSize(QSize(140, 0))
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

        self.frm_left_menu_analyse = QFrame(self.frm_left_menu_buttons)
        self.frm_left_menu_analyse.setObjectName(u"frm_left_menu_analyse")
        self.frm_left_menu_analyse.setFrameShape(QFrame.StyledPanel)
        self.frm_left_menu_analyse.setFrameShadow(QFrame.Raised)
        self.lyt_left_menu_analyse = QVBoxLayout(self.frm_left_menu_analyse)
        self.lyt_left_menu_analyse.setObjectName(u"lyt_left_menu_analyse")
        self.lyt_left_menu_analyse.setContentsMargins(0, 0, 0, 10)
        self.grpbx_analyse_branchPoint = QGroupBox(self.frm_left_menu_analyse)
        self.grpbx_analyse_branchPoint.setObjectName(u"grpbx_analyse_branchPoint")
        self.lyt_analyse_branchPoint = QVBoxLayout(self.grpbx_analyse_branchPoint)
        self.lyt_analyse_branchPoint.setObjectName(u"lyt_analyse_branchPoint")
        self.lyt_analyse_branchPoint.setContentsMargins(1, 6, 1, 6)
        self.chbx_analyse_showBranchPoints = QCheckBox(self.grpbx_analyse_branchPoint)
        self.chbx_analyse_showBranchPoints.setObjectName(u"chbx_analyse_showBranchPoints")
        self.chbx_analyse_showBranchPoints.setChecked(True)

        self.lyt_analyse_branchPoint.addWidget(self.chbx_analyse_showBranchPoints)

        self.chbx_analyse_showBranchPointMarker = QCheckBox(self.grpbx_analyse_branchPoint)
        self.chbx_analyse_showBranchPointMarker.setObjectName(u"chbx_analyse_showBranchPointMarker")
        self.chbx_analyse_showBranchPointMarker.setChecked(True)

        self.lyt_analyse_branchPoint.addWidget(self.chbx_analyse_showBranchPointMarker)

        self.chbx_analyse_showBranchPointCenter = QCheckBox(self.grpbx_analyse_branchPoint)
        self.chbx_analyse_showBranchPointCenter.setObjectName(u"chbx_analyse_showBranchPointCenter")
        self.chbx_analyse_showBranchPointCenter.setChecked(True)

        self.lyt_analyse_branchPoint.addWidget(self.chbx_analyse_showBranchPointCenter)


        self.lyt_left_menu_analyse.addWidget(self.grpbx_analyse_branchPoint)

        self.grpbx_analyse_tipPoint = QGroupBox(self.frm_left_menu_analyse)
        self.grpbx_analyse_tipPoint.setObjectName(u"grpbx_analyse_tipPoint")
        self.lyt_analyse_tipPoint = QVBoxLayout(self.grpbx_analyse_tipPoint)
        self.lyt_analyse_tipPoint.setObjectName(u"lyt_analyse_tipPoint")
        self.lyt_analyse_tipPoint.setContentsMargins(1, 6, 1, 6)
        self.chbx_analyse_showTipPoints = QCheckBox(self.grpbx_analyse_tipPoint)
        self.chbx_analyse_showTipPoints.setObjectName(u"chbx_analyse_showTipPoints")
        self.chbx_analyse_showTipPoints.setChecked(True)

        self.lyt_analyse_tipPoint.addWidget(self.chbx_analyse_showTipPoints)

        self.chbx_analyse_showTipPointMarker = QCheckBox(self.grpbx_analyse_tipPoint)
        self.chbx_analyse_showTipPointMarker.setObjectName(u"chbx_analyse_showTipPointMarker")
        self.chbx_analyse_showTipPointMarker.setChecked(True)

        self.lyt_analyse_tipPoint.addWidget(self.chbx_analyse_showTipPointMarker)

        self.chbx_analyse_showTipPointCenter = QCheckBox(self.grpbx_analyse_tipPoint)
        self.chbx_analyse_showTipPointCenter.setObjectName(u"chbx_analyse_showTipPointCenter")
        self.chbx_analyse_showTipPointCenter.setChecked(True)

        self.lyt_analyse_tipPoint.addWidget(self.chbx_analyse_showTipPointCenter)


        self.lyt_left_menu_analyse.addWidget(self.grpbx_analyse_tipPoint)

        self.grpbx_analyse_branchPath = QGroupBox(self.frm_left_menu_analyse)
        self.grpbx_analyse_branchPath.setObjectName(u"grpbx_analyse_branchPath")
        self.lyt_analyse_branchPath = QVBoxLayout(self.grpbx_analyse_branchPath)
        self.lyt_analyse_branchPath.setObjectName(u"lyt_analyse_branchPath")
        self.lyt_analyse_branchPath.setContentsMargins(1, 6, 1, 6)
        self.chbx_analyse_showBranchPaths = QCheckBox(self.grpbx_analyse_branchPath)
        self.chbx_analyse_showBranchPaths.setObjectName(u"chbx_analyse_showBranchPaths")
        self.chbx_analyse_showBranchPaths.setChecked(True)

        self.lyt_analyse_branchPath.addWidget(self.chbx_analyse_showBranchPaths)

        self.chbx_analyse_showBranchPathId = QCheckBox(self.grpbx_analyse_branchPath)
        self.chbx_analyse_showBranchPathId.setObjectName(u"chbx_analyse_showBranchPathId")
        self.chbx_analyse_showBranchPathId.setChecked(True)

        self.lyt_analyse_branchPath.addWidget(self.chbx_analyse_showBranchPathId)

        self.chbx_analyse_showBranchPathLenght = QCheckBox(self.grpbx_analyse_branchPath)
        self.chbx_analyse_showBranchPathLenght.setObjectName(u"chbx_analyse_showBranchPathLenght")
        self.chbx_analyse_showBranchPathLenght.setChecked(True)

        self.lyt_analyse_branchPath.addWidget(self.chbx_analyse_showBranchPathLenght)


        self.lyt_left_menu_analyse.addWidget(self.grpbx_analyse_branchPath)


        self.lyt_left_menu_buttons.addWidget(self.frm_left_menu_analyse)

        self.pbtn_menu_report = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_report.setObjectName(u"pbtn_menu_report")
        self.pbtn_menu_report.setMinimumSize(QSize(60, 40))

        self.lyt_left_menu_buttons.addWidget(self.pbtn_menu_report)

        self.pbtn_menu_close = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_close.setObjectName(u"pbtn_menu_close")
        self.pbtn_menu_close.setMinimumSize(QSize(60, 40))

        self.lyt_left_menu_buttons.addWidget(self.pbtn_menu_close)


        self.lyt_left_menu.addWidget(self.frm_left_menu_buttons)


        self.lyt_middle_content.addWidget(self.frm_left_menu)

        self.frm_right_scene = QFrame(self.frm_middle_content)
        self.frm_right_scene.setObjectName(u"frm_right_scene")
        self.lyt_right_scene = QVBoxLayout(self.frm_right_scene)
        self.lyt_right_scene.setObjectName(u"lyt_right_scene")
        self.frm_right_scene_content = QFrame(self.frm_right_scene)
        self.frm_right_scene_content.setObjectName(u"frm_right_scene_content")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_right_scene_content.sizePolicy().hasHeightForWidth())
        self.frm_right_scene_content.setSizePolicy(sizePolicy)
        self.frm_right_scene_content.setStyleSheet(u"background-color:#525052;")
        self.frm_right_scene_content.setFrameShape(QFrame.StyledPanel)
        self.frm_right_scene_content.setFrameShadow(QFrame.Raised)
        self.lyt_right_scene_content = QVBoxLayout(self.frm_right_scene_content)
        self.lyt_right_scene_content.setObjectName(u"lyt_right_scene_content")
        self.wgts_sceneContent = QStackedWidget(self.frm_right_scene_content)
        self.wgts_sceneContent.setObjectName(u"wgts_sceneContent")
        sizePolicy.setHeightForWidth(self.wgts_sceneContent.sizePolicy().hasHeightForWidth())
        self.wgts_sceneContent.setSizePolicy(sizePolicy)
        self.page_report = QWidget()
        self.page_report.setObjectName(u"page_report")
        self.page_report.setStyleSheet(u"#horizontalLayout QPushButton:hover{\n"
" background-color: #282828;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.page_report)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pbtn_prev_page = QPushButton(self.page_report)
        self.pbtn_prev_page.setObjectName(u"pbtn_prev_page")
        self.pbtn_prev_page.setStyleSheet(u"background-color: #282828;\n"
"color:white;")

        self.horizontalLayout.addWidget(self.pbtn_prev_page)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pbtn_next_page = QPushButton(self.page_report)
        self.pbtn_next_page.setObjectName(u"pbtn_next_page")
        self.pbtn_next_page.setStyleSheet(u"background-color: #282828;\n"
"color:white;\n"
"")

        self.horizontalLayout.addWidget(self.pbtn_next_page)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.page_report_lwdgt = QWidget(self.page_report)
        self.page_report_lwdgt.setObjectName(u"page_report_lwdgt")
        self.verticalLayout_7 = QVBoxLayout(self.page_report_lwdgt)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.report_widget = QWidget(self.page_report_lwdgt)
        self.report_widget.setObjectName(u"report_widget")
        self.gridLayout = QGridLayout(self.report_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pdf_view = QGraphicsView(self.report_widget)
        self.pdf_view.setObjectName(u"pdf_view")

        self.gridLayout.addWidget(self.pdf_view, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.report_widget)


        self.verticalLayout_4.addWidget(self.page_report_lwdgt)

        self.wgts_sceneContent.addWidget(self.page_report)
        self.page_select_report_options = QWidget()
        self.page_select_report_options.setObjectName(u"page_select_report_options")
        self.verticalLayout = QVBoxLayout(self.page_select_report_options)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.wdgt_select_report_options = QWidget(self.page_select_report_options)
        self.wdgt_select_report_options.setObjectName(u"wdgt_select_report_options")
        self.gridLayout_2 = QGridLayout(self.wdgt_select_report_options)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.grpbx_report_options = QGroupBox(self.wdgt_select_report_options)
        self.grpbx_report_options.setObjectName(u"grpbx_report_options")
        self.grpbx_report_options.setMinimumSize(QSize(0, 400))
        self.grpbx_report_options.setMaximumSize(QSize(16777215, 400))
        self.verticalLayout_6 = QVBoxLayout(self.grpbx_report_options)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.wdgt_checkBoxes = QWidget(self.grpbx_report_options)
        self.wdgt_checkBoxes.setObjectName(u"wdgt_checkBoxes")
        self.horizontalLayout_2 = QHBoxLayout(self.wdgt_checkBoxes)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.wdgt_options_right = QWidget(self.wdgt_checkBoxes)
        self.wdgt_options_right.setObjectName(u"wdgt_options_right")
        self.verticalLayout_5 = QVBoxLayout(self.wdgt_options_right)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_report_veinSEP = QCheckBox(self.wdgt_options_right)
        self.checkBox_report_veinSEP.setObjectName(u"checkBox_report_veinSEP")
        self.checkBox_report_veinSEP.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBox_report_veinSEP)

        self.checkBox_report_vSEPType = QCheckBox(self.wdgt_options_right)
        self.checkBox_report_vSEPType.setObjectName(u"checkBox_report_vSEPType")
        self.checkBox_report_vSEPType.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBox_report_vSEPType)

        self.checkBox_report_vCount = QCheckBox(self.wdgt_options_right)
        self.checkBox_report_vCount.setObjectName(u"checkBox_report_vCount")
        self.checkBox_report_vCount.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBox_report_vCount)

        self.checkBox_report_tvLength = QCheckBox(self.wdgt_options_right)
        self.checkBox_report_tvLength.setObjectName(u"checkBox_report_tvLength")
        self.checkBox_report_tvLength.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBox_report_tvLength)


        self.horizontalLayout_2.addWidget(self.wdgt_options_right)

        self.wdgt_options_left = QWidget(self.wdgt_checkBoxes)
        self.wdgt_options_left.setObjectName(u"wdgt_options_left")
        self.verticalLayout_3 = QVBoxLayout(self.wdgt_options_left)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_report_tpCount = QCheckBox(self.wdgt_options_left)
        self.checkBox_report_tpCount.setObjectName(u"checkBox_report_tpCount")
        self.checkBox_report_tpCount.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_report_tpCount)

        self.checkBox_report_evLength = QCheckBox(self.wdgt_options_left)
        self.checkBox_report_evLength.setObjectName(u"checkBox_report_evLength")
        self.checkBox_report_evLength.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_report_evLength)

        self.checkBox_report_bpCount = QCheckBox(self.wdgt_options_left)
        self.checkBox_report_bpCount.setObjectName(u"checkBox_report_bpCount")
        self.checkBox_report_bpCount.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_report_bpCount)

        self.checkBox_report_avLength = QCheckBox(self.wdgt_options_left)
        self.checkBox_report_avLength.setObjectName(u"checkBox_report_avLength")
        self.checkBox_report_avLength.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_report_avLength)


        self.horizontalLayout_2.addWidget(self.wdgt_options_left)


        self.verticalLayout_6.addWidget(self.wdgt_checkBoxes)

        self.wdgt_btn = QWidget(self.grpbx_report_options)
        self.wdgt_btn.setObjectName(u"wdgt_btn")
        self.wdgt_btn.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_3 = QHBoxLayout(self.wdgt_btn)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pbtn_create_pdf = QPushButton(self.wdgt_btn)
        self.pbtn_create_pdf.setObjectName(u"pbtn_create_pdf")
        self.pbtn_create_pdf.setMinimumSize(QSize(60, 40))
        self.pbtn_create_pdf.setMaximumSize(QSize(200, 40))
        self.pbtn_create_pdf.setStyleSheet(u" QPushButton{\n"
" background-color: #FE6E00;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:20px;\n"
" border-color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: #FF8303;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pbtn_create_pdf)


        self.verticalLayout_6.addWidget(self.wdgt_btn)


        self.gridLayout_2.addWidget(self.grpbx_report_options, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.wdgt_select_report_options)

        self.wgts_sceneContent.addWidget(self.page_select_report_options)
        self.page_image_processing = QWidget()
        self.page_image_processing.setObjectName(u"page_image_processing")
        sizePolicy.setHeightForWidth(self.page_image_processing.sizePolicy().hasHeightForWidth())
        self.page_image_processing.setSizePolicy(sizePolicy)
        self.lyt_image_processing = QVBoxLayout(self.page_image_processing)
        self.lyt_image_processing.setObjectName(u"lyt_image_processing")
        self.lyt_image_processing.setContentsMargins(0, 0, 0, 0)
        self.frm_image_processing_content = QFrame(self.page_image_processing)
        self.frm_image_processing_content.setObjectName(u"frm_image_processing_content")
        self.frm_image_processing_content.setStyleSheet(u"background-color:#3A3A3A;")
        self.frm_image_processing_content.setFrameShape(QFrame.StyledPanel)
        self.frm_image_processing_content.setFrameShadow(QFrame.Raised)
        self.lyt_image_processing_content = QVBoxLayout(self.frm_image_processing_content)
        self.lyt_image_processing_content.setObjectName(u"lyt_image_processing_content")
        self.lyt_image_processing_content.setContentsMargins(0, 0, 0, 0)

        self.lyt_image_processing.addWidget(self.frm_image_processing_content)

        self.wgts_sceneContent.addWidget(self.page_image_processing)

        self.lyt_right_scene_content.addWidget(self.wgts_sceneContent)


        self.lyt_right_scene.addWidget(self.frm_right_scene_content)


        self.lyt_middle_content.addWidget(self.frm_right_scene)


        self.lyt_main.addWidget(self.frm_middle_content)


        self.verticalLayout_2.addWidget(self.frm_main)

        MainWindow.setCentralWidget(self.wgt_main)

        self.retranslateUi(MainWindow)

        self.wgts_sceneContent.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Brain Vasculyzer - Image Processing", None))
        self.pbtn_menu_loadImage.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.pbtn_menu_denoise.setText(QCoreApplication.translate("MainWindow", u"Denoise", None))
        self.pbtn_menu_segment.setText(QCoreApplication.translate("MainWindow", u"Segment", None))
        self.pbtn_menu_skeletonize.setText(QCoreApplication.translate("MainWindow", u"Skeletonize", None))
        self.pbtn_menu_analyse.setText(QCoreApplication.translate("MainWindow", u"Analyse", None))
        self.grpbx_analyse_branchPoint.setTitle(QCoreApplication.translate("MainWindow", u"Branch Points", None))
        self.chbx_analyse_showBranchPoints.setText(QCoreApplication.translate("MainWindow", u"Show Points", None))
        self.chbx_analyse_showBranchPointMarker.setText(QCoreApplication.translate("MainWindow", u"Show Marker", None))
        self.chbx_analyse_showBranchPointCenter.setText(QCoreApplication.translate("MainWindow", u"Show Center", None))
        self.grpbx_analyse_tipPoint.setTitle(QCoreApplication.translate("MainWindow", u"Tip Points", None))
        self.chbx_analyse_showTipPoints.setText(QCoreApplication.translate("MainWindow", u"Show Points", None))
        self.chbx_analyse_showTipPointMarker.setText(QCoreApplication.translate("MainWindow", u"Show Marker", None))
        self.chbx_analyse_showTipPointCenter.setText(QCoreApplication.translate("MainWindow", u"Show Center", None))
        self.grpbx_analyse_branchPath.setTitle(QCoreApplication.translate("MainWindow", u"Branch Paths", None))
        self.chbx_analyse_showBranchPaths.setText(QCoreApplication.translate("MainWindow", u"Show Paths", None))
        self.chbx_analyse_showBranchPathId.setText(QCoreApplication.translate("MainWindow", u"Show Id", None))
        self.chbx_analyse_showBranchPathLenght.setText(QCoreApplication.translate("MainWindow", u"Show Lenght", None))
        self.pbtn_menu_report.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.pbtn_menu_close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pbtn_prev_page.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.pbtn_next_page.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.grpbx_report_options.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.checkBox_report_veinSEP.setText(QCoreApplication.translate("MainWindow", u"vein start/end points", None))
        self.checkBox_report_vSEPType.setText(QCoreApplication.translate("MainWindow", u"vein start/end point types", None))
        self.checkBox_report_vCount.setText(QCoreApplication.translate("MainWindow", u"vein count", None))
        self.checkBox_report_tvLength.setText(QCoreApplication.translate("MainWindow", u"total vein length", None))
        self.checkBox_report_tpCount.setText(QCoreApplication.translate("MainWindow", u"tip point count", None))
        self.checkBox_report_evLength.setText(QCoreApplication.translate("MainWindow", u"length of each vein", None))
        self.checkBox_report_bpCount.setText(QCoreApplication.translate("MainWindow", u"branch points count", None))
        self.checkBox_report_avLength.setText(QCoreApplication.translate("MainWindow", u"average vein length", None))
        self.pbtn_create_pdf.setText(QCoreApplication.translate("MainWindow", u"Create PDF", None))
    # retranslateUi

