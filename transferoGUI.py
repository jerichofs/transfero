#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox, QPushButton, QDialog, QMessageBox, QLineEdit, QLabel, QTabWidget
from Tabs.go_mtpfs import Go_mtpfs
from Tabs.jmtpfs import Jmtpfs
from Tabs.mtpfs import Mtpfs
from PyQt5.QtGui import QIcon
from DialogWindows.dialog_dependencies import DialogDependencies
from transfero import Transfero

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Transfero()

    go_mtpfs_tab = Go_mtpfs()
    jmtpfs_tab = Jmtpfs()
    mtpfs_tab = Mtpfs()

    window.addTab(go_mtpfs_tab, 'Go-mtpfs')
    window.addTab(jmtpfs_tab, 'Jmtpfs')
    window.addTab(mtpfs_tab, 'Mtpfs')

    window.show()

    dialog_dependencies = DialogDependencies()

    sys.exit(app.exec_())