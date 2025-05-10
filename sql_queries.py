import sqlite3


# Вопрос 1. Информация о скольких художниках представлена в базе данных? 
conn = sqlite3.connect('Artistc.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM artists')
data = cursor.fetchall()
print(len(data))
# Вопрос 2. Сколько женщин (Female) в базе?
cursor.execute('SELECT * FROM artists WHERE Gender = "Female"')
data = cursor.fetchall()
print(len(data))
# Вопрос 3. Сколько человек в базе данных родились до 1900 года?
cursor.execute('SELECT * FROM artists WHERE "Birth Year" < "1900"')
data = cursor.fetchall()
print(len(data))

# Вопрос 4*. Как зовут самого пожилого художника?
cursor.execute('SELECT * FROM artists ORDER BY "Birth Year" ')
data = cursor.fetchall()
print(data)