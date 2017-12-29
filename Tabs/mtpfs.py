import sys, os
import re
import subprocess
from Resources import resources
from GeneratedUI.ui_mtpfs import Ui_mtpfs
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QCheckBox, QFileDialog, QTreeView, QFileSystemModel, QMessageBox, QShortcut
from PyQt5.QtGui import QIcon, QKeySequence

class Mtpfs(QWidget, Ui_mtpfs):
    def __init__(self):
        super(Mtpfs, self).__init__()
        self.setupUi(self)

        # connect arrow icons for buttons from resources.py
        self.MoveFileBackward.setIcon(QIcon(':button_arrows/ButtonIcons/left-arrow.png'))
        self.MoveFileForward.setIcon(QIcon(':button_arrows/ButtonIcons/right-arrow.png'))

        self.Unmount.setEnabled(False)
        self.MoveFileForward.setEnabled(False)
        self.MoveFileBackward.setEnabled(False)

        self.MoveFileForward.setDown(True)
        self.MoveFileBackward.setDown(True)
        self.Unmount.setDown(True)

        self.ComputerTreeModel = QFileSystemModel()

        path = self.ComputerTreeModel.setRootPath(os.path.expanduser('~'))

        self.ComputerTree.setModel(self.ComputerTreeModel)
        self.ComputerTree.expand(path)
        self.ComputerTree.scrollTo(path)

        self.ComputerTree.setColumnWidth(0, 350)
        self.ComputerTree.setColumnWidth(1, 50)
        self.ComputerTree.setColumnWidth(2, 50)
        self.ComputerTree.setColumnWidth(3, 50)

        self.ComputerTree.setCurrentIndex(path)


        self.AndroidPath.setText(os.path.expanduser('~'))

        # setting up shortcuts for copying files
        self.copy_android_computer = QShortcut(QKeySequence('Right'), self, self.CopyShortcutAndroidComputer)
        self.copy_computer_android = QShortcut(QKeySequence('Left'), self, self.CopyShortcutComputerAndroid)

        self.Mount.clicked.connect(self.MountFileSystem)
        self.Unmount.clicked.connect(self.UnmountFileSystem)
        self.ChoosePathAndroid.clicked.connect(self.GetDeviceDirectory)
        self.MoveFileForward.clicked.connect(self.CopyFileFromAndroidToComputer)
        self.MoveFileBackward.clicked.connect(self.CopyFileFromComputerToAndroid)


    def CopyFileFromAndroidToComputer(self):

        index_android = self.AndroidTree.currentIndex()
        file_path_android = self.AndroidTreeModel.filePath(index_android)
        file_name_android = self.AndroidTreeModel.fileName(index_android)

        index_computer = self.ComputerTree.currentIndex()
        file_path_computer = self.ComputerTreeModel.filePath(index_computer)
        file_name_computer = self.ComputerTreeModel.fileName(index_computer)
        file_type_computer = self.ComputerTreeModel.type(index_computer)
        file_name_computer_length = len(file_name_computer)

        if file_type_computer == 'Folder':
            self.Output.append('<html><b>Please wait while copying...</b</html>')
            # the next command allows to show Output while a file is copying, it's useful when files are large and thus we notify a user to wait
            QApplication.processEvents()
            command_copy = ['cp', '-R', file_path_android, file_path_computer]
            cp = subprocess.Popen(command_copy, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output_cp = cp.communicate()

            self.Output.append('<html><b>' + file_name_android + '</b</html>' + ' has been successfully copied to ' + '<html><b>' + file_path_computer + '</b</html>')
        else:

            self.Output.append('<html><b>Please wait while copying...</b</html>')
            QApplication.processEvents()
            # "in file_path_computer" we delete the name of the file at the end of the path
            command_copy = ['cp', '-R', file_path_android, file_path_computer[:-file_name_computer_length]]
            cp = subprocess.Popen(command_copy, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output_cp = cp.communicate()

            self.Output.append('<html><b>' + file_name_android + '</b</html>' + ' has been successfully copied to ' + '<html><b>' + file_path_computer[:-file_name_computer_length] + '</b</html>')


    def CopyFileFromComputerToAndroid(self):

        index_computer = self.ComputerTree.currentIndex()
        file_path_computer = self.ComputerTreeModel.filePath(index_computer)
        file_name_computer = self.ComputerTreeModel.fileName(index_computer)

        index_android = self.AndroidTree.currentIndex()
        file_path_android = self.AndroidTreeModel.filePath(index_android)
        file_name_android = self.AndroidTreeModel.fileName(index_android)
        file_type_android = self.AndroidTreeModel.type(index_android)
        file_name_android_length = len(file_name_android)

        if file_type_android == 'Folder':
            self.Output.append('<html><b>Please wait while copying...</b</html>')

            QApplication.processEvents()
            command_copy = ['cp', '-R', file_path_computer, file_path_android]
            cp = subprocess.Popen(command_copy, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output_cp = cp.communicate()

            self.Output.append('<html><b>' + file_name_computer + '</b</html>' + ' has been successfully copied to ' + '<html><b>' + file_path_android + '</b</html>')
        else:
            self.Output.append('<html><b>Please wait while copying...</b</html>')
            QApplication.processEvents()
            command_copy = ['cp', '-R', file_path_computer, file_path_android[:-file_name_android_length]]
            cp = subprocess.Popen(command_copy, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output_cp = cp.communicate()

            self.Output.append('<html><b>' + file_name_computer + '</b</html>' + ' has been successfully copied to ' + '<html><b>' + file_path_android[:-file_name_android_length] + '</b</html>')


    def GetDeviceDirectory(self):
        path_dialog = QFileDialog()
        path_dialog.setFileMode(QFileDialog.DirectoryOnly)
        self.AndroidPath.setText(path_dialog.getExistingDirectory(self, 'Open Folder'))
        if not len(self.AndroidPath.text()):
            self.AndroidPath.setText(os.path.expanduser('~'))


    def MountFileSystem(self):
        # Check if a device connected via USB to the computer
        if self.isDeviceMounted():
            # set the name of the connected device
            self.AndroidLabel.setText(self.androidDeviceName)
            #Check if a folder is empty
            if len(os.listdir(self.AndroidPath.text())) != 0:

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Warning')
                msg.setText('The folder doesn\'t have to contain any files in order to mount the device')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            else:
                self.Mount.setEnabled(False)
                self.Unmount.setEnabled(True)
                self.AndroidPath.setDisabled(True)
                self.ChoosePathAndroid.setEnabled(False)
                self.MoveFileForward.setEnabled(True)
                self.MoveFileBackward.setEnabled(True)
                self.Mount.setText('Mounted')

                self.Mount.setDown(True)
                self.Unmount.setDown(False)
                self.ChoosePathAndroid.setDown(True)
                self.MoveFileForward.setDown(False)
                self.MoveFileBackward.setDown(False)

                #create a folder for Android
                self.aditionalAndroidPath = self.AndroidPath.text() + '/Android'
                command_mkdir = ['mkdir', self.aditionalAndroidPath]
                mkdir = subprocess.Popen(command_mkdir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                command_go_mtpfs = ['mtpfs', self.aditionalAndroidPath]
                mount_go_mtpfs = subprocess.Popen(command_go_mtpfs, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                self.AndroidTreeModel = QFileSystemModel()

                path = self.AndroidTreeModel.setRootPath(self.AndroidPath.text())

                self.AndroidTree.setModel(self.AndroidTreeModel)
                self.AndroidTree.expand(path)
                self.AndroidTree.scrollTo(path)

                self.AndroidTree.setColumnWidth(0, 350)
                self.AndroidTree.setColumnWidth(1, 60)
                self.AndroidTree.setColumnWidth(2, 50)
                self.AndroidTree.setColumnWidth(3, 50)

                self.AndroidTree.setCurrentIndex(path)


                self.Output.append('You\'re using the <html><b>[mtpfs]</b</html> library')

                self.Output.append('Your Android Device mounted at ' + '<html><b>' + self.aditionalAndroidPath + '</b</html>')
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Warning')
            msg.setText('It seems the Device hasn\'t mounted yet. Please, connect your Android Device to the computer')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()


    def isDeviceMounted(self):
        command_usb_devices = ['usb-devices']
        usb_devices = subprocess.Popen(command_usb_devices, stdout=subprocess.PIPE)

        command_grep = ['grep', '-E', 'Manufacturer|Product']
        grep = subprocess.Popen(command_grep, stdin=usb_devices.stdout, stdout=subprocess.PIPE)

        output_grep = grep.communicate()[0].decode('utf-8')
        pattern = re.compile('Manufacturer=Android')
        listDevices = output_grep.split('\n')
        self.androidDeviceName = ''

        for index, line in enumerate(listDevices):
            matchedline = pattern.search(line)
            if matchedline is not None:
                #parsing the name of the device from the line
                self.androidDeviceName = listDevices[index + 1]
                self.androidDeviceName = self.androidDeviceName.split()
                self.androidDeviceName = self.androidDeviceName[1].replace('Product=', '')
                return True

        return False


    def UnmountFileSystem(self):
        self.AndroidTree.setModel(None)
        #get back the android label
        self.AndroidLabel.setText('Android Device')

        command_unmount = ['fusermount', '-uz', self.aditionalAndroidPath]
        fusermount = subprocess.Popen(command_unmount, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        command_rm_folder = ['rm', '-rf', self.aditionalAndroidPath]
        remove_folder = subprocess.Popen(command_rm_folder, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        self.Unmount.setEnabled(False)
        self.Mount.setEnabled(True)
        self.AndroidPath.setDisabled(False)
        self.ChoosePathAndroid.setEnabled(True)
        self.MoveFileForward.setEnabled(False)
        self.MoveFileBackward.setEnabled(False)
        self.Mount.setText('Mount')

        self.Unmount.setDown(True)
        self.Mount.setDown(False)
        self.ChoosePathAndroid.setDown(False)
        self.MoveFileForward.setDown(True)
        self.MoveFileBackward.setDown(True)

        self.Output.append('The Android Device successfully unmounted!')
        self.Output.clear()


    def CopyShortcutAndroidComputer(self):
        # if system is mounted we can use shortcuts
        if self.Unmount.isEnabled():
            index_android = self.AndroidTree.currentIndex()
            file_path_android = self.AndroidTreeModel.filePath(index_android)
            file_name_android = self.AndroidTreeModel.fileName(index_android)

            index_computer = self.ComputerTree.currentIndex()
            file_path_computer = self.ComputerTreeModel.filePath(index_computer)
            file_name_computer = self.ComputerTreeModel.fileName(index_computer)
            file_type_computer = self.ComputerTreeModel.type(index_computer)
            file_name_computer_length = len(file_name_computer)

            if file_type_computer == 'Folder':
                self.Output.append('<html><b>Please wait while copying...</b</html>')
                # the next command allows to show Output while a file is copying, it's useful when files are large and thus we notify a user to wait
                QApplication.processEvents()
                command_copy = ['cp', '-R', file_path_android, file_path_computer]
                cp = subprocess.Popen(command_copy, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                output_cp = cp.communicate()

                self.Output.append('<html><b>' + file_name_android + '</b</html>' + ' has been successfully copied to ' + '<html><b>' + file_path_computer + '</b</html>')
            else:

                self.Output.append('<html><b>Please wait while copying...</b</html>')
                QApplication.processEvents()
                # "in file_path_computer" we delete the name of the file at the end of the path
                command_copy = ['cp', '-R', file_path_android, file_path_computer[:-file_name_computer_length]]
                cp = subprocess.Popen(command_copy, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                output_cp = cp.communicate()

                self.Output.append('<html><b>' + file_name_android + '</b</html>' + ' has been successfully copied to ' + '<html><b>' + file_path_computer[:-file_name_computer_length] + '</b</html>')


    def CopyShortcutComputerAndroid(self):
        if self.Unmount.isEnabled():
            # if system is mounted we can use shortcuts
            index_computer = self.ComputerTree.currentIndex()
            file_path_computer = self.ComputerTreeModel.filePath(index_computer)
            file_name_computer = self.ComputerTreeModel.fileName(index_computer)

            index_android = self.AndroidTree.currentIndex()
            file_path_android = self.AndroidTreeModel.filePath(index_android)
            file_name_android = self.AndroidTreeModel.fileName(index_android)
            file_type_android = self.AndroidTreeModel.type(index_android)
            file_name_android_length = len(file_name_android)

            if file_type_android == 'Folder':
                self.Output.append('<html><b>Please wait while copying...</b</html>')

                QApplication.processEvents()
                command_copy = ['cp', '-R', file_path_computer, file_path_android]
                cp = subprocess.Popen(command_copy, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                output_cp = cp.communicate()

                self.Output.append('<html><b>' + file_name_computer + '</b</html>' + ' has been successfully copied to ' + '<html><b>' + file_path_android  + '</b</html>')
            else:
                self.Output.append('<html><b>Please wait while copying...</b</html>')
                QApplication.processEvents()
                command_copy = ['cp', '-R', file_path_computer, file_path_android[:-file_name_android_length]]
                cp = subprocess.Popen(command_copy, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                output_cp = cp.communicate()

                self.Output.append('<html><b>' + file_name_computer + '</b</html>' + ' has been successfully copied to ' + '<html><b>' + file_path_android[:-file_name_android_length] + '</b</html>')


