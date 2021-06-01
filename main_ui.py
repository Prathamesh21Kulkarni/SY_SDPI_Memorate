# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtWidgets import QMessageBox, QStyle
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
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
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 464, 349))
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
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 259, 347))
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 236, 331))
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
        self.Input_text.setStyleSheet("#plainTextEdit{\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(49, 63, 171, 255), stop:0.55 rgba(10, 20, 105, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
                                      "font-family: verdana;\n"
                                      "color:white;\n"
                                      "font: 25 10pt \"Bahnschrift Light\";\n"
                                      "border: 2px solid ;\n"
                                      "border-color: rgb(97, 24, 206);\n"
                                      "border-radius: 5px;\n"
                                      "\n"
                                      "}\n"
                                      "#\n"
                                      "{background-color: rgb(45, 0, 82);}    ")
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
        self.Cancel_Button.clicked.connect(self.cancel_cliked)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Output_Text = QtWidgets.QPlainTextEdit(self.tab_2)
        self.Output_Text.setAutoFillBackground(False)
        self.Output_Text.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(49, 63, 171, 255), stop:0.55 rgba(10, 20, 105, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font-family: verdana;\n"
            "color:white;\n"
            '''font: 25 10pt "Bahnschrift Light";\n'''
            "text-align : center;\n"
            '''font: 12pt "Italic" "Bold";\n'''
            "border: 2px solid ;\n"
            "border-color: rgb(97, 24, 206);\n"
            "border-radius: 5px;\n"
            )
        self.Output_Text.setPlainText("")
        self.Output_Text.setPlaceholderText("")
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
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 197, 347))
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
        self.horizontalLayout_9.setContentsMargins(-1, 15, 8, 8)
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
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 104, 261))
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
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.926136 rgba(28, 79, 201, 255));")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(-1, 6, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setStyleSheet("border-radius : 5px;")
        self.pushButton.setIcon(QIcon("play1.png"))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setStyleSheet("border-radius : 5px;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setStyleSheet("border-radius : 5px;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_7.setStyleSheet("border-radius : 5px;")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_4.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_9.addWidget(self.scrollArea_2)
        self.scrollArea_6 = QtWidgets.QScrollArea(self.groupBox_7)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 88, 261))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_8 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_5.setContentsMargins(-1, 15, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_9.setStyleSheet("border-radius : 5px;")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_5.addWidget(self.pushButton_9, 0, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_5.addWidget(self.pushButton_10, 0, 1, 1, 1)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 20))
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
        self.statusbar.setStyleSheet("background-color: Black;")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setShortcutVisibleInContextMenu(True)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionNew_FIle = QtWidgets.QAction(MainWindow)
        self.actionNew_FIle.setShortcutVisibleInContextMenu(True)
        self.actionNew_FIle.setObjectName("actionNew_FIle")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setShortcutVisibleInContextMenu(True)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setShortcutVisibleInContextMenu(True)
        self.actionPrint.setObjectName("actionPrint")
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
        self.menuFile.addAction(self.actionNew_FIle)
        self.menuFile.addAction(self.actionPrint)
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
        text_for_verse = self.Input_text.toPlainText()
        if len(text_for_verse.split()) >= 20:
            self.Info_Box_Ok()
        else:
            self.Info_Box_Not_Ok()
        self.Info_Box_Ok()
        from Verse import verse
        final_text = verse(text_for_verse)
        for each_line in final_text:
            each_line = each_line.replace('[', '')
            each_line = each_line.replace(']', '')
            each_line = each_line.replace("'", '')
            each_line = each_line.replace(',', '')
            each_line = each_line.replace('''"''', '')
            self.Output_Text.appendPlainText("| " + each_line + " ||")
            self.Output_Text.appendPlainText(" ")

    def cancel_clicked(self):
        self.Input_text.clear()
        self.Output_Text.clear()

    def Info_Box_Ok(self):
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText("Check the Output Tab")
        infoBox.setWindowTitle("Memorate Says...")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.setEscapeButton(QMessageBox.Close)
        infoBox.exec_()

    def Info_Box_Not_Ok(self):
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Critical)
        infoBox.setText("Input less than 20 words")
        infoBox.setWindowTitle("Memorate Says...")
        infoBox.setDetailedText("Your text must be greater than 20 words")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.setEscapeButton(QMessageBox.Close)
        infoBox.exec_()
        self.Input_text.setPlainText(" ")
        self.Output_Text.setPlainText(" ")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Memorate"))
        self.Input_text.setPlaceholderText(_translate("MainWindow", "Write Your Text Here"))
        self.Ok_Button.setText(_translate("MainWindow", "Ok"))
        self.Cancel_Button.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Input"))
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
        self.actionNew_FIle.setText(_translate("MainWindow", "New FIle"))
        self.actionNew_FIle.setStatusTip(_translate("MainWindow", "Creates a new file"))
        self.actionNew_FIle.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Saves the File"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave_as.setStatusTip(_translate("MainWindow", "Save as.."))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setStatusTip(_translate("MainWindow", "Print the file"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
