#создай приложение для запоминания информации
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox ,QPushButton
from PyQt5.QtCore import Qt
from random import shuffle
def show_test():
    if 'Проверить' == button.text():
        start_test()
    else:
        shot_iscept()
def shot_iscept():
    unRandobox.hide()
    Randobox.show()
    button.setText('Проверить')
def start_test():
    Randobox.hide()
    unRandobox.show()
    button.setText('следующий тест')
def ask(q,qesthon):                               ''' тут оставить просто q '''
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    inscriptions1.setText(q.qesthon)
    inscriptions1.setText(q.right_answer)
class Qesthon:
    def __init__(self,qesthon,right_answer,wrong1,wrong2,wrong3):
        self.qesthon = qesthon
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong2                      ''' тут self.wrong3 = wrong3 '''
    
qesthon1 = []
qesthon1.append(Qesthon('Самое глубокое озеро в Мире?','байкал','	Танганьика','Восток','Ладожское озеро'))
qesthon1.append(Qesthon('Самый холодный Город в России?','Оймякон','Сочи','Санкт-Петербург','Мурманск'))
qesthon1.append(Qesthon('Год основания Санкт-Петербурга?','1703','1941','1305','1605'))
app = QApplication([])
window = QWidget()

lind = QVBoxLayout()
inscriptions1 = QLabel('тест')
lind.addWidget(inscriptions1)

Randobox = QGroupBox('какая комбинация клафишь копирует выделенный текс?')           ''' этот вопрос можешь тоже добавить в список qesthon1 '''
r1 = QRadioButton('ctrl + c')
r2 = QRadioButton('ctrl + v')
r3 = QRadioButton('ctrl + a')
r4 = QRadioButton('crtl + s')
answer = [r1,r2,r3,r4]
v = QVBoxLayout()                                                                   '''линия v у тебя нигде не используется, убери ее вообще'''
unRandobox = QGroupBox('какая комбинация клафишь копирует выделенный текст?')
rc1 = QLabel('Правильный ответ \n crtl + c')                                           ''' эта надпись нигде не используется, убери ее '''
v.addWidget(r1)              ''' убрать '''
v.addWidget(r2)              ''' убрать '''
v.addWidget(r3)              ''' убрать '''
v.addWidget(r4)              ''' убрать '''
layout1 = QVBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

layout2.addWidget(r1)
layout2.addWidget(r2)
layout3.addWidget(r3)
layout3.addWidget(r4)
layout1.addLayout(layout2)
layout1.addLayout(layout3)
Randobox.setLayout(layout1)
lind.addWidget(Randobox)
lind.addWidget(unRandobox)                    '''эта форма с ответом - должна быть скрыта, появится только после нажатия на кнопку: добавь строку ниже unRandbox.hide() '''
window.setLayout(lind)
button = QPushButton('Проверить')
button.clicked.connect(show_test)

lind.addWidget(button)

ask('какая комбинация клафишь копирует выделенный текс?','right_answer','wrong1','wrong2','wrong3')         '''тут переписать, как объект ask(Qesthon('какая комбинация клафишь копирует выделенный текс?','right_answer','wrong1','wrong2','wrong3'))
window.show()
app.exec()
