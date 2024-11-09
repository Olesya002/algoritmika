'''Функционал приложения'''
# две функции (всплывающее окно победы и проигрыша)
def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Верно!\nВы выиграли Playstation')
    victory_win.exec_()
def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('Нет, Kivy\nВы выиграли ручку')
    victory_win.exec_()



'''Интерфейс приложения'''
# 1 шаг - подгружаем все необходимые классы
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

# 2 шаг - создаем два главных объекта: приложение и окно
app = QApplication([])
window = QWidget()

# 3 шаг - создаем объекты-виджеты 
# (у нас их пять: 4 переключателя и 1 надпись)
label = QLabel('Что из этого НЕ является языком программирования?')
r_1 = QRadioButton('R')
r_2 = QRadioButton('C#')
r_3 = QRadioButton('Pascal')
r_4 = QRadioButton('Kivy')

# 4 шаг - приконнектим функции к кнопкам
r_1.clicked.connect(show_lose)
r_2.clicked.connect(show_lose)
r_3.clicked.connect(show_lose)
r_4.clicked.connect(show_win)

# 5 шаг - создадим линии, на которые поместим все виджеты
line_h_1 = QHBoxLayout()
line_h_2 = QHBoxLayout()
line_h_3 = QHBoxLayout()
line_h_1.addWidget(label, alignment = Qt.AlignCenter)
line_h_2.addWidget(r_1, alignment = Qt.AlignCenter)
line_h_2.addWidget(r_2, alignment = Qt.AlignCenter)
line_h_3.addWidget(r_3, alignment = Qt.AlignCenter)
line_h_3.addWidget(r_4, alignment = Qt.AlignCenter)

layout_main = QVBoxLayout()
layout_main.addLayout(line_h_1)
layout_main.addLayout(line_h_2)
layout_main.addLayout(line_h_3)

# теперь прикрепим линию на окно
window.setLayout(layout_main)

# 6 шаг - две команды для работы приложения
window.show()
app.exec()
