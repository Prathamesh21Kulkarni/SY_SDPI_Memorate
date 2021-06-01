# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtWidgets import QMessageBox, QStyle, QFileDialog


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 589, 396))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_5)
        self.scrollArea_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea_4.setStyleSheet("color: white;\n"
                                        "font-style : Bold;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.926136 rgba(28, 79, 201, 255));")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 313, 394))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.scrollArea = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea.setStyleSheet("background-color: rgb(0, 39, 117);\n"
                                      "font-family: verdana;\n"
                                      "color:black;\n"
                                      "font: 25 10pt \"Bahnschrift Light\";\n"
                                      "border: 2px solid ;\n"
                                      "border-color: rgb(97, 24, 206);\n"
                                      "border-radius: 5px;\n"
                                      "")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 290, 378))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 39, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 39, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 39, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 39, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 39, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 39, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 39, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 39, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 39, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("#tab{\n"
                                     "background-color: rgb(0, 39, 117);\n"
                                     "font-family: verdana;\n"
                                     "color:black;\n"
                                     "font: 25 10pt \"Bahnschrift Light\";\n"
                                     "border: 2px solid ;\n"
                                     "border-color: rgb(97, 24, 206);\n"
                                     "border-radius: 5px;\n"
                                     "}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setTabletTracking(True)
        self.tab.setAcceptDrops(True)
        self.tab.setAutoFillBackground(False)
        self.tab.setStyleSheet("\n"
                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(49, 63, 171, 255), stop:0.55 rgba(10, 20, 105, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
                               "font-family: verdana;\n"
                               "color:white;\n"
                               "font: 25 10pt \"Bahnschrift Light\";\n"
                               "border: 2px solid ;\n"
                               "border-color: rgb(97, 24, 206);\n"
                               "border-radius: 2px;\n"
                               "\n"
                               "")
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Input_text = QtWidgets.QPlainTextEdit(self.tab)
        self.Input_text.setAutoFillBackground(False)
        self.Input_text.setStyleSheet("\n"
                                      "background-color: rgb(0, 0, 78);\n"
                                      "font-family: verdana;\n"
                                      "color:white;\n"
                                      "font: 25 10pt \"Bahnschrift Light\";\n"
                                      "border: 2px solid ;\n"
                                      "border-color: rgb(97, 24, 206);\n"
                                      "border-radius: 5px;\n"
                                      "\n"
                                      "")
        self.Input_text.setPlainText("")
        self.Input_text.setObjectName("Input_text")
        self.verticalLayout_5.addWidget(self.Input_text)
        self.Ok_Button = QtWidgets.QPushButton(self.tab)
        self.Ok_Button.setObjectName("Ok_Button")
        self.Ok_Button.clicked.connect(self.ok_clicked)
        self.verticalLayout_5.addWidget(self.Ok_Button)
        self.Cancel_Button = QtWidgets.QPushButton(self.tab)
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.verticalLayout_5.addWidget(self.Cancel_Button)
        self.Cancel_Button.clicked.connect(self.cancel_clicked)
        self.verticalLayout_5.addWidget(self.Cancel_Button)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Output_Text = QtWidgets.QPlainTextEdit(self.tab_2)
        self.Output_Text.setAutoFillBackground(False)
        self.Output_Text.setStyleSheet("background-color: rgb(0, 0, 78);\n"
                                       "\n"
                                       "font-family: verdana;\n"
                                       "color:white;\n"
                                       "font: 25 10pt \"Bahnschrift Light\";\n"
                                       "text-align : center;\n"
                                       "font: 12pt \"Italic\";\n"
                                       "border: 2px solid ;\n"
                                       "border-color: rgb(97, 24, 206);\n"
                                       "border-radius: 5px;\n"
                                       "\n"
                                       "")
        self.Output_Text.setPlainText("")
        self.Output_Text.setObjectName("Output_Text")
        self.horizontalLayout_2.addWidget(self.Output_Text)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_8.addWidget(self.scrollArea)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_8.addWidget(self.line_2)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_10.addWidget(self.scrollArea_4)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_5)
        self.scrollArea_3.setStyleSheet("color: white;\n"
                                        "font-style : Bold;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.926136 rgba(28, 79, 201, 255));")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 268, 394))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(49, 63, 171, 255), stop:0.55 rgba(10, 20, 105, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font-family: verdana;\n"
            "color:white;\n"
            "font: 25 10pt \"Bahnschrift Light\";\n"
            "border: 2px solid ;\n"
            "border-color: rgb(97, 24, 206);\n"
            "border-radius: 5px;\n"
            "")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_7.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_7)
        self.scrollArea_2.setStyleSheet("background-color: rgb(0, 39, 117);\n"
                                        "font-family: verdana;\n"
                                        "color:black;\n"
                                        "font: 25 10pt \"Bahnschrift Light\";\n"
                                        "border: 2px solid ;\n"
                                        "border-color: rgb(97, 24, 206);\n"
                                        "border-radius: 0.5px;\n"
                                        "")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 108, 308))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: white;\n"
                                    "font-style : Bold;\n"
                                    "background-color: rgb(0, 0, 78);")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(-1, 25, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(-1, 6, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setStyleSheet("border-radius : 5px; border-color :rgb(0, 0, 78); ")
        self.pushButton_2.setIcon(QIcon("loop.png"))
        # self.pushButton_2.setIcon(self.style())
        self.pushButton_2.setFixedSize(50, 50)
        size = QSize(45, 45)
        self.pushButton_2.setIconSize(size)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setStyleSheet("border-radius : 5px; border-color :rgb(0, 0, 78); ")
        self.pushButton.setIcon(QIcon("play2.png"))
        self.pushButton.setFixedSize(50, 50)
        size = QSize(50, 50)
        self.pushButton.setIconSize(size)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        # self.pushButton.clicked.connect(self.play_1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setStyleSheet("border-color :rgb(0, 0, 78);")
        self.gridLayout.addWidget(self.horizontalSlider, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setStyleSheet("border-radius : 5px; border-color :rgb(0, 0, 78); ")
        self.pushButton_4.setIcon(QIcon("loop.png"))
        self.pushButton_4.setFixedSize(50, 50)
        size = QSize(45, 45)
        self.pushButton_4.setIconSize(size)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setStyleSheet("border-radius : 5px; border-color :rgb(0, 0, 78); ")
        self.pushButton_3.setIcon(QIcon("play2.png"))
        self.pushButton_3.setFixedSize(50, 50)
        size = QSize(50, 50)
        self.pushButton_3.setIconSize(size)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setStyleSheet("border-color :rgb(0, 0, 78);")
        self.gridLayout_2.addWidget(self.horizontalSlider_2, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setStyleSheet("border-radius : 5px; border-color :rgb(0, 0, 78); ")
        self.pushButton_5.setIcon(QIcon("play2.png"))
        self.pushButton_5.setFixedSize(50, 50)
        size = QSize(50, 50)
        self.pushButton_5.setIconSize(size)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_6.setStyleSheet("border-radius : 5px; border-color :rgb(0, 0, 78); ")
        self.pushButton_6.setIcon(QIcon("loop.png"))
        self.pushButton_6.setFixedSize(50, 50)
        size = QSize(45, 45)
        self.pushButton_6.setIconSize(size)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 2, 1, 1)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.groupBox_4)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.setStyleSheet("border-color :rgb(0, 0, 78);")
        self.gridLayout_3.addWidget(self.horizontalSlider_3, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_7.setStyleSheet("border-radius : 5px; border-color :rgb(0, 0, 78); ")
        self.pushButton_7.setIcon(QIcon("play2.png"))
        self.pushButton_7.setFixedSize(50, 50)
        size = QSize(50, 50)
        self.pushButton_7.setIconSize(size)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_4.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_8.setStyleSheet("border-radius : 5px; border-color :rgb(0, 0, 78); ")
        self.pushButton_8.setIcon(QIcon("loop.png"))
        self.pushButton_8.setFixedSize(50, 50)
        size = QSize(45, 45)
        self.pushButton_8.setIconSize(size)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 2, 1, 1)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.groupBox_5)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_4.setStyleSheet("border-color :rgb(0, 0, 78);")
        self.gridLayout_4.addWidget(self.horizontalSlider_4, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_9.addWidget(self.scrollArea_2)
        self.scrollArea_6 = QtWidgets.QScrollArea(self.groupBox_7)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 132, 343))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_8 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_8.setStyleSheet("background-color: rgb(0, 0, 78);")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_5.setContentsMargins(-1, 15, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 2, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setStyleSheet("border-radius : 5px; border-color :rgb(0, 0, 78); ")
        self.pushButton_10.setIcon(QIcon("rec_start.png"))
        self.pushButton_10.setFixedSize(50, 50)
        size = QSize(45, 45)
        self.pushButton_10.setIconSize(size)
        self.gridLayout_6.addWidget(self.pushButton_10, 0, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_9.setStyleSheet("border-radius : 5px;")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setStyleSheet("border-radius : 5px; border-color :rgb(0, 0, 78); ")
        self.pushButton_9.setIcon(QIcon("rec_stop.png"))
        self.pushButton_9.setFixedSize(50, 50)
        size = QSize(40, 40)
        self.pushButton_9.setIconSize(size)
        self.gridLayout_6.addWidget(self.pushButton_9, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 0, 2, 1, 1)
        self.horizontalSlider_5 = QtWidgets.QSlider(self.groupBox_9)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.gridLayout_6.addWidget(self.horizontalSlider_5, 2, 0, 1, 3)
        self.gridLayout_5.addWidget(self.groupBox_9, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_8)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_9.addWidget(self.scrollArea_6)
        self.horizontalLayout_7.addWidget(self.groupBox_7)
        self.horizontalLayout_6.addWidget(self.groupBox_6)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_10.addWidget(self.scrollArea_3)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_2.addWidget(self.scrollArea_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 20))
        self.menubar.setStyleSheet("background-color: Black;\n"
                                   "font-family: verdana;\n"
                                   "color:white;\n"
                                   "font: 25 10pt \"Bahnschrift Light\";\n"
                                   "border: 2px solid ;\n"
                                   "border-color: rgb(97, 24, 206);\n"
                                   "border-radius: 5px;\n"
                                   "")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: Black; color: White;")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setShortcutVisibleInContextMenu(True)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setShortcutVisibleInContextMenu(True)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setShortcutVisibleInContextMenu(True)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setShortcutVisibleInContextMenu(True)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setShortcutVisibleInContextMenu(True)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setShortcutVisibleInContextMenu(True)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def ok_clicked(self):
        text = self.Input_text.toPlainText()
        if len(text.split()) >= 20:
            self.Info_Box_Ok_1()
            # self.Info_Box_Ok_2()
        else:
            self.Info_Box_Not_Ok()

    def cancel_clicked(self):
        self.Input_text.clear()
        self.Output_Text.clear()
    def Info_Box_Ok_1(self):
        reply = QMessageBox.question(self, 'Summarize', 'Do you want to summarize the text?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.Summary_plus_verse()
        else:
            self.Only_verse()
    def Only_verse(self):
        from verse2 import Verse2
        text = self.Input_text.toPlainText()
        final_text = Verse2(text)
        for each_line in final_text:
            each_line = each_line.replace('[', '')
            each_line = each_line.replace(']', '')
            each_line = each_line.replace("'", '')
            each_line = each_line.replace(',', '')
            each_line = each_line.replace('''"''', '')
            self.Output_Text.appendPlainText(each_line)
            self.Output_Text.appendPlainText(" ")
    def Summary_plus_verse(self):
        from verse2 import Verse2
        from Summarizer import summary
        text = self.Input_text.toPlainText()
        summarized_text = summary(text)
        final_text = Verse2(summarized_text)
        for each_line in final_text:
            each_line = each_line.replace('[', '')
            each_line = each_line.replace(']', '')
            each_line = each_line.replace("'", '')
            each_line = each_line.replace(',', '')
            each_line = each_line.replace('''"''', '')
            self.Output_Text.appendPlainText(each_line)
            self.Output_Text.appendPlainText(" ")
    def Info_Box_Ok_2(self):
        infoBox_2 = QMessageBox()
        infoBox_2.setIcon(QMessageBox.Information)
        infoBox_2.setText("Done 👍! Check the Output Tab")
        infoBox_2.setWindowTitle("Memorate Says...")
        infoBox_2.setStandardButtons(QMessageBox.Ok)
        infoBox_2.setEscapeButton(QMessageBox.Close)
        infoBox_2.exec_()

    def Info_Box_Not_Ok(self):
        infoBox_3 = QMessageBox()
        infoBox_3.setIcon(QMessageBox.Critical)
        infoBox_3.setText("Input less than 20 words")
        infoBox_3.setWindowTitle("Memorate Says...")
        infoBox_3.setDetailedText("Your text must be greater than 20 words")
        infoBox_3.setStandardButtons(QMessageBox.Ok)
        infoBox_3.setEscapeButton(QMessageBox.Close)
        infoBox_3.exec_()
        self.Input_text.setPlainText(" ")
        self.Output_Text.setPlainText(" ")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Input_text.setPlaceholderText(_translate("MainWindow", "Write Your Text Here"))
        self.Ok_Button.setText(_translate("MainWindow", "Ok"))
        self.Cancel_Button.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Input"))
        self.Output_Text.setPlaceholderText(_translate("MainWindow", "First type your input in input tab"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Output"))
        self.groupBox.setTitle(_translate("MainWindow", "Playback music"))
        self.groupBox_2.setTitle(_translate("MainWindow", "First Song"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Second  Song"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Third Song"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Fourth Song"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Recordings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionOpen_File.setStatusTip(_translate("MainWindow", "Open another file"))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_File.triggered.connect(self.Open_file)
        # self.actionNew_FIle.setText(_translate("MainWindow", "New FIle"))
        # self.actionNew_FIle.setStatusTip(_translate("MainWindow", "Creates a new file"))
        # self.actionNew_FIle.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Saves the File"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave.triggered.connect(self.file_save)
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave_as.setStatusTip(_translate("MainWindow", "Save as.."))
        self.actionSave_as.triggered.connect(self.file_saveas)
        # self.actionPrint.setText(_translate("MainWindow", "Print"))
        # self.actionPrint.setStatusTip(_translate("MainWindow", "Print the file"))
        # self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setStatusTip(_translate("MainWindow", "Undo 1 step"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setStatusTip(_translate("MainWindow", "Redo 1 step"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy selected areas"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.pushButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.pushButton.setStyleSheet("background-color : white;border-radius : 25%;")
        self.pushButton_3.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.pushButton_3.setStyleSheet("background-color : white;border-radius : 25%;")
        self.pushButton_5.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.pushButton_5.setStyleSheet("background-color : white;border-radius : 25%;")
        self.pushButton_7.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.pushButton_7.setStyleSheet("background-color : white;border-radius : 25%;")
        self.pushButton_2.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.pushButton_2.setStyleSheet("background-color : white;border-radius : 25%;")
        self.pushButton_4.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.pushButton_4.setStyleSheet("background-color : white;border-radius : 25%;")
        self.pushButton_6.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.pushButton_6.setStyleSheet("background-color : white;border-radius : 25%;")
        self.pushButton_8.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.pushButton_8.setStyleSheet("background-color : white;border-radius : 25%;")
        self.pushButton_9.setIcon(QIcon("rec_start.png"))
        self.pushButton_10.setIcon(QIcon("rec_stop.png"))
        # ---------------------First---------------------------------------------
        self.horizontalSlider.sliderMoved.connect(self.set_position_1)
        self.url = QtCore.QUrl.fromLocalFile('music_1.mp3')
        self.content = QtMultimedia.QMediaContent(self.url)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)
        self.pushButton.clicked.connect(self.play_audio_1)
        self.pushButton_2.clicked.connect(self.stop_1)
        self.player.stateChanged.connect(self.mediastate_changed_1)
        self.player.positionChanged.connect(self.position_changed_1)
        self.player.durationChanged.connect(self.duration_changed_1)
        # ------------------------Second------------------------------------------
        self.horizontalSlider_2.sliderMoved.connect(self.set_position_2)
        self.url_1 = QtCore.QUrl.fromLocalFile('music_2.mp3')
        self.content_1 = QtMultimedia.QMediaContent(self.url_1)
        self.player_1 = QtMultimedia.QMediaPlayer()
        self.player_1.setMedia(self.content_1)
        self.pushButton_3.clicked.connect(self.play_audio_2)
        self.pushButton_4.clicked.connect(self.stop_2)
        self.player_1.stateChanged.connect(self.mediastate_changed_2)
        self.player_1.positionChanged.connect(self.position_changed_2)
        self.player_1.durationChanged.connect(self.duration_changed_2)
        # -------------------------Third-----------------------------------------
        self.horizontalSlider_3.sliderMoved.connect(self.set_position_3)
        self.url_2 = QtCore.QUrl.fromLocalFile('music_3.mp3')
        self.content_2 = QtMultimedia.QMediaContent(self.url_2)
        self.player_2 = QtMultimedia.QMediaPlayer()
        self.player_2.setMedia(self.content_2)
        self.pushButton_5.clicked.connect(self.play_audio_3)
        self.pushButton_6.clicked.connect(self.stop_3)
        self.player_2.stateChanged.connect(self.mediastate_changed_3)
        self.player_2.positionChanged.connect(self.position_changed_3)
        self.player_2.durationChanged.connect(self.duration_changed_3)
        # --------------------------Fourth----------------------------------------
        self.horizontalSlider_4.sliderMoved.connect(self.set_position_4)
        self.url_3 = QtCore.QUrl.fromLocalFile('music_4.mp3')
        self.content_3 = QtMultimedia.QMediaContent(self.url_3)
        self.player_3 = QtMultimedia.QMediaPlayer()
        self.player_3.setMedia(self.content_3)
        self.pushButton_7.clicked.connect(self.play_audio_4)
        self.pushButton_8.clicked.connect(self.stop_4)
        self.player_3.stateChanged.connect(self.mediastate_changed_4)
        self.player_3.positionChanged.connect(self.position_changed_4)
        self.player_3.durationChanged.connect(self.duration_changed_4)
        # ------------------------------Record_Button------------------------------------
        # self.pushButton_9.clicked.connect(self.record)
        # self.pushButton_10.clicked.connect(self.stop_record)
    # -----------------------------------------------------------------------------
    def play_audio_1(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    # def play_1(self):
    #     self.player.play()

    def stop_1(self):
        self.player.pause()
        # self.pushButton_2.isEnabled(False)
        self.pushButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.player.setPosition(0)

    def mediastate_changed_1(self, state):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.pushButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.pushButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def set_position_1(self, position):
        self.player.setPosition(position)

    def position_changed_1(self, position):
        self.horizontalSlider.setValue(position)

    def duration_changed_1(self, duration):
        self.horizontalSlider.setRange(0, duration)

    # -----------------------------------------------------------------------------
    def play_audio_2(self):
        if self.player_1.state() == QMediaPlayer.PlayingState:
            self.player_1.pause()
        else:
            self.player_1.play()

    # def play_1(self):
    #     self.player.play()

    def stop_2(self):
        self.player_1.pause()
        # self.pushButton_2.isEnabled(False)
        self.pushButton_3.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.player_1.setPosition(0)

    def mediastate_changed_2(self, state):
        if self.player_1.state() == QMediaPlayer.PlayingState:
            self.pushButton_3.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.pushButton_3.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def set_position_2(self, position):
        self.player_1.setPosition(position)

    def position_changed_2(self, position):
        self.horizontalSlider_2.setValue(position)

    def duration_changed_2(self, duration):
        self.horizontalSlider_2.setRange(0, duration)

# -----------------------------------------------------------------------------
    def play_audio_3(self):
            if self.player_2.state() == QMediaPlayer.PlayingState:
                self.player_2.pause()
            else:
                self.player_2.play()

        # def play_1(self):
        #     self.player.play()

    def stop_3(self):
            self.player_2.pause()
            # self.pushButton_2.isEnabled(False)
            self.pushButton_5.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.player_2.setPosition(0)

    def mediastate_changed_3(self, state):
            if self.player_2.state() == QMediaPlayer.PlayingState:
                self.pushButton_5.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            else:
                self.pushButton_5.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def set_position_3(self, position):
            self.player_2.setPosition(position)

    def position_changed_3(self, position):
            self.horizontalSlider_3.setValue(position)

    def duration_changed_3(self, duration):
            self.horizontalSlider_3.setRange(0, duration)

        # -----------------------------------------------------------------------------
    def play_audio_4(self):
            if self.player_3.state() == QMediaPlayer.PlayingState:
                self.player_3.pause()
            else:
                self.player_3.play()

        # def play_1(self):
        #     self.player.play()

    def stop_4(self):
            self.player_3.pause()
            # self.pushButton_2.isEnabled(False)
            self.pushButton_7.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.player_3.setPosition(0)

    def mediastate_changed_4(self, state):
            if self.player_3.state() == QMediaPlayer.PlayingState:
                self.pushButton_7.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            else:
                self.pushButton_7.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def set_position_4(self, position):
            self.player_3.setPosition(position)

    def position_changed_4(self, position):
            self.horizontalSlider_4.setValue(position)

    def duration_changed_4(self, duration):
            self.horizontalSlider_4.setRange(0, duration)

    def record(self):
        import sounddevice
        from scipy.io.wavfile import write
        fs = 44100
        second = 180
        record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
        sounddevice.wait()
        write("output.mp3", fs, record_voice)
    def stop_record(self):
        print("hi")
    def Open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")

        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()

            except Exception as e:
                self.dialog_critical(str(e))

            else:
                self.path = path
                self.Input_text.setPlainText(text)

    def file_save(self):
        if self.path is None:
            # If we do not have a path, we need to use Save As.
            return self.file_saveas()

        self._save_to_path(self.path)

    def file_saveas(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files (*.*)")

        if not path:
            # If dialog is cancelled, will return ''
            return

        self._save_to_path(self.path)

    def _save_to_path(self, path):
        text = self.Output_Text.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_title()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
