from flask import Flask, render_template, request
from Aps import (
    calcular_creditos, calcular_transporte, calcular_energia,
    calcular_gas, calcular_residuos, preco_credito
)

app = Flask(__name__, template_folder="../HTML", static_folder="../CSS")

# Rota da página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota da calculadora
@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    if request.method == 'POST':
        try:
            distancia = float(request.form.get('distancia', 0))
            transporte = request.form.get('transporte')
            combustivel = request.form.get('combustivel')
            kwh = float(request.form.get('kwh', 0))
            botijoes = float(request.form.get('botijoes', 0))
            lixo = float(request.form.get('lixo', 0))
            projeto = request.form.get('projeto')

            emissao_transporte = calcular_transporte(transporte, distancia, combustivel)
            emissao_energia = calcular_energia(kwh)
            emissao_gas = calcular_gas(botijoes)
            emissao_lixo = calcular_residuos(lixo)

            emissao_total = emissao_transporte + emissao_energia + emissao_gas + emissao_lixo
            preco = preco_credito(projeto)
            ton, creditos, custo = calcular_creditos(emissao_total, preco)

            return render_template(
                'calculadora.html',
                resultado=True,
                emissao=emissao_total,
                ton=ton,
                creditos=creditos,
                custo=custo
            )
        except Exception as e:
            return render_template('calculadora.html', erro=str(e))
    return render_template('calculadora.html')

if __name__ == '__main__':
    app.run(debug=True)
