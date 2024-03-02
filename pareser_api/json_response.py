import requests, json, os, time

cur_path = os.path.dirname(__file__)
os.chdir(cur_path)


HEADERS = {
    'Authorization': 'Token f3820ac3-3c1e-4396-9d4b-7bac33e02d7c',
    'Content-Type': 'application/json',
}
    
l = []
for id in range(1, 2):
    general = requests.get(f'https://kinopoiskapiunofficial.tech/api/v2.2/films/top?type=TOP_250_BEST_FILMS&page={id}', headers=HEADERS)
    data_1 = general.json()
    for i in range(len(data_1["films"])):
        try:
            id_m = data_1["films"][i]["filmId"]
            l.append(id_m)
        except:
            print('EXIT')
        finally:
            continue


json_data = []            
for i in l[:3]:
    response = requests.get(f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{i}', headers=HEADERS)
    time.sleep(1)
    budget = requests.get(f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{i}/box_office', headers=HEADERS)
    data = response.json()
    data_2 = budget.json()
    print(data_2)
    b = data_2['items'][-1]['amount']
    json_data.append((data, {'budget': b}))

try:
    with open('db1.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
except:
    print('EXIT WRITE')