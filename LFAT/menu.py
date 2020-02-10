# https://pythonprogramminglanguage.com/pyqt-menu/
import sys, os
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction
from PyQt5.QtCore import QSize    
from PyQt5.QtGui import QIcon
import webbrowser



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.setWindowIcon( QtGui.QIcon("icon.png") )
        self.setWindowIcon(QtGui.QIcon("/icon.png"))
        self.setMinimumSize(QSize(500, 500))    
        self.setWindowTitle("Linux Forensics Automator - Main Menu") 

        # Add button widget
        #pybutton = QPushButton('Pyqt', self)
        #pybutton.clicked.connect(self.clickMethod)
        #pybutton.resize(100,32)
        #pybutton.move(130, 30)        
        #pybutton.setToolTip('This is a tooltip message.')  

        # Create List Devices action
        LDAction = QAction(QIcon('listdevices.png'), '&List Devices', self)        
       #newAction.setShortcut('Ctrl+N')
        LDAction.setStatusTip('List all system Devices')
        LDAction.triggered.connect(self.listdev)

        # Create Sanitize action
        sanAction = QAction(QIcon('sanitize.png'), '&Sanitization', self)        
       # openAction.setShortcut('Ctrl+O')
        sanAction.setStatusTip('Wipe a device')
        sanAction.triggered.connect(self.sanitize)
        
                
        # Create HDD Imaging action
        hddAction = QAction(QIcon('hdd.png'), '&HDD Imaging', self)        
        #exitAction.setShortcut('Ctrl+Q')
        hddAction.setStatusTip('Create a forensic image of an HDD')
        hddAction.triggered.connect(self.hddimage)
        
        # Create DFR action
        dfrAction = QAction(QIcon('dfr.png'), '&Deleted File Recovery', self)        
        #exitAction.setShortcut('Ctrl+Q')
        dfrAction.setStatusTip('Recover deleted files')
        dfrAction.triggered.connect(self.dfr)

        
        # Create Help action
        HelpAction = QAction(QIcon('help.png'), '&Docs', self)        
      # exitAction.setShortcut('Ctrl+Q')
        HelpAction.setStatusTip('Help')
        HelpAction.triggered.connect(self.help)
        
        # Create exit action
        exitAction = QAction(QIcon('exit.png'), '&Quit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&Functions')
        fileMenu.addAction(LDAction)
        fileMenu.addAction(sanAction)
        fileMenu.addAction(hddAction)
        fileMenu.addAction(dfrAction)
        
        fileMenu = menuBar.addMenu('&Help')
        fileMenu.addAction(HelpAction)
        
        fileMenu = menuBar.addMenu('&Exit')
        fileMenu.addAction(exitAction)
        
     #   fileMenu.addAction(newAction)
    #    fileMenu.addAction(openAction)
        
        

    def listdev(self):
        os.system('python CLI.py')

    def sanitize(self):
        os.system('python Sanitize.py')

    def hddimage(self):
        os.system('python HDD_Image.py')
    
    def dfr(self):
        os.system('python DFR.py')
    
    def exitCall(self):
        sys.exit()
        
    def help(self):
        
        webbrowser.open('http://www.google.com')
        #webbrowser.open('http://www.google.com')

        #btn.clicked.connect(open_webbrowser)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
