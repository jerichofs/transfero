import sys, os
import re
import subprocess
from Resources import resources
from GeneratedUI.ui_jmtpfs import Ui_jmtpfs
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QCheckBox, QFileDialog, QTreeView, QFileSystemModel, QMessageBox, QShortcut
from PyQt5.QtGui import QIcon

class Jmtpfs(QWidget, Ui_jmtpfs):
    def __init__(self):
        super(Jmtpfs, self).__init__()
        self.setupUi(self)
        
        # connect arrow icons for buttons from resources.py
        self.MoveFileBackward.setIcon(QIcon(':button_arrows/ButtonIcons/left-arrow.png'))
        self.MoveFileForward.setIcon(QIcon(':button_arrows/ButtonIcons/right-arrow.png'))