'''Функционал приложения'''
# при нажатии на кнопку будет генерироваться случайное имя и текст надписи label_2 изменится на имя победителя
import random
names = ['Святослав', 'Степан', 'Кирилл', 'Вячеслав', 'Никита', 'Владислав', 'Александр']
def show_winner():
    winner = names[random.randint(0, len(names) - 1)]
    label_2.setText(winner)



'''Интерфейс приложения'''
# 1 шаг - подгружаем все необходимые классы:
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

# 2 шаг - создаем два главных объекта: приложение и окно
app = QApplication([])
window = QWidget()

# 3 шаг - создаем объекты-виджеты (у нас их три: две надписи и кнопка)
# вместо '-' при нажатии на кнопку будет появляться результат
label_1 = QLabel('Нажми, чтобы узнать, кто лучший программист')
label_2 = QLabel('-')  
button = QPushButton('Сгенерировать')

# 4 шаг - приконнектим функцию к кнопке
button.clicked.connect(show_winner)

# 5 шаг - создадим линию, на которую поместим все виджеты
line = QVBoxLayout()
line.addWidget(label_1)
line.addWidget(label_2)
line.addWidget(button)
# теперь прикрепим линию на окно
window.setLayout(line)

# 6 шаг - две команды для работы приложения
window.show()
app.exec()
