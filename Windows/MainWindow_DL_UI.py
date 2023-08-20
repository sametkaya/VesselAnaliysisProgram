# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_DL_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow_DL(object):
    def setupUi(self, MainWindow_DL):
        if not MainWindow_DL.objectName():
            MainWindow_DL.setObjectName(u"MainWindow_DL")
        MainWindow_DL.resize(875, 818)
        MainWindow_DL.setAnimated(False)
        self.centralwidget = QWidget(MainWindow_DL)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frm_main = QFrame(self.centralwidget)
        self.frm_main.setObjectName(u"frm_main")
        self.frm_main.setStyleSheet(u"#frm_main{\n"
"background-color : #282828;\n"
"}")
        self.lyt_main_2 = QVBoxLayout(self.frm_main)
        self.lyt_main_2.setObjectName(u"lyt_main_2")
        self.lyt_main_2.setContentsMargins(15, 15, 15, 15)
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
"  background-color: #FE6E00;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:20px;\n"
" border-color: white;\n"
"}\n"
"#frm_left_menu_buttons_2 QPushButton:hover{\n"
" background-color: #FF8303;\n"
"}\n"
"#frm_left_menu_buttons QComboBox{\n"
"background-color: #FE6E00;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-color: white;\n"
"}\n"
"#frm_left_menu_buttons QComboBox:hover{\n"
" background-color: #FF8303;\n"
"}\n"
"")
        self.lyt_middle_content_2 = QHBoxLayout(self.frm_middle_content)
        self.lyt_middle_content_2.setSpacing(15)
        self.lyt_middle_content_2.setObjectName(u"lyt_middle_content_2")
        self.frm_left_menu = QFrame(self.frm_middle_content)
        self.frm_left_menu.setObjectName(u"frm_left_menu")
        self.frm_left_menu.setMinimumSize(QSize(140, 0))
        self.frm_left_menu.setMaximumSize(QSize(140, 16777215))
        self.lyt_left_menu_2 = QVBoxLayout(self.frm_left_menu)
        self.lyt_left_menu_2.setObjectName(u"lyt_left_menu_2")
        self.lyt_left_menu_2.setContentsMargins(6, 6, 6, 6)
        self.frm_left_menu_buttons = QFrame(self.frm_left_menu)
        self.frm_left_menu_buttons.setObjectName(u"frm_left_menu_buttons")
        self.frm_left_menu_buttons.setFrameShape(QFrame.StyledPanel)
        self.frm_left_menu_buttons.setFrameShadow(QFrame.Raised)
        self.lyt_left_menu_buttons_2 = QVBoxLayout(self.frm_left_menu_buttons)
        self.lyt_left_menu_buttons_2.setObjectName(u"lyt_left_menu_buttons_2")
        self.lyt_left_menu_buttons_2.setContentsMargins(0, 0, 0, 0)
        self.pbtn_menu_loadImage = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_loadImage.setObjectName(u"pbtn_menu_loadImage")
        self.pbtn_menu_loadImage.setMinimumSize(QSize(60, 40))
        self.pbtn_menu_loadImage.setStyleSheet(u"")

        self.lyt_left_menu_buttons_2.addWidget(self.pbtn_menu_loadImage)

        self.pbtn_menu_chooseMdl = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_chooseMdl.setObjectName(u"pbtn_menu_chooseMdl")
        self.pbtn_menu_chooseMdl.setMinimumSize(QSize(60, 40))
        self.pbtn_menu_chooseMdl.setMaximumSize(QSize(16777215, 16777215))
        self.pbtn_menu_chooseMdl.setStyleSheet(u" QPushButton{\n"
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

        self.lyt_left_menu_buttons_2.addWidget(self.pbtn_menu_chooseMdl)

        self.pbtn_menu_skeletonize = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_skeletonize.setObjectName(u"pbtn_menu_skeletonize")
        self.pbtn_menu_skeletonize.setMinimumSize(QSize(60, 40))

        self.lyt_left_menu_buttons_2.addWidget(self.pbtn_menu_skeletonize)

        self.pbtn_menu_analyse = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_analyse.setObjectName(u"pbtn_menu_analyse")
        self.pbtn_menu_analyse.setMinimumSize(QSize(60, 40))

        self.lyt_left_menu_buttons_2.addWidget(self.pbtn_menu_analyse)

        self.frm_left_menu_analyse = QFrame(self.frm_left_menu_buttons)
        self.frm_left_menu_analyse.setObjectName(u"frm_left_menu_analyse")
        self.frm_left_menu_analyse.setFrameShape(QFrame.StyledPanel)
        self.frm_left_menu_analyse.setFrameShadow(QFrame.Raised)
        self.lyt_left_menu_analyse_2 = QVBoxLayout(self.frm_left_menu_analyse)
        self.lyt_left_menu_analyse_2.setObjectName(u"lyt_left_menu_analyse_2")
        self.lyt_left_menu_analyse_2.setContentsMargins(0, 0, 0, 10)
        self.grpbx_analyse_branchPoint = QGroupBox(self.frm_left_menu_analyse)
        self.grpbx_analyse_branchPoint.setObjectName(u"grpbx_analyse_branchPoint")
        self.lyt_analyse_branchPoint_2 = QVBoxLayout(self.grpbx_analyse_branchPoint)
        self.lyt_analyse_branchPoint_2.setObjectName(u"lyt_analyse_branchPoint_2")
        self.lyt_analyse_branchPoint_2.setContentsMargins(1, 6, 1, 6)
        self.chbx_analyse_showBranchPoints = QCheckBox(self.grpbx_analyse_branchPoint)
        self.chbx_analyse_showBranchPoints.setObjectName(u"chbx_analyse_showBranchPoints")
        self.chbx_analyse_showBranchPoints.setChecked(True)

        self.lyt_analyse_branchPoint_2.addWidget(self.chbx_analyse_showBranchPoints)

        self.chbx_analyse_showBranchPointMarker = QCheckBox(self.grpbx_analyse_branchPoint)
        self.chbx_analyse_showBranchPointMarker.setObjectName(u"chbx_analyse_showBranchPointMarker")
        self.chbx_analyse_showBranchPointMarker.setChecked(True)

        self.lyt_analyse_branchPoint_2.addWidget(self.chbx_analyse_showBranchPointMarker)

        self.chbx_analyse_showBranchPointCenter = QCheckBox(self.grpbx_analyse_branchPoint)
        self.chbx_analyse_showBranchPointCenter.setObjectName(u"chbx_analyse_showBranchPointCenter")
        self.chbx_analyse_showBranchPointCenter.setChecked(True)

        self.lyt_analyse_branchPoint_2.addWidget(self.chbx_analyse_showBranchPointCenter)


        self.lyt_left_menu_analyse_2.addWidget(self.grpbx_analyse_branchPoint)

        self.grpbx_analyse_tipPoint = QGroupBox(self.frm_left_menu_analyse)
        self.grpbx_analyse_tipPoint.setObjectName(u"grpbx_analyse_tipPoint")
        self.lyt_analyse_tipPoint_2 = QVBoxLayout(self.grpbx_analyse_tipPoint)
        self.lyt_analyse_tipPoint_2.setObjectName(u"lyt_analyse_tipPoint_2")
        self.lyt_analyse_tipPoint_2.setContentsMargins(1, 6, 1, 6)
        self.chbx_analyse_showTipPoints = QCheckBox(self.grpbx_analyse_tipPoint)
        self.chbx_analyse_showTipPoints.setObjectName(u"chbx_analyse_showTipPoints")
        self.chbx_analyse_showTipPoints.setChecked(True)

        self.lyt_analyse_tipPoint_2.addWidget(self.chbx_analyse_showTipPoints)

        self.chbx_analyse_showTipPointMarker = QCheckBox(self.grpbx_analyse_tipPoint)
        self.chbx_analyse_showTipPointMarker.setObjectName(u"chbx_analyse_showTipPointMarker")
        self.chbx_analyse_showTipPointMarker.setChecked(True)

        self.lyt_analyse_tipPoint_2.addWidget(self.chbx_analyse_showTipPointMarker)

        self.chbx_analyse_showTipPointCenter = QCheckBox(self.grpbx_analyse_tipPoint)
        self.chbx_analyse_showTipPointCenter.setObjectName(u"chbx_analyse_showTipPointCenter")
        self.chbx_analyse_showTipPointCenter.setChecked(True)

        self.lyt_analyse_tipPoint_2.addWidget(self.chbx_analyse_showTipPointCenter)


        self.lyt_left_menu_analyse_2.addWidget(self.grpbx_analyse_tipPoint)

        self.grpbx_analyse_branchPath = QGroupBox(self.frm_left_menu_analyse)
        self.grpbx_analyse_branchPath.setObjectName(u"grpbx_analyse_branchPath")
        self.lyt_analyse_branchPath_2 = QVBoxLayout(self.grpbx_analyse_branchPath)
        self.lyt_analyse_branchPath_2.setObjectName(u"lyt_analyse_branchPath_2")
        self.lyt_analyse_branchPath_2.setContentsMargins(1, 6, 1, 6)
        self.chbx_analyse_showBranchPaths = QCheckBox(self.grpbx_analyse_branchPath)
        self.chbx_analyse_showBranchPaths.setObjectName(u"chbx_analyse_showBranchPaths")
        self.chbx_analyse_showBranchPaths.setChecked(True)

        self.lyt_analyse_branchPath_2.addWidget(self.chbx_analyse_showBranchPaths)

        self.chbx_analyse_showBranchPathId = QCheckBox(self.grpbx_analyse_branchPath)
        self.chbx_analyse_showBranchPathId.setObjectName(u"chbx_analyse_showBranchPathId")
        self.chbx_analyse_showBranchPathId.setChecked(True)

        self.lyt_analyse_branchPath_2.addWidget(self.chbx_analyse_showBranchPathId)

        self.chbx_analyse_showBranchPathLenght = QCheckBox(self.grpbx_analyse_branchPath)
        self.chbx_analyse_showBranchPathLenght.setObjectName(u"chbx_analyse_showBranchPathLenght")
        self.chbx_analyse_showBranchPathLenght.setChecked(True)

        self.lyt_analyse_branchPath_2.addWidget(self.chbx_analyse_showBranchPathLenght)


        self.lyt_left_menu_analyse_2.addWidget(self.grpbx_analyse_branchPath)


        self.lyt_left_menu_buttons_2.addWidget(self.frm_left_menu_analyse)

        self.pbtn_menu_report = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_report.setObjectName(u"pbtn_menu_report")
        self.pbtn_menu_report.setMinimumSize(QSize(60, 40))

        self.lyt_left_menu_buttons_2.addWidget(self.pbtn_menu_report)

        self.pbtn_menu_close = QPushButton(self.frm_left_menu_buttons)
        self.pbtn_menu_close.setObjectName(u"pbtn_menu_close")
        self.pbtn_menu_close.setMinimumSize(QSize(60, 40))

        self.lyt_left_menu_buttons_2.addWidget(self.pbtn_menu_close)


        self.lyt_left_menu_2.addWidget(self.frm_left_menu_buttons)


        self.lyt_middle_content_2.addWidget(self.frm_left_menu)

        self.frm_right_scene = QFrame(self.frm_middle_content)
        self.frm_right_scene.setObjectName(u"frm_right_scene")
        self.lyt_right_scene_2 = QVBoxLayout(self.frm_right_scene)
        self.lyt_right_scene_2.setObjectName(u"lyt_right_scene_2")
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
        self.lyt_right_scene_content_2 = QVBoxLayout(self.frm_right_scene_content)
        self.lyt_right_scene_content_2.setObjectName(u"lyt_right_scene_content_2")
        self.wdgt_dl_models = QWidget(self.frm_right_scene_content)
        self.wdgt_dl_models.setObjectName(u"wdgt_dl_models")
        self.horizontalLayout = QHBoxLayout(self.wdgt_dl_models)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cmbbx_dl_models = QComboBox(self.wdgt_dl_models)
        self.cmbbx_dl_models.addItem("")
        self.cmbbx_dl_models.addItem("")
        self.cmbbx_dl_models.addItem("")
        self.cmbbx_dl_models.addItem("")
        self.cmbbx_dl_models.addItem("")
        self.cmbbx_dl_models.setObjectName(u"cmbbx_dl_models")
        self.cmbbx_dl_models.setMinimumSize(QSize(140, 22))
        self.cmbbx_dl_models.setStyleSheet(u"background-color:rgb(167, 167, 167)")

        self.horizontalLayout.addWidget(self.cmbbx_dl_models)

        self.spcr_wdgt_dl_models = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spcr_wdgt_dl_models)


        self.lyt_right_scene_content_2.addWidget(self.wdgt_dl_models)

        self.wgts_sceneContent = QStackedWidget(self.frm_right_scene_content)
        self.wgts_sceneContent.setObjectName(u"wgts_sceneContent")
        sizePolicy.setHeightForWidth(self.wgts_sceneContent.sizePolicy().hasHeightForWidth())
        self.wgts_sceneContent.setSizePolicy(sizePolicy)
        self.page_report = QWidget()
        self.page_report.setObjectName(u"page_report")
        self.verticalLayout_5 = QVBoxLayout(self.page_report)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.hrzntl_page_report = QHBoxLayout()
        self.hrzntl_page_report.setObjectName(u"hrzntl_page_report")
        self.pbtn_prev_page = QPushButton(self.page_report)
        self.pbtn_prev_page.setObjectName(u"pbtn_prev_page")
        self.pbtn_prev_page.setStyleSheet(u"background-color: #282828;\n"
"color:white;\n"
"")

        self.hrzntl_page_report.addWidget(self.pbtn_prev_page)

        self.spcr_page_report = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hrzntl_page_report.addItem(self.spcr_page_report)

        self.pbtn_next_page = QPushButton(self.page_report)
        self.pbtn_next_page.setObjectName(u"pbtn_next_page")
        self.pbtn_next_page.setStyleSheet(u"background-color: #282828;\n"
"color:white;\n"
"")

        self.hrzntl_page_report.addWidget(self.pbtn_next_page)


        self.verticalLayout_5.addLayout(self.hrzntl_page_report)

        self.page_report_lwdgt = QWidget(self.page_report)
        self.page_report_lwdgt.setObjectName(u"page_report_lwdgt")
        self.verticalLayout_8 = QVBoxLayout(self.page_report_lwdgt)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.report_widget = QWidget(self.page_report_lwdgt)
        self.report_widget.setObjectName(u"report_widget")
        self.gridLayout_2 = QGridLayout(self.report_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pdf_view = QGraphicsView(self.report_widget)
        self.pdf_view.setObjectName(u"pdf_view")

        self.gridLayout_2.addWidget(self.pdf_view, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.report_widget)


        self.verticalLayout_5.addWidget(self.page_report_lwdgt)

        self.wgts_sceneContent.addWidget(self.page_report)
        self.page_image_processing = QWidget()
        self.page_image_processing.setObjectName(u"page_image_processing")
        sizePolicy.setHeightForWidth(self.page_image_processing.sizePolicy().hasHeightForWidth())
        self.page_image_processing.setSizePolicy(sizePolicy)
        self.lyt_image_processing_2 = QVBoxLayout(self.page_image_processing)
        self.lyt_image_processing_2.setObjectName(u"lyt_image_processing_2")
        self.lyt_image_processing_2.setContentsMargins(0, 0, 0, 0)
        self.frm_image_processing_content = QFrame(self.page_image_processing)
        self.frm_image_processing_content.setObjectName(u"frm_image_processing_content")
        self.frm_image_processing_content.setStyleSheet(u"background-color:#3A3A3A;")
        self.frm_image_processing_content.setFrameShape(QFrame.StyledPanel)
        self.frm_image_processing_content.setFrameShadow(QFrame.Raised)
        self.lyt_image_processing_content_2 = QVBoxLayout(self.frm_image_processing_content)
        self.lyt_image_processing_content_2.setObjectName(u"lyt_image_processing_content_2")
        self.lyt_image_processing_content_2.setContentsMargins(0, 0, 0, 0)

        self.lyt_image_processing_2.addWidget(self.frm_image_processing_content)

        self.wgts_sceneContent.addWidget(self.page_image_processing)
        self.page_select_report_options = QWidget()
        self.page_select_report_options.setObjectName(u"page_select_report_options")
        self.verticalLayout = QVBoxLayout(self.page_select_report_options)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.wdgt_select_report_options = QWidget(self.page_select_report_options)
        self.wdgt_select_report_options.setObjectName(u"wdgt_select_report_options")
        self.gridLayout = QGridLayout(self.wdgt_select_report_options)
        self.gridLayout.setObjectName(u"gridLayout")
        self.grpbx_report_options = QGroupBox(self.wdgt_select_report_options)
        self.grpbx_report_options.setObjectName(u"grpbx_report_options")
        self.grpbx_report_options.setMinimumSize(QSize(0, 400))
        self.grpbx_report_options.setMaximumSize(QSize(16777215, 400))
        self.verticalLayout_6 = QVBoxLayout(self.grpbx_report_options)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 6, 1, 6)
        self.wdgt_checkBoxes = QWidget(self.grpbx_report_options)
        self.wdgt_checkBoxes.setObjectName(u"wdgt_checkBoxes")
        self.horizontalLayout_2 = QHBoxLayout(self.wdgt_checkBoxes)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.wdgt_options_right = QWidget(self.wdgt_checkBoxes)
        self.wdgt_options_right.setObjectName(u"wdgt_options_right")
        self.verticalLayout_4 = QVBoxLayout(self.wdgt_options_right)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_report_veinSEP = QCheckBox(self.wdgt_options_right)
        self.checkBox_report_veinSEP.setObjectName(u"checkBox_report_veinSEP")
        self.checkBox_report_veinSEP.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkBox_report_veinSEP)

        self.checkBox_report_vSEPType = QCheckBox(self.wdgt_options_right)
        self.checkBox_report_vSEPType.setObjectName(u"checkBox_report_vSEPType")
        self.checkBox_report_vSEPType.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkBox_report_vSEPType)

        self.checkBox_report_vCount = QCheckBox(self.wdgt_options_right)
        self.checkBox_report_vCount.setObjectName(u"checkBox_report_vCount")
        self.checkBox_report_vCount.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkBox_report_vCount)

        self.checkBox_report_tvLength = QCheckBox(self.wdgt_options_right)
        self.checkBox_report_tvLength.setObjectName(u"checkBox_report_tvLength")
        self.checkBox_report_tvLength.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkBox_report_tvLength)


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


        self.gridLayout.addWidget(self.grpbx_report_options, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.wdgt_select_report_options)

        self.wgts_sceneContent.addWidget(self.page_select_report_options)

        self.lyt_right_scene_content_2.addWidget(self.wgts_sceneContent)


        self.lyt_right_scene_2.addWidget(self.frm_right_scene_content)


        self.lyt_middle_content_2.addWidget(self.frm_right_scene)


        self.lyt_main_2.addWidget(self.frm_middle_content)


        self.gridLayout_3.addWidget(self.frm_main, 0, 0, 1, 1)

        MainWindow_DL.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_DL)

        self.wgts_sceneContent.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow_DL)
    # setupUi

    def retranslateUi(self, MainWindow_DL):
        MainWindow_DL.setWindowTitle(QCoreApplication.translate("MainWindow_DL", u"Brain Vasculyzer - Deep Learning", None))
        self.pbtn_menu_loadImage.setText(QCoreApplication.translate("MainWindow_DL", u"Load Image", None))
        self.pbtn_menu_chooseMdl.setText(QCoreApplication.translate("MainWindow_DL", u"Choose Model", None))
        self.pbtn_menu_skeletonize.setText(QCoreApplication.translate("MainWindow_DL", u"Skeletonize", None))
        self.pbtn_menu_analyse.setText(QCoreApplication.translate("MainWindow_DL", u"Analyse", None))
        self.grpbx_analyse_branchPoint.setTitle(QCoreApplication.translate("MainWindow_DL", u"Branch Points", None))
        self.chbx_analyse_showBranchPoints.setText(QCoreApplication.translate("MainWindow_DL", u"Show Points", None))
        self.chbx_analyse_showBranchPointMarker.setText(QCoreApplication.translate("MainWindow_DL", u"Show Marker", None))
        self.chbx_analyse_showBranchPointCenter.setText(QCoreApplication.translate("MainWindow_DL", u"Show Center", None))
        self.grpbx_analyse_tipPoint.setTitle(QCoreApplication.translate("MainWindow_DL", u"Tip Points", None))
        self.chbx_analyse_showTipPoints.setText(QCoreApplication.translate("MainWindow_DL", u"Show Points", None))
        self.chbx_analyse_showTipPointMarker.setText(QCoreApplication.translate("MainWindow_DL", u"Show Marker", None))
        self.chbx_analyse_showTipPointCenter.setText(QCoreApplication.translate("MainWindow_DL", u"Show Center", None))
        self.grpbx_analyse_branchPath.setTitle(QCoreApplication.translate("MainWindow_DL", u"Branch Paths", None))
        self.chbx_analyse_showBranchPaths.setText(QCoreApplication.translate("MainWindow_DL", u"Show Paths", None))
        self.chbx_analyse_showBranchPathId.setText(QCoreApplication.translate("MainWindow_DL", u"Show Id", None))
        self.chbx_analyse_showBranchPathLenght.setText(QCoreApplication.translate("MainWindow_DL", u"Show Lenght", None))
        self.pbtn_menu_report.setText(QCoreApplication.translate("MainWindow_DL", u"Report", None))
        self.pbtn_menu_close.setText(QCoreApplication.translate("MainWindow_DL", u"Close", None))
        self.cmbbx_dl_models.setItemText(0, QCoreApplication.translate("MainWindow_DL", u"UNet", None))
        self.cmbbx_dl_models.setItemText(1, QCoreApplication.translate("MainWindow_DL", u"ResNet", None))
        self.cmbbx_dl_models.setItemText(2, QCoreApplication.translate("MainWindow_DL", u"Model3", None))
        self.cmbbx_dl_models.setItemText(3, QCoreApplication.translate("MainWindow_DL", u"Model4", None))
        self.cmbbx_dl_models.setItemText(4, QCoreApplication.translate("MainWindow_DL", u"Model5", None))

        self.pbtn_prev_page.setText(QCoreApplication.translate("MainWindow_DL", u"Previous", None))
        self.pbtn_next_page.setText(QCoreApplication.translate("MainWindow_DL", u"Next", None))
        self.grpbx_report_options.setTitle(QCoreApplication.translate("MainWindow_DL", u"Options", None))
        self.checkBox_report_veinSEP.setText(QCoreApplication.translate("MainWindow_DL", u"vein start/end points", None))
        self.checkBox_report_vSEPType.setText(QCoreApplication.translate("MainWindow_DL", u"vein start/end point types", None))
        self.checkBox_report_vCount.setText(QCoreApplication.translate("MainWindow_DL", u"vein count", None))
        self.checkBox_report_tvLength.setText(QCoreApplication.translate("MainWindow_DL", u"total vein length", None))
        self.checkBox_report_tpCount.setText(QCoreApplication.translate("MainWindow_DL", u"tip point count", None))
        self.checkBox_report_evLength.setText(QCoreApplication.translate("MainWindow_DL", u"length of each vein", None))
        self.checkBox_report_bpCount.setText(QCoreApplication.translate("MainWindow_DL", u"branch points count", None))
        self.checkBox_report_avLength.setText(QCoreApplication.translate("MainWindow_DL", u"average vein length", None))
        self.pbtn_create_pdf.setText(QCoreApplication.translate("MainWindow_DL", u"Create PDF", None))
    # retranslateUi

