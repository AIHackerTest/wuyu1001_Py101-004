#!usr/bin/env python3
#-*- coding: utf-8 -*-

from flask import Flask, request, render_template
from API_test import fetchWeather, parse_data
app = Flask(__name__)

history = []
@app.route('/')
def index():
    return render_template('weather.html')
@app.route('/query' )
def do_the_query():
    city = request.args.get('city')
    
    if request.args.get('bnt') == "提交": 
        data = fetchWeather(city)
        get_text, temperature, get_name = parse_data(data)
        history.append(get_name)
        return render_template('query-ok.html', get_text=get_text,
                               temperature=temperature, get_name=get_name)

    elif request.args.get('help') == "帮助":
        return render_template('help.html')

    elif request.args.get('history') == "历史":
        
        return render_template('history.html', history=history)

    else:
        return render_template('weather.html', message="您输入的城市名称有误，请重新输入") # 函数必须有返回值，否则报错, 可以用return ok进行测试


if __name__ == '__main__':
    app.run(debug=True)
