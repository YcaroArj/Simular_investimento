from flask import Flask, render_template, request
from services.simular import Simular_investimento
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/simular", methods=['GET', 'POST'])
def simular():
    if request.method == 'POST':
        inv_inicial = float(request.form.get('inv_inicial'))
        inv_mensal = float(request.form.get('inv_mensal'))
        prazo = float(request.form.get('prazo'))
        rentabilidade = float(request.form.get('rentabilidade'))
        
    simulacao = Simular_investimento(inv_inicial, inv_mensal, prazo, rentabilidade)
    
    valor_investido = locale.currency(simulacao.valor_investido() , grouping=True)
    valor_bruto = locale.currency(simulacao.valor_bruto() , grouping=True)
    valor_juros = locale.currency(simulacao.valor_juros() , grouping=True)
    valor_pago_IR = locale.currency(simulacao.valor_pago_IR() , grouping=True)
    valor_liquido = locale.currency(simulacao.valor_liquido() , grouping=True)

    return render_template('index.html', valor_investido=valor_investido, valor_bruto=valor_bruto,
                               valor_juros=valor_juros, valor_pago_IR=valor_pago_IR, valor_liquido=valor_liquido)

