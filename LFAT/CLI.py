import os
import sys 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 
 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 
 
        # create objects
        self.pb = QPushButton(self.tr("List Devices"))
        self.te = QTextEdit()
        self.setWindowTitle("List Devices") 
        self.setStyleSheet("background-color: dark-grey;")
        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.pb)
        layout.addWidget(self.te)
        self.setLayout(layout) 

        # create connection
        self.connect(self.pb, SIGNAL("clicked(bool)"),
                     self.run_command)

    def run_command(self):
        
        stdouterr = os.popen4("lsblk -e 7,11")[1].read()
        #stdouterr = os.popen4("lsblk -e 7,8,11")[1].read()
        self.te.setText(stdouterr)
  
if __name__ == "__main__": 
    main()

