from GUI_f import Ui_MainWindow_2
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_Main_2(QMainWindow, Ui_MainWindow_2):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.images = "" #选择图片
        self.save_images = ""
        self.pushButton_1.clicked.connect(self.look)
        self.pushButton_18.clicked.connect(self.savetup)  # 单图片保存
        self.pushButton_1_2.clicked.connect(self.x_s_s)  #

    def look(self):
        pass

    def savetup(self):
        pass
    def x_s_s(self):
       pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Ui_Main_2()
    gui.show()
    sys.exit(app.exec_())





























