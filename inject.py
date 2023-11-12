import requests

api_key = '748cd0b1-6262-4ab0-bf12-8c549b15cdbf'
word = 'flowers'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)