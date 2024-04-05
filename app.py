from flask import Flask, render_template, request
from datetime import datetime
from tinydb import TinyDB, Query

app = Flask(__name__)

db = TinyDB('db.json')

@app.route('/ping')
def ping():
    db.insert({
    "hora":str(datetime.now()),
    "metodo": str(request.method),
    "acao": "Ping/Pong",
    })
    return {"resposta": "pong"}

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    user_input = data.get('dados')
    db.insert({
    "hora":str(datetime.now()),
    "metodo": str(request.method),
    "acao": "Echo",
    })
    return {'resposta': user_input}

@app.route('/dash')
def dash():
    return render_template('logs.html')

@app.route('/info')
def retorna_acessos():
    return render_template('item-log.html', itens=db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)