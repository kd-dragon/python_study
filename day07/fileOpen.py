import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFileDialog, QLabel
from os.path import basename, join, isfile, isdir
from os import makedirs

class QtGUI(QWidget):
    #복사할 파일 이름
    copyFileName = ""

    def __init__(self):
        super().__init__()

        self.num = 0

        self.setWindowTitle("Appia Qt GUI")

        self.resize(500, 50)

        self.qclist = []

        self.position = 0

        self.Lgrid = QGridLayout()

        self.setLayout(self.Lgrid)

        self.label1 = QLabel('', self)

        self.label2 = QLabel('', self)

        addbutton1 = QPushButton('Open File', self)

        self.Lgrid.addWidget(self.label1, 1, 1)

        self.Lgrid.addWidget(addbutton1, 2, 1)

        addbutton1.clicked.connect(self.add_open)

        addbutton2 = QPushButton('Copy File', self)

        self.Lgrid.addWidget(self.label2, 3, 1)

        self.Lgrid.addWidget(addbutton2, 4, 1)

        addbutton2.clicked.connect(self.add_copy)

        self.show()

    def add_open(self):
        #파일 찾기 창을 열기
        FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './')

        #파일 찾기 창에서 선택한 파일의 경로와 이름을 라벨에 설정
        self.label1.setText(FileOpen[0])

        #파일 이름만 저장해놓자.
        self.copyFileName = basename(FileOpen[0])

    def add_copy(self):
        #여기 파일 복사 기능 코딩
        file1 = open(self.label1.text(), 'rb')
        data = file1.read()
        print(type(data))
        file1.close()


        if not (isdir('D:/iam/virus/')):
            makedirs(join('D:/iam/virus/'))

        file2 = open('D:/iam/virus/'+self.copyFileName, 'wb')
        file2.write(data)
        file2.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = QtGUI()

    app.exec_()