import pandas as pd
from flask import Flask, jsonify # modifica o dicionário para o formato JSON

app = Flask(__name__)

# aqui será constuindas as funcionalidades
@app.route('/')
def homepage():
    return 'A api está no ar'

@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('assets/advertising.csv')
    total_vendas =  tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)

# rodar a nossa api
app.run(host='0.0.0.0')



