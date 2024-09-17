import sys
from PyQt6.QtWidgets import*
import pic
from PyQt6.QtGui import*
from PyQt6.QtCore import*
from PyQt6 import QtCore

Windows_Icon = "C:\\Users\\whw\\Desktop\\扫雷\\pic\\Window_Icon.png"
_COVER_ = "C:\\Users\\whw\\Desktop\\扫雷\\pic\\cover.png"
_Mine_ = "C:\\Users\\whw\\Desktop\\扫雷\\pic\\Boom.png"
_EASY_ROW = 10
_EASY_COL = 10
_EASY_NUM = 10
_NORMAL_ROW = 15
_NORMAL_COL = 15
_NORMAL_NUM = 35
_HARD_ROW = 20
_HARD_COL = 20
_HARD_NUM = 75
class Main_Window(QWidget):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.resize(400, 400)
        self.setWindowTitle("Mine_Sweeper")
        self.setWindowIcon(QIcon(Windows_Icon))

        self.image = QPixmap("C:\\Users\\whw\\Desktop\\扫雷\\pic\\Banner.png")
        self.Banner = QLabel(self)
        self.Banner.setPixmap(self.image)

        self.Menu = QLabel(self.Banner)
        self.Menu.resize(400, 200)
        self.Menu.move(0,200)

        self.Easy_Button = QPushButton(self.Menu)
        self.Easy_Button.setFixedSize(100,40)
        self.Easy_Button.setText("Easy")
        self.Easy_Button.clicked.connect(lambda : self.StartGame(_EASY_ROW, _EASY_COL, _EASY_NUM))

        self.Normal_Button = QPushButton(self.Menu)
        self.Normal_Button.setFixedSize(100,40)
        self.Normal_Button.setText("Normal")
        self.Normal_Button.clicked.connect(lambda : self.StartGame(_NORMAL_ROW, _NORMAL_COL, _NORMAL_NUM))

        self.Hard_Button = QPushButton(self.Menu)
        self.Hard_Button.setFixedSize(100,40)
        self.Hard_Button.setText("Hard")
        self.Hard_Button.clicked.connect(lambda : self.StartGame(_HARD_ROW, _HARD_COL, _HARD_NUM))

        self.grid_menu = QGridLayout(self.Menu)
        self.grid_menu.addWidget(self.Easy_Button, 0, 1)
        self.grid_menu.addWidget(self.Normal_Button, 1, 1)
        self.grid_menu.addWidget(self.Hard_Button, 2, 1)

        def StartGame(self,row, col, num):
            self.Showboard(row, col)

        def Showboard(self, row, col):
            self.Banner.close
            for i in range(row):
                for j in range(col):
                    self.button = QPushButton(self)
def main():
    app = QApplication(sys.argv)
    Window = Main_Window()
    Window.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
