import requests, json
import matplotlib.pyplot as plt

URL = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/'

print('Gerador de nomes')
name = input('Digite um nome: ')

data = json.loads(requests.get(URL + name.lower()).text)[0]['res']

x = []
y = []

for _ in data:
    try:
        if data.index(_) == 0:
                x.append(int(_['periodo'][0:4]))
        else:
            x.append(int(_['periodo'][1:5]))
        y.append(int(_['frequencia']))
    except:
        pass

plt.plot(x, y)
plt.xlabel(name)
plt.show()
