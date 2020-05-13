import os
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Sanitization") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Device:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.Sanitize)
        pybutton.resize(200,32)
        pybutton.move(80, 60)        

    def clickMethod2(self):
        print('Device: ' + self.line.text())
        
    
    def Sanitize(self):
		
		if self.line.text() == 'sda':
		
		   print "Cannot Sanitize SDA as it is the computer's main hard-drive"
		
		   sys.exit()
		
		else:
		
		   wipeCmd = "sudo dd if=/dev/zero of=/dev/%s bs=1M " % (self.line.text())
		     
		   os.system(wipeCmd)
		
		   CmdFormat = "sudo parted /dev/'{0}' --align opt mklabel msdos 0 4G ; sudo mkfs.exfat -n TargetHDD /dev/'{1}' " .format(self.line.text(),  self.line.text())
		
		   os.system(CmdFormat)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
