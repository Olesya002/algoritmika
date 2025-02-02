#создай здесь свой индивидуальный проект!
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


df = pd.read_csv('Python/train.csv')

'''1 - Анализ данных'''
# проверим, есть ли взаимосвязь между признаками result и occupation_type
print(pd.pivot_table(df, columns=['result'], index=['occupation_type'], values=['id'], aggfunc='count'))
# доли купивших и не купивших почти одинаковы --> признак occupation_type


'''Для определения, есть ли взаимосвязь между признаками, следует использовать корреляционную матрицу'''
# correlation = df['result'].corr(df['occupation_type'])
# print(f'Корреляция между продажами и рекламой: {correlation}')
# для ее применения признаки должны иметь численные значения, попробуем применить ее после предобработки данных
'''Метод corr() вычисляет коэффициент корреляции Пирсона, 
который является мерой линейной зависимости между двумя переменными. 
Значение коэффициента Пирсона варьируется от -1 до 1, где значения, близкие к 1 или -1, 
указывают на сильную линейную зависимость, а значения, близкие к 0, 
указывают на слабую или отсутствующую зависимость.'''




'''2 - Предобработка данных'''
print(df.columns)
# удалим столбцы, которые точно нам не нужны
df.drop('id', axis=1, inplace=True)  # id удалим (ни на что не влияет)
df.drop('city', axis=1, inplace=True) # city удалим, потому что сложно преобразовать в число
df.drop('last_seen', axis=1, inplace=True) # last_seen удалим, потому что сложно работать со временем
df.drop('occupation_name', axis=1, inplace=True) # название заведения - сложно преобразовать в число
print(df.columns)

print(df.info())
# перейдем к feature engineering

# разберемся с bdate - сделаем столбец Age
# много пропущенных значений и тип данных - object: заполним пропуски средним возрастом для работающих и учащихся людей
occupation_type = df['occupation_type'].unique()
print(occupation_type)
# видим, что в occupation_type не хватает 193 значений, заполнить сложно, давайте удалим 193 наблюдения
df = df[~df['occupation_type'].isna()]
print(df.info())

university = df[(df['occupation_type'] == 'university') & df['bdate'].notna()]['bdate'].apply(lambda x: int(x.split('.')[2]) if len(x.split('.')) == 3 else 1999).mean()
work = df[(df['occupation_type'] == 'work') & df['bdate'].notna()]['bdate'].apply(lambda x: int(x.split('.')[2]) if len(x.split('.')) == 3 else 1980).mean()
university, work = round(university), round(work)
print(university) # среднийй возраст учащихся 
print(work) # средний возраст работающих

def bdate_to_age(row):
    if pd.isnull(row['bdate']):
        if row['occupation_type'] == 'work':
            return 2025 - work
        if row['occupation_type'] == 'university':
            return 2025 - university
    if len(row['bdate'].split('.')) != 3:
        if row['occupation_type'] == 'work':
            return 2025 - work
        if row['occupation_type'] == 'university':
            return 2025 - university
    return 2025 - int(row['bdate'].split('.')[2])

df['age'] = df.apply(bdate_to_age, axis = 1)
# удаляем bdate
df.drop('bdate', axis = 1, inplace=True)
print(df.info())

df.drop('education_form', axis = 1, inplace=True)

print(df['education_status'].unique()) # можно сделать dummy variables
print(df['langs'].unique())
df.drop('langs', axis = 1, inplace=True)
df.drop('life_main', axis = 1, inplace=True)
df.drop('people_main', axis = 1, inplace=True)
df.drop('education_status', axis = 1, inplace=True)
# occupation_type преобразуем в 0 и 1
df['occupation_type'] = df['occupation_type'].apply(lambda x: 1 if x == 'work' else 0)
print(df.info())
print(df['career_start'].unique())
print(df['career_end'].unique())

def start(df):
    if df['career_start'] == 'False':
        return 0
    if df['career_end'] == 'False':
        return 2025 - int(df['career_start'])
    return int(df['career_end']) - int(df['career_start'])

df['career_age'] = df.apply(start, axis = 1)
df.drop('career_start', axis=1,inplace=True)
df.drop('career_end', axis=1,inplace=True)
print(df.info())

X = df.drop('result', axis = 1)
y = df['result']

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.25)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
classifier = KNeighborsClassifier(n_neighbors = 5)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
print('Процет правильно предсказаныых исходов:', accuracy_score(Y_test, Y_pred))
