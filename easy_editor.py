from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QListWidget, QFileDialog
import os
from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

app = QApplication([])
win = QWidget()
win.resize(700, 400)
win.setWindowTitle('Easy Editor')
btn_dir = QPushButton("Папка")
pic = QLabel('Картинка')

btn1 = QPushButton("Лево")
btn2 = QPushButton("Право")
btn3 = QPushButton("Зеркало")
btn4 = QPushButton("Резкость")
btn5 = QPushButton("Ч/Б")

list_pic = QListWidget()

v_label1 = QVBoxLayout()
v_label1.addWidget(btn_dir)
v_label1.addWidget(list_pic)

v_label2 = QVBoxLayout()
v_label2.addWidget(pic)

h_label1 = QHBoxLayout()
h_label1.addWidget(btn1)
h_label1.addWidget(btn2)
h_label1.addWidget(btn3)
h_label1.addWidget(btn4)
h_label1.addWidget(btn5)

v_label2.addLayout(h_label1)

h_label2 = QHBoxLayout()
h_label2.addLayout(v_label1)
h_label2.addLayout(v_label2)
win.setLayout(h_label2)

win.show()
app.exec()
