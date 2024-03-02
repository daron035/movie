import json, os, time, datetime, pprint
import sqlite3 as sq


cur_path = os.path.dirname(__file__)
os.chdir(cur_path)

with open('db1.json', 'r') as f:
    data = json.load(f)
    
# pprint.pprint(data[0][0]['kinopoiskId']) # id
# pprint.pprint(data[0][1]['budget']) # budget
    
    
    
print(data[0][0]['kinopoiskId']) # id
print(data[0][0]['nameRu']) # title
print(data[0][0]['slogan']) # tagline
print(data[0][0]['description']) # description
print(data[0][0]['posterUrl']) # posterUrl
print(data[0][0]['year']) # age
print(data[0][0]['slogan']) # tagline
print(data[0][0]['countries'][0]['country']) # country
print(data[0][1]['budget']) # budget
print(data[0][0]['nameRu']) # url
print(1) # category_id
print(True) # is_published
print(datetime.datetime.now()) # time_create
print(datetime.datetime.now()) # time_update

# mov = [data[1]['kinopoiskId'], data[1]['nameRu']]
