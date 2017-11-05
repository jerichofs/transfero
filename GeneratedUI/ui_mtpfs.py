# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/ui_mtpfs.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mptfs(object):
    def setupUi(self, mptfs):
        mptfs.setObjectName("mptfs")
        mptfs.resize(577, 463)
        self.gridLayout_2 = QtWidgets.QGridLayout(mptfs)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Mount = QtWidgets.QPushButton(mptfs)
        self.Mount.setObjectName("Mount")
        self.gridLayout_2.addWidget(self.Mount, 0, 0, 1, 1)
        self.Output = QtWidgets.QTextBrowser(mptfs)
        self.Output.setObjectName("Output")
        self.gridLayout_2.addWidget(self.Output, 0, 1, 2, 1)
        self.Unmount = QtWidgets.QPushButton(mptfs)
        self.Unmount.setEnabled(True)
        self.Unmount.setObjectName("Unmount")
        self.gridLayout_2.addWidget(self.Unmount, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.DevicePath = QtWidgets.QLabel(mptfs)
        self.DevicePath.setObjectName("DevicePath")
        self.gridLayout.addWidget(self.DevicePath, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AndroidPath = QtWidgets.QLineEdit(mptfs)
        self.AndroidPath.setObjectName("AndroidPath")
        self.horizontalLayout.addWidget(self.AndroidPath)
        self.ChoosePathAndroid = QtWidgets.QToolButton(mptfs)
        self.ChoosePathAndroid.setObjectName("ChoosePathAndroid")
        self.horizontalLayout.addWidget(self.ChoosePathAndroid)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.MoveFileForward = QtWidgets.QPushButton(mptfs)
        self.MoveFileForward.setText("")
        self.MoveFileForward.setObjectName("MoveFileForward")
        self.verticalLayout.addWidget(self.MoveFileForward)
        self.MoveFileBackward = QtWidgets.QPushButton(mptfs)
        self.MoveFileBackward.setText("")
        self.MoveFileBackward.setObjectName("MoveFileBackward")
        self.verticalLayout.addWidget(self.MoveFileBackward)
        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.ComputerTree = QtWidgets.QTreeView(mptfs)
        self.ComputerTree.setObjectName("ComputerTree")
        self.gridLayout.addWidget(self.ComputerTree, 3, 2, 1, 1)
        self.AndroidLabel = QtWidgets.QLabel(mptfs)
        self.AndroidLabel.setObjectName("AndroidLabel")
        self.gridLayout.addWidget(self.AndroidLabel, 2, 0, 1, 1)
        self.ComputerLabel = QtWidgets.QLabel(mptfs)
        self.ComputerLabel.setObjectName("ComputerLabel")
        self.gridLayout.addWidget(self.ComputerLabel, 2, 2, 1, 1)
        self.AndroidTree = QtWidgets.QTreeView(mptfs)
        self.AndroidTree.setObjectName("AndroidTree")
        self.gridLayout.addWidget(self.AndroidTree, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)

        self.retranslateUi(mptfs)
        QtCore.QMetaObject.connectSlotsByName(mptfs)

    def retranslateUi(self, mptfs):
        _translate = QtCore.QCoreApplication.translate
        mptfs.setWindowTitle(_translate("mptfs", "Mtpfs"))
        self.Mount.setText(_translate("mptfs", "Mount"))
        self.Unmount.setText(_translate("mptfs", "Unmount"))
        self.DevicePath.setText(_translate("mptfs", "Mount folder for Android"))
        self.ChoosePathAndroid.setText(_translate("mptfs", "..."))
        self.AndroidLabel.setText(_translate("mptfs", "Android device"))
        self.ComputerLabel.setText(_translate("mptfs", "Computer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mptfs = QtWidgets.QWidget()
    ui = Ui_mptfs()
    ui.setupUi(mptfs)
    mptfs.show()
    sys.exit(app.exec_())

