import requests

link = 'http://127.0.0.1:5000/pegarvendas'

requisicao = requests.get(link)

print(requisicao) # response 200 ok
print(requisicao.json()) # resultado no formato Json

dicionario = requisicao.json()
print(dicionario['total_vendas']) # Resultado sem formato Json