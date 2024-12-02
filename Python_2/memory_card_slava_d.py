
'''Интерфейс приложения'''
# 1 шаг - подгружаем все необходимые классы
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox,QPushButton
from PyQt5.QtCore import Qt

class Question():

    def __init__(self, question, right_answers, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answers = right_answers
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

app  = QApplication([])                                            ''' Это убрать '''

btn = QPushButton('ответить')
question_list = []
question_list.append(Question('какой национальности C.RONALDO', 'германец', 'аргентинец', 'португалец', 'никто из них'))
question_list.append(Question('кто топ 1 мира на мо', 'HYRA', 'VITAL_SHARK', 'CUBE', 'ALEZZ'))
question_list.append(Question('КТО ТОП 1 МИРА В БС', 'PHYZIC', 'CUBE', 'HYRA', 'RZM64'))

def ask(ques, right_answers, wrong_1, wrong_2, wrong_3):                    ''' тут в скобках оставь только q '''
    shuffle(answers)
    answers[0].setText(right_answers)                                       '''  тут в скобках q.right_answers '''
    answers[1].setText(wrong_1)                                             '''  тут в скобках q.wrong1 '''
    answers[2].setText(wrong_2)                                             '''  тут в скобках q.wrong2 '''
    answers[3].setText(wrong_3)                                             '''  тут в скобках q.wrong3 '''

    q.setText(ques)                                                         '''  тут quess.setText(q.question) '''
    q1.setText(right_answers)                                               '''  тут в скобках q.right_answers '''


def show_question():
    QRadioGroupBox.show()
    QRadioGroupBox2.hide()
    btn.setText('ответить')
def show_result():
    QRadioGroupBox.hide()
    QRadioGroupBox2.show()
    btn.setText('следующий вопрос')
def start_test():
    if 'ответить' == btn.text():
        show_result()
    else:
        show_question()

    
app = QApplication([])                           ''' 50-51 перемести наверх, поставь сразу после import-ов '''
main_win = QWidget()

QRadioGroupBox = QGroupBox('Варианты ответов:')
q = QLabel('кто такой подсос')                   ''' тут измени на quess = '''
btn = QPushButton('ответить')
btn.clicked.connect(start_test)


r_1 = QRadioButton('эдгар')
r_2 = QRadioButton('мортис ')
r_3 = QRadioButton('баз с гипером')
r_4 = QRadioButton('шелли с ультой')
l_ans1 = QHBoxLayout()

from random import shuffle

answers = [r_1, r_2, r_3, r_4]


# группа с ответом
QRadioGroupBox2 = QGroupBox('ответы')
q1 = QLabel('правильный ответ')
l_ans4 = QVBoxLayout()
l_ans4.addWidget(q1)
QRadioGroupBox2.setLayout(l_ans4)
QRadioGroupBox2.hide()



l_ans2 = QVBoxLayout()
l_ans3 = QVBoxLayout()

l_ans2.addWidget(r_1)
l_ans2.addWidget(r_2)
l_ans3.addWidget(r_3)
l_ans3.addWidget(r_4)
l_ans1.addLayout(l_ans2)
l_ans1.addLayout(l_ans3)

QRadioGroupBox.setLayout(l_ans1)
V =  QVBoxLayout()
V.addWidget(q)                                  ''' в скобках quess '''
V.addWidget(QRadioGroupBox)
V.addWidget(QRadioGroupBox2)
V.addWidget(btn)
main_win.setLayout(V)

 
ask('кто такой подсос','эдгар', 'мортис','базз с гипером','шелли с ультой')          ''' тут будет ask(Question('кто такой подсос','эдгар', 'мортис','базз с гипером','шелли с ультой')) '''
main_win.show()
app.exec()
