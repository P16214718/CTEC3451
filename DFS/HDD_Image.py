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
        self.setWindowTitle("HDD Imaging") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Device:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)        

    def clickMethod2(self):
        print('Device: ' + self.line.text())
        
    
    def clickMethod(self):
		
		     #Software Writeblocker - make evidence read only
		     myCmdReadOnly = "sudo hdparm -r1 /dev/%s " % (self.line.text())       
		     os.system(myCmdReadOnly)
		     
		     #Change Directory to targetHDD device
		     myCmdDIR = "cd /home/ ; cd /media/user/TargetHDD "
		     os.system(myCmdDIR)
		     
		     #Image evidence to TargetHDD
		     myCmd3 = "sudo dd if=/dev/%s of=/media/user/TargetHDD/img.dd conv=notrunc status=progress " % (self.line.text())
		     
		     os.system(myCmd3)
		     print("HDD imaged to Target HDD directory")
		     
		     #HDD/IMAGE VERIFICATION
		     print ("Verification process will now begin")
		    		    
		     myCmd4 = "sudo sha1sum img.dd >> Hash-Verification.txt & sudo sha1sum /dev/%s >> Hash-Verification.txt " % (self.line.text())
		     
		     os.system(myCmd4)   		
		

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
