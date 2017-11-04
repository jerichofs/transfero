# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_jmtpfs.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_jmtpfs(object):
    def setupUi(self, jmtpfs):
        jmtpfs.setObjectName("jmtpfs")
        jmtpfs.resize(577, 463)
        self.gridLayout_2 = QtWidgets.QGridLayout(jmtpfs)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Mount = QtWidgets.QPushButton(jmtpfs)
        self.Mount.setObjectName("Mount")
        self.gridLayout_2.addWidget(self.Mount, 0, 0, 1, 1)
        self.Output = QtWidgets.QTextBrowser(jmtpfs)
        self.Output.setObjectName("Output")
        self.gridLayout_2.addWidget(self.Output, 0, 1, 2, 1)
        self.Umount = QtWidgets.QPushButton(jmtpfs)
        self.Umount.setEnabled(True)
        self.Umount.setObjectName("Umount")
        self.gridLayout_2.addWidget(self.Umount, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.DevicePath = QtWidgets.QLabel(jmtpfs)
        self.DevicePath.setObjectName("DevicePath")
        self.gridLayout.addWidget(self.DevicePath, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AndroidPath = QtWidgets.QLineEdit(jmtpfs)
        self.AndroidPath.setObjectName("AndroidPath")
        self.horizontalLayout.addWidget(self.AndroidPath)
        self.ChoosePathAndroid = QtWidgets.QToolButton(jmtpfs)
        self.ChoosePathAndroid.setObjectName("ChoosePathAndroid")
        self.horizontalLayout.addWidget(self.ChoosePathAndroid)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.MoveFileForward = QtWidgets.QPushButton(jmtpfs)
        self.MoveFileForward.setText("")
        self.MoveFileForward.setObjectName("MoveFileForward")
        self.verticalLayout.addWidget(self.MoveFileForward)
        self.MoveFileBackward = QtWidgets.QPushButton(jmtpfs)
        self.MoveFileBackward.setText("")
        self.MoveFileBackward.setObjectName("MoveFileBackward")
        self.verticalLayout.addWidget(self.MoveFileBackward)
        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.ComputerTree = QtWidgets.QTreeView(jmtpfs)
        self.ComputerTree.setObjectName("ComputerTree")
        self.gridLayout.addWidget(self.ComputerTree, 3, 2, 1, 1)
        self.AndroidLabel = QtWidgets.QLabel(jmtpfs)
        self.AndroidLabel.setObjectName("AndroidLabel")
        self.gridLayout.addWidget(self.AndroidLabel, 2, 0, 1, 1)
        self.ComputerLabel = QtWidgets.QLabel(jmtpfs)
        self.ComputerLabel.setObjectName("ComputerLabel")
        self.gridLayout.addWidget(self.ComputerLabel, 2, 2, 1, 1)
        self.AndroidTree = QtWidgets.QTreeView(jmtpfs)
        self.AndroidTree.setObjectName("AndroidTree")
        self.gridLayout.addWidget(self.AndroidTree, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)

        self.retranslateUi(jmtpfs)
        QtCore.QMetaObject.connectSlotsByName(jmtpfs)

    def retranslateUi(self, jmtpfs):
        _translate = QtCore.QCoreApplication.translate
        jmtpfs.setWindowTitle(_translate("jmtpfs", "jmtpfs"))
        self.Mount.setText(_translate("jmtpfs", "Mount"))
        self.Umount.setText(_translate("jmtpfs", "Unmount"))
        self.DevicePath.setText(_translate("jmtpfs", "Mount folder for Android"))
        self.ChoosePathAndroid.setText(_translate("jmtpfs", "..."))
        self.AndroidLabel.setText(_translate("jmtpfs", "Android device"))
        self.ComputerLabel.setText(_translate("jmtpfs", "Computer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jmtpfs = QtWidgets.QWidget()
    ui = Ui_jmtpfs()
    ui.setupUi(jmtpfs)
    jmtpfs.show()
    sys.exit(app.exec_())

