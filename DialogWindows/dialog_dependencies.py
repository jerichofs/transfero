import sys
import os
import subprocess
from GeneratedUI.ui_dependencies import Ui_Depend
from PyQt5.QtWidgets import QDialog

class DialogDependencies(QDialog, Ui_Depend):
    def __init__(self):
        super(DialogDependencies, self).__init__()
        self.setupUi(self)
        # set fixed size of the dialog without resizing
        self.setFixedSize(self.size())
        self.CheckLibraries()

        self.transfero_logs_directory = os.path.dirname('.config/transfero/settings/')
        self.transfero_logs_file_path = self.transfero_logs_directory + '/dialog_state.txt'

        self.check_window.stateChanged.connect(self.CheckBoxStateChanged)
        self.check_libraries.clicked.connect(self.UpdateStateLibraries)

        self.NeverOpenDialog()


    def CheckLibraries(self):
        # check if go is instaled
        command = ['dpkg', '-s', 'golang-go']
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output_process = process.communicate()[0].decode('utf-8')

        output_process = output_process.split('\n')

        if output_process[0] == 'Package: golang-go':
            self.golang_state.setText('Installed')
        else:
            self.golang_state.setText('is not installed')

        # check if mtp-tools is installed
        command = ['dpkg', '-s', 'mtp-tools']
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output_process = process.communicate()[0].decode('utf-8')

        output_process = output_process.split('\n')
        if output_process[0] == 'Package: mtp-tools':
            self.mtp_state.setText('Installed')
        else:
            self.mtp_state.setText('is not installed')


        # check if go-mtpfs is installed
        command = ['dpkg', '-s', 'go-mtpfs']
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output_process = process.communicate()[0].decode('utf-8')

        output_process = output_process.split('\n')
        if output_process[0] == 'Package: go-mtpfs':
            self.go_mtpfs_state.setText('Installed')
        else:
            self.go_mtpfs_state.setText('is not installed')

        # check if jmtpfs is installed
        command = ['dpkg', '-s', 'jmtpfs']
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output_process = process.communicate()[0].decode('utf-8')

        output_process = output_process.split('\n')
        if output_process[0] == 'Package: jmtpfs':
            self.jmtpfs_state.setText('Installed')
        else:
            self.jmtpfs_state.setText('is not installed')

        #check if mtpfs is installed
        command = ['dpkg', '-s', 'mtpfs']
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output_process = process.communicate()[0].decode('utf-8')

        output_process = output_process.split('\n')
        if output_process[0] == 'Package: mtpfs':
            self.mtpfs_state.setText('Installed')
        else:
            self.mtpfs_state.setText('is not installed')

    def UpdateStateLibraries(self):
        self.CheckLibraries()

    def CheckBoxStateChanged(self):
        self.CheckDialogOpen()

    def NeverOpenDialog(self):
        if os.path.isfile(self.transfero_logs_file_path):
            file = open(self.transfero_logs_file_path, 'r')
            string = file.read().replace('\n', '')
            file.close()

            if string == 'False':
                self.exec_()
        else:
            self.CheckDialogOpen()
            self.exec_()

    def CheckDialogOpen(self):
        # if there's not a folder .transfero then create it
        if not os.path.exists(self.transfero_logs_directory):
            os.makedirs(self.transfero_logs_directory)
            #if there's not a file
        if not os.path.isfile(self.transfero_logs_file_path):
            file = open(self.transfero_logs_file_path, 'w+')
            # check if the checkbox's been enabled
            if self.check_window.isChecked():
                file.write('True')
                file.seek(0)
                file.close()
            else:
                file.write('False')
                file.seek(0)
                file.close()
        else:
            # if the file already exists
            file = open(self.transfero_logs_file_path, 'w+')
            # check if the checkbox's been enabled
            if self.check_window.isChecked():
                file.write('True')
                file.seek(0)
                file.close()
            else:
                file.write('False')
                file.seek(0)
                file.close()
