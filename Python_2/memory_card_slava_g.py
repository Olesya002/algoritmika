#создай приложение для запоминания информации
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QMessageBox, QPushButton, QButtonGroup
from PyQt5.QtCore import Qt
from random import shuffle
app = QApplication([])
window = QWidget()
window.resize(1600, 800)


class Question():                                             ''' потерял def __init__(self, question, right_answer, wrong1, wrong2, wrong3): '''
    self.question = question
    self.right_answer = right_answer
    self.wrong1 = wrong1
    self.wrong2 = wrong2
    self.wrong3 = wrong3


question_list = []
question_list.append(Question('Сколько будет 25 * 25?', '685', '645', '625', '665'))


def ask(question, right_answer, wrong1, wrong2, wrong3):     ''' в скобках будет только q '''
    shuffle(list_Widget)
    list_Widget[0].setText(right_answer)                     ''' тут в скобках будет q.right_answer '''
    answer[1].setText(wrong1)                                ''' измени 25-27 как в предыдущей строчке (тут будет list_Widget[1].setText(q.wrong1)) '''
    answer[2].setText(wrong2)
    answer[3].setText(wrong3)
    label_1.setText(question)                                ''' q.question '''
    label_1_Corect.setText(right_answer)                     ''' q.right_answer '''


def action():
    if btn_OK.text() == 'Ответить':
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('продолжить')
    else:
        RadioGroup.setExclusive(False)
        r_1.setChecked(False)
        r_2.setChecked(False)
        r_3.setChecked(False)
        r_4.setChecked(False)
        RadioGroup.setExclusive(True)
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Ответить')


label_1 = QLabel('Конкурс от Crazy People')
btn_OK = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианы ответов')


r_1_1 = '2005'
r_1_2 = '1996'
r_1_3 = '1990'
r_1_4 = '2010'

r_1 = QRadioButton('2005')
r_2 = QRadioButton('1996')
r_3 = QRadioButton('1990')
r_4 = QRadioButton('2010')

list_Widget = [r_1, r_2, r_3, r_4]
shuffle(list_Widget)

r_1.setText(r_1_1)
r_2.setText(r_1_2)
r_3.setText(r_1_3)
r_4.setText(r_1_4)


RadioGroup = QButtonGroup()
RadioGroup.addButton(r_1)
RadioGroup.addButton(r_2)
RadioGroup.addButton(r_3)
RadioGroup.addButton(r_4)

line_h_1 = QHBoxLayout()

line_h_2 = QHBoxLayout()
line_h_3 = QHBoxLayout()

line_h_1.addWidget(label_1, alignment = Qt.AlignCenter)

line_h_2.addWidget(r_1, alignment = Qt.AlignCenter)
line_h_2.addWidget(r_2, alignment = Qt.AlignCenter)
line_h_3.addWidget(r_3, alignment = Qt.AlignCenter)
line_h_3.addWidget(r_4, alignment = Qt.AlignCenter)

layout_main_radio = QVBoxLayout()
layout_main_radio.addLayout(line_h_2)
layout_main_radio.addLayout(line_h_3)

RadioGroupBox.setLayout(layout_main_radio)

AnsGroupBox = QGroupBox('Результат теста')
label_1_Result = QLabel('правильный ответ или не правельный?')
label_1_Corect = QLabel('Ответ будет находится тут!')

layout_true = QVBoxLayout()
layout_true.addWidget(label_1_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_true.addWidget(label_1_Corect, alignment = (Qt.AlignCenter))
AnsGroupBox.setLayout(layout_true)

main = QVBoxLayout()
main.addLayout(line_h_1)
main.addWidget(RadioGroupBox)
main.addWidget(AnsGroupBox)
main.addWidget(btn_OK)

window.setLayout(main)

AnsGroupBox.hide()

btn_OK.clicked.connect(action)
ask('вопрос', 'r_1', 'r_2', 'r_3', 'r_4')                     ''' Тут переписать через объект ask(Question('вопрос', 'r_1', 'r_2', 'r_3', 'r_4'))  '''
window.show()
app.exec()
