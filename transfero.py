import sys
from PyQt5.QtWidgets import QMessageBox, QTabWidget
from PyQt5.QtGui import QIcon

class Transfero(QTabWidget):
    def __init__(self, name='Transfero', ax=300, ay=200, aw=1000, ah=500):
        super(Transfero, self).__init__()
        self.setWindowTitle(name)
        self.setGeometry(ax, ay, aw, ah)

        # set icon for window
        self.setWindowIcon(QIcon(':window_icon/WindowIcon/transfero.png'))

    # this method checks whether we unmounted FUSE system or not before actually leaving the program
    def closeEvent(self, e):
        # check if go-mtpfs is mounted, prevent closing window until unmounting system
        go_mtpfs_mounted = self.widget(0).Unmount.isEnabled()
        jmtpfs_mounted = self.widget(1).Unmount.isEnabled()
        mtpfs_mounted = self.widget(2).Unmount.isEnabled()

        if go_mtpfs_mounted:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Warning')
            msg.setText('It seems you haven\'t unmounted one of the systems. Please, unmount system(s) and try again.')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

            e.ignore()

        elif jmtpfs_mounted:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Warning')
            msg.setText('It seems you haven\'t unmounted one of the systems. Please, unmount system(s) and try again.')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

            e.ignore()

        elif mtpfs_mounted:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Warning')
            msg.setText('It seems you haven\'t unmounted one of the systems. Please, unmount system(s) and try again.')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

            e.ignore()

        else:
            # close window
            e.accept()

