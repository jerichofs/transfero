import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox, QPushButton, QDialog, QMessageBox, QLineEdit, QLabel, QTabWidget
from Tabs.go_mtpfs import Go_mtpfs
from PyQt5.QtGui import QIcon

class Transfero(QTabWidget):
    def __init__(self, name='Transfero', ax=300, ay=200, aw=1000, ah=500):
        super(Transfero, self).__init__()
        self.setWindowTitle(name)
        self.setGeometry(ax, ay, aw, ah)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Transfero()
    # set icon for window
    window.setWindowIcon(QIcon(':window_icon/WindowIcon/transfero.png'))

    go_mtpfs_tab = Go_mtpfs()

    window.addTab(go_mtpfs_tab, 'Go-mtpfs')

    window.show()

    sys.exit(app.exec_())
