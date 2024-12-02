#создай приложение для запоминания информации
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QRadioButton,QGroupBox,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt
from random import shuffle
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app =   QApplication([])               ''' 13-14 строчки убрать '''
btn =   QPushButton('Ответить')

question_list = []
question_list.append(Question('Кто такой настоящий герой слав?','Злодей Бо Син','Настоящий герой слав это не тот кто в сияющих доспехах и красивой позе...','Булька Барабулька', 'Абаюнда'))
question_list.append(Question('Кто такой кольт?','Тап тапер обрыганный','Сигма бой',"Крыса",'Ягода малинка'))
question_list.append(Question('Кто лучший футболист?','Песси','Роналду','Рональдинио','Их несколько...'))

def ask (question, right_answer, wrong1, wrong2, wrong3):        ''' тут в скобках только q  '''
    shuffle(answer)
    answer[0].setText(right_answer)               ''' тут в скобках q.right_answer '''
    answer[1].setText(wrong1)                     ''' тут в скобках q.wrong1 '''
    answer[2].setText(wrong2)                     ''' тут в скобках q.wrong2 '''
    answer[3].setText(wrong3)                     ''' тут в скобках q.wrong3 '''
    text.setText(question)                        ''' тут в скобках q.question '''
    ab_right.setText(right_answer)                ''' тут в скобках q.right_answer '''


def action():
    if btn.text() == 'Ответить':
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn.setText('продолжить')
    else:
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn.setText('Ответить')

a=QApplication([])
d=QWidget()
text = QLabel('Какой цифры не существует?')
btn = QPushButton('Ответить')
RadioGroupBox = QGroupBox ("Варианты ответов")
rbtn_1 = QRadioButton('3') 
rbtn_2 = QRadioButton ('9') 
rbtn_3 = QRadioButton ('11') 
rbtn_4 = QRadioButton ('1') 
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 =   QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4) 
layout_ans1.addLayout(layout_ans2) 
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)




AnsGroupBox = QGroupBox('Результат')
lb_right = QLabel('Верно/Неверно')
ab_right = QLabel('fhf')
Layout_res = QVBoxLayout()
Layout_res.addWidget(lb_right, alignment=(Qt.AlignLeft | Qt.AlignTop))
Layout_res.addWidget(ab_right, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(Layout_res)


line = QVBoxLayout()
line.addWidget(text)
line.addWidget(RadioGroupBox)
line.addWidget(AnsGroupBox)
line.addWidget(btn)

d.setLayout(line)

AnsGroupBox.hide()
btn.clicked.connect(action)

answer = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

ask("Какой цифры не существует?", '11','3','9','1')               ''' тут сделай ask(Question("Какой цифры не существует?", '11','3','9','1')) '''

d.show()
a.exec_()
