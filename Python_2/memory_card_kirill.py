#создай приложение для запоминания информации
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton
from random import shuffle
aprosi = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Опрос') 

btn = QPushButton('Отправить ответ')
qstn = QLabel('Какой национальности не существует?')


RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Эльфы')
rbtn_3 = QRadioButton('Негры')
rbtn_4 = QRadioButton('Мордва')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

RadioSoloBox = QGroupBox('Варианты ответов:')   ''' после этой строки нужно дописать создание второй формы, в которой будет результат '''
# сначала создай надпись QLabel (*)
# создай верткальную линию
# закрепи надпись на линию
# закрепи линию в группу

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

''' добавь себе этот класс '''
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



def ask(question, right_answer, wrong1, wrong2, wrong3):    ''' в скобках поставь q '''
    shuffle(answers)
    answers[0].setText(right_answer)                        ''' в скобках поставь q.right_answer '''
    answers[1].setText(wrong1)                              ''' в скобках поставь q.wrong1 '''
    answers[2].setText(wrong2)                              ''' в скобках поставь q.wrong2 '''
    answers[3].setText(wrong3)                              ''' в скобках поставь q.wrong3 '''
    ques.setText(question)                                  ''' в скобках поставь q.question + замени ques на qstn '''
    ans.setText(right_text)                                 ''' в скобках поставь q.right_answer + замени ans на надпись (*) '''

''' функция для отображения формы с вопросом '''
def show_question():
    RadioSoloBox.hide()
    RadioGroupBox.show()
    btn.setText('Отправить ответ')

''' функция для отображения формы с ответом '''
def show_result():
    RadioGroupBox.hide()
    RadioSoloBox.show()
    btn.setText('Продолжить')

''' функция для обработки события нажатия на кнопку '''
def test():
    if btn.text() == 'Отправить ответ':
        show_result()
    else:
        show_question()
      
''' забиндим функцию на кнопку '''
btn.clicked.connect(test)

line = QVBoxLayout()
line.addWidget(qstn)
line.addWidget(RadioGroupBox)
''' здесь необходимо закрепить вторую группу RadioSoloBox на линию line: line.addWidget(RadioSoloBox) '''
''' и сразу же скрыть её: RadioSoloBox.hide() '''
line.addWidget(btn)
main_win.setLayout(line)

main_win.show()
aprosi.exec()
