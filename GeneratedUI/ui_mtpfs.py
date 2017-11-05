# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/ui_mtpfs.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mtpfs(object):
    def setupUi(self, mtpfs):
        mtpfs.setObjectName("mtpfs")
        mtpfs.resize(577, 463)
        self.gridLayout_2 = QtWidgets.QGridLayout(mtpfs)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Mount = QtWidgets.QPushButton(mtpfs)
        self.Mount.setObjectName("Mount")
        self.gridLayout_2.addWidget(self.Mount, 0, 0, 1, 1)
        self.Output = QtWidgets.QTextBrowser(mtpfs)
        self.Output.setObjectName("Output")
        self.gridLayout_2.addWidget(self.Output, 0, 1, 2, 1)
        self.Unmount = QtWidgets.QPushButton(mtpfs)
        self.Unmount.setEnabled(True)
        self.Unmount.setObjectName("Unmount")
        self.gridLayout_2.addWidget(self.Unmount, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.DevicePath = QtWidgets.QLabel(mtpfs)
        self.DevicePath.setObjectName("DevicePath")
        self.gridLayout.addWidget(self.DevicePath, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AndroidPath = QtWidgets.QLineEdit(mtpfs)
        self.AndroidPath.setObjectName("AndroidPath")
        self.horizontalLayout.addWidget(self.AndroidPath)
        self.ChoosePathAndroid = QtWidgets.QToolButton(mtpfs)
        self.ChoosePathAndroid.setObjectName("ChoosePathAndroid")
        self.horizontalLayout.addWidget(self.ChoosePathAndroid)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.MoveFileForward = QtWidgets.QPushButton(mtpfs)
        self.MoveFileForward.setText("")
        self.MoveFileForward.setObjectName("MoveFileForward")
        self.verticalLayout.addWidget(self.MoveFileForward)
        self.MoveFileBackward = QtWidgets.QPushButton(mtpfs)
        self.MoveFileBackward.setText("")
        self.MoveFileBackward.setObjectName("MoveFileBackward")
        self.verticalLayout.addWidget(self.MoveFileBackward)
        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.ComputerTree = QtWidgets.QTreeView(mtpfs)
        self.ComputerTree.setObjectName("ComputerTree")
        self.gridLayout.addWidget(self.ComputerTree, 3, 2, 1, 1)
        self.AndroidLabel = QtWidgets.QLabel(mtpfs)
        self.AndroidLabel.setObjectName("AndroidLabel")
        self.gridLayout.addWidget(self.AndroidLabel, 2, 0, 1, 1)
        self.ComputerLabel = QtWidgets.QLabel(mtpfs)
        self.ComputerLabel.setObjectName("ComputerLabel")
        self.gridLayout.addWidget(self.ComputerLabel, 2, 2, 1, 1)
        self.AndroidTree = QtWidgets.QTreeView(mtpfs)
        self.AndroidTree.setObjectName("AndroidTree")
        self.gridLayout.addWidget(self.AndroidTree, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)

        self.retranslateUi(mtpfs)
        QtCore.QMetaObject.connectSlotsByName(mtpfs)

    def retranslateUi(self, mtpfs):
        _translate = QtCore.QCoreApplication.translate
        mtpfs.setWindowTitle(_translate("mtpfs", "Mtpfs"))
        self.Mount.setText(_translate("mtpfs", "Mount"))
        self.Unmount.setText(_translate("mtpfs", "Unmount"))
        self.DevicePath.setText(_translate("mtpfs", "Mount folder for Android"))
        self.ChoosePathAndroid.setText(_translate("mtpfs", "..."))
        self.AndroidLabel.setText(_translate("mtpfs", "Android device"))
        self.ComputerLabel.setText(_translate("mtpfs", "Computer"))
