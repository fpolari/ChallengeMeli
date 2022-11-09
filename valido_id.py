import requests

url  = 'https://6f008c57-99e0-4a2e-8d80-782a71cf99db.mock.pstmn.io/orders/4114999549'
data = requests.get(url)
id_cons = {'id' : '4114999549'}
if data.status_code == 200:
    consulto = data.json()

id_url = consulto["id"]

for e in id_cons.values():
    if id_url == e:
        print ("ID recibido diferente")
    else:
      print ("ID recibido OK")
