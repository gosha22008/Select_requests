import sqlalchemy

db = 'postgresql://user_1:user_1_55555@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# 1.название и год выхода альбомов, вышедших в 2018 году;
request = f'''
    SELECT name, year FROM album
        WHERE year = 2018
    '''
for i in connection.execute(request):
    print(i)
print('-'*30)

## 2.название и продолжительность самого длительного трека;
request = f'''
    SELECT name, long FROM track
        ORDER BY long DESC
        LIMIT 1
    '''
for i in connection.execute(request):
    print(i)
print('-'*30)

## 3.название треков, продолжительность которых не менее 3,5 минуты;
request = f'''
    SELECT name FROM track
        WHERE long >= 3.5*60
    '''
for i in connection.execute(request):
    print(i)
print('-'*30)

## 4.названия сборников, вышедших в период с 2018 по 2020 год включительно;
request = f'''
    SELECT name FROM collection
        WHERE year BETWEEN 2018 and 2020
    '''
for i in connection.execute(request):
    print(i)
print('-'*30)

## 5.исполнители, чье имя состоит из 1 слова;
request = f'''
    SELECT name FROM executor
        WHERE name NOT LIKE '%% %%';
    '''
for i in connection.execute(request):
    print(i)
print('-'*30)

## 6.название треков, которые содержат слово "мой"/"my".
request = f'''
    SELECT name FROM track
        WHERE name iLIKE '%%мой%%' or name iLIKE '%%my%%'
    '''
for i in connection.execute(request):
    print(i)