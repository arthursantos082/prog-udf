import requests
import json

r = requests.get('https://rickandmortyapi.com/api/character/2')

personagem = json.loads(r.text)

print(personagem['name'])