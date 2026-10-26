from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QLabel, QVBoxLayout, QApplication, QWidget, QGridLayout,
    QStackedLayout, QTabWidget, QInputDialog)
from PyQt5.QtGui import QPalette, QColor, QPixmap

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('прилипала')
        self.resize(800, 800)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.push_btn = QPushButton(self.central_widget)
        self.push_btn.setGeometry(QtCore.QRect(350, 701, 150, 100))
        self.push_btn.setText('заказать пиццу')
        self.push_btn.clicked.connect(self.start_questions)





        #frame -
        self.frame = QtWidgets.QFrame(self.central_widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)  # Устанавливаем стиль фрейма
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)  # Устанавливаем тень фрейма

        #Qlabel -для картинки внутри фрейма

        self.image_label = QLabel(self.frame)
        self.image_label.setGeometry(QtCore.QRect(0, 0, 800, 700))
        self.image_label.setScaledContents(True)

        #загружаем изображение

        pixmap = QPixmap("фон.jpg")
        self.image_label.setPixmap(pixmap)


        self.answers = []
        self.questions = ['какой размер пиццы?','какой у тебя цвет глаз?','красный или чёрный?','что пьёт корова?']


    def start_questions(self):
        n = 1
        for question in self.questions:
            text, ok = QInputDialog.getText(self, f'глупый вопрос {n}', question)
            n+=1
            if not ok:
                return
            self.answers.append(text)
        self.final()

    def final(self):
        self.image_label.deleteLater()
        self.push_btn.deleteLater()
        self.lbl = QLabel(self.frame)
        self.lbl.setGeometry(QtCore.QRect(0, 0, 800, 700))
        self.lbl.setText('\n'.join(self.answers))
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.show()

        self.push_btn2 = QPushButton(self.central_widget)
        self.push_btn2.setGeometry(QtCore.QRect(350, 701, 150, 100))
        self.push_btn2.setText('подтвердить')
        self.push_btn2.clicked.connect(self.close)
        self.push_btn2.show()



    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())