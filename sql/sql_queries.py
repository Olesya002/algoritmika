import sqlite3

conn = sqlite3.connect('quiz.sqlite')
cursor = conn.cursor()

cursor.execute('''PRAGMA foreign_keys=on''')

cursor.execute('''DROP TABLE IF EXISTS quiz_content''')
cursor.execute('''DROP TABLE IF EXISTS question''')
cursor.execute('''DROP TABLE IF EXISTS quiz''')

cursor.execute('''CREATE TABLE IF NOT EXISTS quiz 
              (id INTEGER PRIMARY KEY,
              name VARCHAR)''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS quiz 
              (id INTEGER PRIMARY KEY,
              name VARCHAR)''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS question (
              id INTEGER PRIMARY KEY,
              question VARCHAR,
              answer VARCHAR,
              wrong1 VARCHAR,
              wrong2 VARCHAR,
              wrong3 VARCHAR)''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS quiz_content (
              id INTEGER PRIMARY KEY,
              quiz_id INTEGER,
              question_id INTEGER,
              FOREIGN KEY (quiz_id) REFERENCES quiz (id),
              FOREIGN KEY (question_id) REFERENCES question (id) )
''')
conn.commit()

quizes = [
        ('Своя игра', ),
        ('Кто хочет стать миллионером?', ),
        ('Самый умный', )]

questions = [
        ('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один', 'Ни одного', 'Два'),
        ('Каким станет зеленый утес, если упадет в Красное море?', 'Мокрым', 'Красным', 'Не изменится', 'Фиолетовым'),
        ('Какой рукой лучше размешивать чай?', 'Ложкой', 'Правой', 'Левой', 'Любой'),
        ('Что не имеет длины, глубины, ширины, высоты, а можно измерить?', 'Время', 'Глупость', 'Море', 'Воздух'),
        ('Когда сетью можно вытянуть воду?', 'Когда вода замерзла', 'Когда нет рыбы', 'Когда уплыла золотая рыбка', 'Когда сеть порвалась'),
        ('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар', 'Парашют', 'Облако')]


cursor.executemany('''INSERT INTO question 
                    (question, answer, wrong1, wrong2, wrong3) 
                    VALUES (?,?,?,?,?)''', questions)
conn.commit()

cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizes)
conn.commit()

q = input('Хотите ли установить новую связь между вопросом и викториной (y/n)?')
while q != 'n':
    id_q = input('Id вопроса: ')
    id_v = input('Id викторины: ')
    try:
        cursor.execute('''INSERT INTO quiz_content
                        (quiz_id, question_id) 
                        VALUES (?,?)''', [id_v, id_q])
    except:
        print('Введен неверный id')
    conn.commit()
    q = input('Хотите ли установить новую связь между вопросом и викториной (y/n)?')

# cursor.execute('''SELECT * FROM quiz_content''')
# print(cursor.fetchall())
# cursor.execute('''SELECT * FROM quiz''')
# print(cursor.fetchall())
# cursor.execute('''SELECT * FROM question''')
# print(cursor.fetchall())

# запросы к БД

def get_question_after(question_id=0, quiz_id=1):
    conn = sqlite3.connect('quiz.sqlite')
    cursor = conn.cursor()

    cursor.execute('''SELECT quiz_content.id, question.question, 
                    question.answer, question.wrong1, question.wrong2, question.wrong3
                    FROM question, quiz_content
                    WHERE quiz_content.question_id == question.id
                    AND quiz_content.id > ? AND quiz_content.quiz_id == ?
                    ORDER BY quiz_content.id''', [question_id, quiz_id])
    res = cursor.fetchone()
    cursor.close()
    conn.close()

    return res

cursor.close()
conn.close()
