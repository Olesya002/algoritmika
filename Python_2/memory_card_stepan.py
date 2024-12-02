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
def ask(q,qesthon):                                               ''' тут оставить просто q '''
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    inscriptions1.setText(q.qesthon)
    inscriptions1.setText(q.right_answer)                         ''' тут следует записать верный ответ в нужный виджет (у тебя это rc1) '''
class Qesthon:
    def __init__(self,qesthon,right_answer,wrong1,wrong2,wrong3):
        self.qesthon = qesthon
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong2                                      ''' тут self.wrong3 = wrong3 '''
    
qesthon1 = []
qesthon1.append(Qesthon('Самое глубокое озеро в Мире?','байкал','	Танганьика','Восток','Ладожское озеро'))
qesthon1.append(Qesthon('Самый холодный Город в России?','Оймякон','Сочи','Санкт-Петербург','Мурманск'))
qesthon1.append(Qesthon('Год основания Санкт-Петербурга?','1703','1941','1305','1605'))
app = QApplication([])
window = QWidget()

lind = QVBoxLayout()
inscriptions1 = QLabel('тест')                                                       ''' это надпись для вопроса (именно в нее мы записываем новый вопрос в функции ask) '''
lind.addWidget(inscriptions1)

Randobox = QGroupBox('какая комбинация клафишь копирует выделенный текс?')           ''' тут ты создаешь форму (то, что в скобках - это заголовок для формы с вариантами ответа, можно написать "Варианты") '''
r1 = QRadioButton('ctrl + c')
r2 = QRadioButton('ctrl + v')
r3 = QRadioButton('ctrl + a')
r4 = QRadioButton('crtl + s')
answer = [r1,r2,r3,r4]
v = QVBoxLayout()                                                                    ''' линия v пусть будет для формы unRandobox '''
unRandobox = QGroupBox('какая комбинация клафишь копирует выделенный текст?')        ''' в скобках заголовок для формы - можно написать "Результат" '''
rc1 = QLabel('Правильный ответ \n crtl + c')                                         ''' это надпись для верного ответа (она должна быть в форме unRandobox и именно в нее мы записываем правильный ответ в ф-ии ask). '''
v.addWidget(r1)                                                                      ''' закрепи rc1 на v: v.addWidget(rc1) + затем закрепи эту линию в группу: unRandobox.setLayout(v) ''' 
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
