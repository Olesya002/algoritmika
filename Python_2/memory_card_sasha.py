


'''Интерфейс приложения'''
# 1 шаг - подгружаем все необходимые классы
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton
from PyQt5.QtCore import Qt
from random import shuffle

# 2 шаг - создаем два главных объекта: приложение и окно
app = QApplication([])
window = QWidget()

#создаем окно в окне и ставим кнопки
g = QGroupBox('Варианты:')
r1 = QRadioButton('1')
r2 = QRadioButton('2')
r3 = QRadioButton('3')
r4 = QRadioButton('4')
answers = [r1, r2, r3, r4]

V = QVBoxLayout()
H1 = QHBoxLayout()
H2 = QHBoxLayout()
H1.addWidget(r1)
H1.addWidget(r2)
H2.addWidget(r3)
H2.addWidget(r4)
V.addLayout(H1)
V.addLayout(H2)
qestion = QLabel('вопрос')
g.setLayout(V)

g2 = QGroupBox('Следующий вопрос')
ans = QLabel('тут будет ответ')
line = QVBoxLayout()
line.addWidget(g2)                                              ''' на линию line закрепляй ans, а не g2 '''
g2.setLayout(line)
V2 = QVBoxLayout()
V2.addWidget(g)
r5 = QPushButton('Ответить')
V2.addWidget(g2)                                                ''' на след. строке добавь g2.hide() '''
V2.addWidget(qestion)
V2.addWidget(r5)
window.setLayout(V2)                                              

def show_test():
    if 'Проверить' == button.text():                               ''' вместо button твой виджет с кнопкой - у тебя это r5 + на твоей кнопке надпись Ответить, тогда и тут напиши 'Ответить' '''
        start_test()
    else:
        shot_iscept()

def shot_iscept():
    g2.hide()
    g.show()
    button.setText('Проверить')                                    ''' вместо button твой виджет с кнопкой - у тебя это r5 + на твоей кнопке надпись Ответить, тогда и тут напиши 'Ответить' '''

def start_test():
    g2.show()
    g.hide()
    button.setText('Следующий тест')                               ''' вместо button твой виджет с кнопкой - у тебя это r5 '''


def ask(qestion, right_answer, wrong1, wrong2, wrong3):            ''' тут в скобках оставь только q - это будет объект класса Question '''
    shuffle(answers)
    answer[0].setText(right_answer)                                ''' теперь в функции ask только один аргумент q, поэтому тут будет: answers[0].setText(q.right_answer) '''
    answer[1].setText(wrong1)                                      ''' изменить 67 - 69 строки по аналогии: answers[1].setText(q.wrong1) '''
    answer[2].setText(wrong2)
    answer[3].setText(wrong3)
    question.setText(question)                                     ''' тут название виджета не совпадает с твоим, у тебя qestion: qestion.setText(q.question) '''
    ans.setText(right_text)                                        ''' а тут в скобках будет q.right_answer '''
                                                                   ''' еще нужен класс Question для вопросов, вставила его ниже, скопируй'''
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
      
# итоговая линия
main_line = QVBoxLayout()                        ''' Нашла у тебя итоговую линию - это V2, поэтому все это можно стереть '''
main_line.addWidget(queston)                                      
main_line.addWidget(g)
main_line.addWidget(g2)
main_line.addbutton()                                             


''' Не забудем приконнектить функцию к кнопке  ''' 
r5.clicked.connect(show_test)

# 3 шаг - создаем объекты-виджеты 
# (у нас их пять: 4 переключателя и 1 надпись)


# 4 шаг - приконнектим функции к кнопками и создем цикл 
# r1.clicked.connect(show_lose)
# r2.clicked.connect(show_lose)
# r3.clicked.connect()
# r4.clicked.connect()

# 5 шаг - создадим линии, на которые поместим все виджеты
# V = QVBoxLayout()
# H1 = QHBoxLayout()
# H2 = QHBoxLayout()

# H1.addWidget(r1, alignment = Qt.AlignCenter)
# H1.addWidget(r2, alignment = Qt.AlignCenter)
# H2.addWidget(r3, alignment = Qt.AlignCenter)
# H2.addWidget(r4, alignment = Qt.AlignCenter)

# layout_main = QVBoxLayout()
# layout_main.addLayout(H1)
# layout_main.addLayout(H2)
# layout_main.addLayout(V)

# # теперь прикрепим линию на окно
# window.setLayout(layout_main)

# 6 шаг - две команды для работы приложения

ask('каков ответ?', '1', '2', '3', '4')          ''' Теперь при вызове функции ask будем в качестве аргумента указывать объект, тогда будет ask(Question('каков ответ?', '1', '2', '3', '4')) '''
window.show()


app.exec()
