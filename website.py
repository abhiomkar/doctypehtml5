#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Website server for doctypehtml5.in
"""

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=301)

app.config.from_object(__name__)
#app.config.from_object('settings')

if __name__ == '__main__':
    app.run(debug=True)
