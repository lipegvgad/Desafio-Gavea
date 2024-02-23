from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import os

app = Flask(__name__)

def criaCarteira():
  if os.path.exists('carteira.json'):
      with open('carteira.json', 'r') as file:
          return json.load(file)
  else:
      return {}


def atualizaCarteira(carteira):
  with open('carteira.json', 'w') as file:
      json.dump(carteira, file)


def achaPrecoAtual(ticker):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}.SA"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        try:
            precoAtual = data['chart']['result'][0]['meta']['regularMarketPrice']
            return precoAtual
        except (KeyError, IndexError):
            return None
    else:
        return None


carteira = criaCarteira()

@app.route('/')
def inicio():
    return render_template('inicio.html', carteira=carteira)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    ticker = request.form['ticker']
    if achaPrecoAtual(ticker)is not None:
      precoCompra = float(request.form['precoCompra'])
      quantidade = int(request.form['quantidade'])

  
      
      if ticker in carteira:
          qtdAnt = carteira[ticker]['quantidade']
          precoAnt = carteira[ticker]['precoCompra']
          precoCompra = (precoAnt * qtdAnt + precoCompra * quantidade) / (qtdAnt + quantidade)
          carteira[ticker]['quantidade'] += quantidade
          carteira[ticker]['precoCompra'] = precoCompra
      else:
          carteira[ticker] = {'quantidade': quantidade, 'precoCompra': precoCompra}
  
     
      atualizaCarteira(carteira)

    return redirect(url_for('inicio'))


@app.route('/lucroprejuizo')
def lucroprejuizo():
    valorTot = 0
    valorInvestido = 0
    posCarteira = 0
    for ticker, info in carteira.items():
        quantidade = info['quantidade']
        precoCompra = info['precoCompra']
        precoAtual = achaPrecoAtual(ticker)
        valorAtual = precoAtual * quantidade
        posCarteira+= valorAtual
        custoTotal= precoCompra * quantidade
        valorInvestido +=custoTotal
        lucroprejuizo = valorAtual - custoTotal
        valorTot += lucroprejuizo
        valorTot= round(valorTot, 2)
        posCarteira= round(posCarteira, 2)

    return render_template('lucroprejuizo.html', valorTot=valorTot, valorInvestido=valorInvestido, posCarteira=posCarteira)


if __name__ == '__main__':
    if not os.path.exists('carteira.json'):
        atualizaCarteira({})
    app.run(host='0.0.0.0', port=8080)

