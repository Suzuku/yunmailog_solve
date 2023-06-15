# file: quit_button.py
#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

This program creates a quit
button. When we press the button,
the application terminates.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication,QFileDialog,QLineEdit

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        lineText = QLineEdit(self)
        lineText.move(60,100)
        # self.setCentralWidget(self.lineText)
        qbtn = QPushButton('浏览', self)
        qbtn.clicked.connect(self.showDialog)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('浏览文件')
        self.show()

    def print(self):
        print(self)

    def showDialog(self):

        home_dir ='*'
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            self.lineText.setText(fname[0])
            print(fname)

           

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()