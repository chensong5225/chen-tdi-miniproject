import requests
import datetime
import simplejson as json
import pandas as pd
from bokeh.plotting import figure, show, output_file, save
from bokeh.layouts import column

def stock_graph(stock_name):

    quandl_apikey = "W1_Zw8zAmSS8XEosenzw"
    quandl_header = "https://www.quandl.com/api/v3/datasets/WIKI"

    end_date = "2018-03-01"
    start_date = "2017-03-01"

    qurl='https://www.quandl.com/api/v3/datasets/WIKI/%s.json?column_index=4&start_date=%s&end_date=%s&api_key=W1_Zw8zAmSS8XEosenzw'%(stock_name, start_date, end_date)
    r = requests.get(qurl)
    if r.status_code != requests.codes.ok: return 0

    data = r.json()['dataset']['data']

    s1 = []
    s2 = []
    for price in data:
        s1.insert(0,pd.Timestamp(price[0]))
        s2.insert(0,price[1])

    df = pd.DataFrame({'date':s1,'price':s2})
    #print(df)

    graph_title = "2017-03-01 ~ 2018-03-01 Stock Price of " + stock_name

    p = figure(x_axis_type="datetime", plot_width=800, plot_height=350, title=graph_title)
    p.line('date', 'price', source=df)

    save(obj=p, filename='templates/stockgraph.html')
    return 1
