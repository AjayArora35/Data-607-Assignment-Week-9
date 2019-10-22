# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:12:45 2019

@author: ajay arora
"""
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import requests
import json
from pandas.io.json import json_normalize


app = Flask(__name__, template_folder='.')

@app.route('/')
def search():
   return render_template('search.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        criteria = request.form['search']
        params = {'api-key': 'hvHeqqlTzIhjv5GtM0M4WQo5isCzHQ1l', 'q':criteria }
        url = "http://api.nytimes.com/svc/search/v2/articlesearch.json"
        JSONContent = requests.get(url, params=params).json()
        content = json.dumps(JSONContent, indent = 4, sort_keys=True)
        #print(content)
        
        data = json_normalize(JSONContent['response']['docs'])
        #print(len(data))
    
        return render_template('dataset.html', tables=[data.to_html(classes='data')], headers=data.columns.values)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)    