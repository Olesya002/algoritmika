from random import randint
from flask import Flask, session, redirect, url_for
from sql_queries import get_question_after

quiz_id = 0
question_id = 0

def index():
    global quiz_id, question_id
    quiz_id = 3
    question_id = 0
    return '<a href="/test">Тест</a>'

def test():
    global question_id
    result = get_question_after(question_id, quiz_id)
    if result is None:
        return redirect(url_for('result'))
    else:
        question_id  = result[0]
        return '<h1>' + str(quiz_id) + '<br>' + str(result) + '</h1>'
    
def result():
    return "that's all folks!"


app = Flask(__name__) # создаём объект веб-приложения

app.add_url_rule('/', 'index', index)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)

if __name__ == "__main__":
    app.run()  # запускаем веб-сервер
