from GUI_f_1 import Ui_Main_2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import *
import sys
class MainUi(Ui_Main_2):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setObjectName("InterFace_1")
        self.resize(1300, 900)
        #设置整个界面的大小、背景        1100, 680        #背景图
        self.setStyleSheet("#InterFace_1{border-image:url(./image/background.png)}")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel()
        self.label.setMinimumSize(QtCore.QSize(0, 70))
        self.label.setMaximumSize(QtCore.QSize(85, 70))
        self.label = QtWidgets.QLabel("晨曦识别")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{border-image:url(./image/total_title.png);color:rgb(0, 255, 255)}")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        #上方标题    ：居中，字体类型、大小
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.up_widget = QtWidgets.QWidget()  # 创建上侧部件
        self.up_widget.setObjectName('up_widget')
        self.up_layout = QtWidgets.QGridLayout()
        self.up_widget.setLayout(self.up_layout)  # 设置上侧部件布局为网格
        self.up_layout.addWidget(self.label, 0, 0, 3, 13)

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格
        self.right_widget_2 = QtWidgets.QWidget()  # 创建部件
        self.right_widget_2.setObjectName('right_widget_2')
        self.right_layout_2 = QtWidgets.QGridLayout()
        self.right_widget_3 = QtWidgets.QWidget()  # 创建部件
        self.right_widget_3.setObjectName('right_widget_3')
        self.right_layout_3 = QtWidgets.QGridLayout()

        self.main_layout.addWidget(self.up_widget, 0, 0, 3, 13)
        self.main_layout.addWidget(self.right_widget, 4, 0, 2, 13)  # (0,0,12,2)左侧部件在第0行第0列，占14行2列  总共12列，

        self.setCentralWidget(self.main_widget)  # 设置窗口主部件


        self.up_widget1 = QWebEngineView()  # 创建上侧部件
        self.up_widget1.setObjectName('up_widget1')
        self.up_widget1.setMinimumSize(QtCore.QSize(20, 0))
        self.up_widget1.setMaximumSize(QtCore.QSize(70, 40))
        self.up_widget1.page().setBackgroundColor(QColor('transparent'))
        self.main_layout.addWidget(self.up_widget1,0, 12, 3, 1)
        self.up_button_1 = QtWidgets.QPushButton("")
        self.up_button_1.setObjectName('up')
        self.up_button_3 = QtWidgets.QPushButton("")
        self.up_button_3.setObjectName('up')
        self.up_button_1.setIcon(QIcon(QPixmap('xiaobiao/minus5.png')))
        self.up_button_3.setIcon(QIcon(QPixmap('xiaobiao/times5.png')))
        self.g = 0   #全屏  正常  记录
        self.h = 0   #收    正常  记录
        self.up_button_3.clicked.connect(self.close)  #关闭窗口
        self.up_button_1.clicked.connect(self.show_2)
        self.up_button_1.setFixedSize(70, 40)
        self.up_button_3.setFixedSize(50, 40)
        self.main_layout.addWidget(self.up_button_1, 0, 11, 3, 1)
        self.main_layout.addWidget(self.up_button_3, 0, 12, 3, 1)
        self.main_widget.setStyleSheet('''
        #up {   
              font-family:KaiTi;
              font-size:17px;
              font-weight:200;
             border:none;}
                ''')

        # 然后再以电子病历确定开始功能
        self.x_1 = Ui_Main_2()
        self.right_widget_2.setStyleSheet('''
        background:#082E54;
           ''')
        self.right_layout_2.addWidget(self.x_1, 5, 0, 27, 13)
        self.right_widget_2.setLayout(self.right_layout_2)  # 设置右侧部件布局为网格
        self.main_layout.addWidget(self.right_widget_2, 5, 0, 27, 13)
        self.right_widget_2.show()
        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(0)
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def show_1(self):
        self.g +=1
        x = self.g%2
        if (x== 1):
            self.showNormal()
        else:
            self.showMaximized()
    def show_2(self):
        self.h +=1
        h = self.h%2
        if (h == 1):
            self.showMinimized()
        else:
            self.showMinimized()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())





