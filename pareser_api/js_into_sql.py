import json, os, datetime
import sqlite3 as sq

cur_path = os.path.dirname(__file__)
os.chdir(cur_path)
# os.chdir(r'/Users/kamilkusakov/mydoc/PyDocs/PROJECT/mysite:v1:/pareser_api/')

# new_path = os.path.relpath('..\\subfldr1\\testfile.txt', cur_path)


try:
    with open('db1.json', 'r', encoding='utf-8') as f: # , 'r', encoding='utf-8'
        data = json.load(f) # json => python
except Exception:
    print(Exception)
    
# print(data[0][0]['kinopoiskId']) # id
# print(data[0][0]['nameRu']) # title
# print(data[0][0]['slogan']) # tagline
# print(data[0][0]['description']) # description
# print(data[0][0]['posterUrl']) # posterUrl
# print(data[0][0]['year']) # age
# print(data[0][0]['slogan']) # tagline
# print(data[0][0]['countries'][0]['country']) # country
# print(data[0][1]['budget']) # budget
# print(data[0][0]['nameRu']) # url
# print(1) # category_id
# print(True) # is_published
# print(datetime.datetime.now()) # time_create
# print(datetime.datetime.now()) # time_update

t = datetime.datetime.now()
mov = [(data[0][0]['kinopoiskId'], data[0][0]['nameRu'], data[0][0]['slogan'], data[0][0]['description'], data[0][0]['year'], data[0][0]['countries'][0]['country'], data[0][0]['year'], data[0][1]['budget'], 
       'url', 1, True, t, t, data[0][0]['nameRu'], data[0][0]['posterUrl'])] # 15

with sq.connect("db.sqlite3") as con:
    cur = con.cursor()
    
    # cur.execute("""DROP TABLE IF EXISTS test""")
    # cur.execute("""CREATE TABLE IF NOT EXISTS test (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         model INTEGER,
    #         price TEXT
    # )""")
    cur.executemany("INSERT INTO movie_movie  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, ?, ?)", mov)
    # cur.executescript("""UPDATE cars SET model = 'dsfdfgdfgdfgdfgdfg' WHERE model LIKE 'A%';
    #             UPDATE cars SET price = price + 10000000000""")
    con.commit()
    
    
# print(type(data))
# print(data["films"])
# print(data["films"])
# print(type(data["films"][0]["countries"]))
# print(data["films"][0]["countries"][0])
# print(os.listdir())