from flask import Flask, render_template, request, redirect
from stock import stock_graph
app_stock = Flask(__name__)

app_stock.vars={}

@app_stock.route('/')
def main():
    return redirect('/index')

@app_stock.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        app_stock.vars['stock_name'] = request.form['stock_name']
        stock_graph(app_stock.vars['stock_name'])
        return redirect('/stockgraph')

@app_stock.route('/stockgraph', methods=['GET','POST'])
def stockgraph():
    if request.method == 'GET':
        return render_template('stockgraph.html')
    else:
        return redirect('/index')

if __name__ == "__main__":
    app_stock.run(debug=True)
