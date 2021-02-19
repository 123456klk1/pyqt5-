# -*- codfrom PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow_2(object):
    """
    该函数用于切片图像查看界面功能的显示
    """
    def setupUi(self, MainWindow):
        self.setObjectName("InterFace_1")
        self.resize(1300, 900)
        #设置整个界面的大小、背景        1100, 680        #背景图
        self.setStyleSheet("#InterFace_1{border-image:url(./image/background.png)}")
        # MainWindow.setObjectName("MainWindow")
        self.setGeometry(300, 10, 900, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QGridLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2.addLayout(self.gridLayout, 3, 1,18, 19)
        self.gridLayout_2.addLayout(self.gridLayout_3, 3, 17, 20, 24)
        self.textEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.gridLayout.addWidget(self.textEdit_1, 1, 2, 12, 11)
        self.textEdit_1.setReadOnly(True)
        self.textEdit_1.setFixedSize(420, 350)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label")
        self.gridLayout.addWidget(self.label_5, 5, 3, 1, 3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("输入图像地址")
        self.gridLayout.addWidget(self.lineEdit, 5, 4, 1, 4)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton_1, 5, 8, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton_18,  9, 3, 1, 2)
        self.pushButton_18.setFixedSize(130, 32)
        self.pushButton_1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1_2.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton_1_2, 7, 3, 1, 2)
        self.pushButton_1_2.setFixedSize(130, 32)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label")
        self.gridLayout.addWidget(self.label_2, 24, 3, 1, 8)
        self.label_2.setFixedSize(10, 10)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label")
        self.gridLayout_3.addWidget(self.label_3, 0, 1, 26, 26)
        self.label_3.setStyleSheet("background-color:rgb(135,206,235)")
        self.label_3.setFixedSize(690, 690)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton_8, 23, 23, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit_10, 23, 24, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton_19, 23, 13, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label")
        self.gridLayout_4.addWidget(self.label_12, 23, 17, 1, 3)
        self.label_12.setFixedSize(130, 32)
        self.line_4 = QtWidgets.QLabel()
        self.line_4.setMinimumSize(QtCore.QSize(0, 20))
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_4.setStyleSheet("#line{border-image:url(./image/h_line.png)}")
        self.line_4.setObjectName("line")
        self.gridLayout_2.addWidget(self.line_4, 0, 0, 1, 43)
        self.line_3 = QtWidgets.QLabel()
        self.line_3.setMinimumSize(QtCore.QSize(20, 0))
        self.line_3.setMaximumSize(QtCore.QSize(20, 16777215))
        self.line_3.setStyleSheet("#line{border-image:url(./image/vertical_line.png)}")
        self.line_3.setObjectName("line")
        self.gridLayout_2.addWidget(self.line_3, 0, 0, 33, 1)
        self.pushButton_1.setFixedSize(80, 32)
        self.lineEdit_10.setFixedSize(50, 32)
        self.lineEdit.setFixedSize(180, 32)
        self.label_4.setFixedSize(130, 32)
        self.label_5.setFixedSize(80, 32)
        self.lineEdit.setPlaceholderText("输入图像地址")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 23, 1, 10, 1)


        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setObjectName("label_d")
        self.gridLayout_2.addWidget(self.label_25, 0, 0, 1, 5)
        self.label_25.setFixedSize(90, 32)
        self.pushButton_18.setStyleSheet(''' 
                                QPushButton{background:rgb(135,206,235);}
                            ''')
        self.label_4.setObjectName("label1")
        self.label_25.setObjectName("label1")
        self.label_5.setObjectName("label")
        self.label_3.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font1 = QtGui.QFont()
        font1.setFamily("微软雅黑")
        font1.setPointSize(12)
        self.label_4.setFont(font1)
        self.label_25.setFont(font1)
        self.label_5.setFont(font)
        self.label_3.setFont(font)
        self.centralwidget.setStyleSheet('''      
        #lineEdit{color:rgb(255, 255, 255);}
        #comboBox{color:rgb(255, 255, 255);}
        #label{color:rgb(0, 255, 255);}
        #label1{color:rgb(0, 255, 255);}
        QPushButton#pushButton{
        font-family:KaiTi; 
        font-size:17px;
        font-weight:200;
        background:rgb(135,206,235);border:2px groove gray;border-radius:10px;padding:2px 4px
        }
        QPushButton#pushButton_2{
        font-family:KaiTi; 
        font-size:17px;
        font-weight:200;
        }
        QLabel#label{font-family:KaiTi; 
        font-size:17px;
        font-weight:200;}
        QLabel#label_d{font-family:KaiTi; 
        font-size:19px;
        font-weight:200;}
            QLabel#label_1{font-family:_GB2312	FangSong_GB2312; 
        font-size:19px;
        font-weight:200;}
         QLabel#label_1{font-family:_GB2312	FangSong_GB2312; 
        font-size:19px;
        font-weight:200;}
          QLabel#label_9{font-family:KaiTi; 
        font-size:17px;
        font-weight:200;}
         QLabel#label_10{font-family:KaiTi; 
        font-size:17px;
        font-weight:200;}
        QLabel#label_d{ font-family:Microsoft YaHei; 
                      font-size:19px;
                      font-weight:300;}
        QFrame#line{
        width:30px;
       border:3px solid gray;
        border-radius:10px;
        } 
                ''')

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", ""))
        self.label_12.setText(_translate("MainWindow", ""))

        self.label_25.setText(_translate("MainWindow", "图片预测"))
        self.label_4.setText(_translate("MainWindow", "选择图片"))
        self.label_5.setText(_translate("MainWindow", "输入地址"))
        self.pushButton_1.setText(_translate("MainWindow", "浏览"))  # 选择病人的图片
        self.pushButton_1_2.setText(_translate("MainWindow", "预测图片"))  # 选择病人的图片
        self.pushButton_18.setText(_translate("MainWindow", "图像另存为"))





