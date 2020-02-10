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
        self.setWindowTitle("Deleted File Recovery") 

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
        print('Image name: ' + self.line.text())
        
    
    def clickMethod(self):
		   		
		     #FUNCTION 4.2 Recovery of deleted files
		     
		   
		     myCmdRecover = "sudo cd /home/ ; cd user ; cd Desktop ; tsk_recover -i raw -e %s Recovered-Files/ " % (self.line.text())
		     
		     os.system(myCmdRecover)
		     
		      
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
