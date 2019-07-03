from flask import Flask
import time

start = time.time()

app = Flask(__name__)

@app.route('/')
def hello_world():
    global start
    end = time.time()
    elapsed = end-start

    resposta = ""
    if elapsed > 120:
        resposta = 'ERRO!!!!!!. Raspberry NÃO está capturando fotos. O ultimo sinal foi a {:.1f} segundos'.format(elapsed)
    else:
        resposta = 'Raspberry está capturando fotos. O ultimo sinal foi a {:.1f} segundos'.format(elapsed)
    return resposta

@app.route('/estouvivo', methods=['GET'])
def estouvivo():
    global start
    start = time.time()
    return 'Parabéns você está vivo!'

if __name__ == '__main__':
    app.run(debug = True)