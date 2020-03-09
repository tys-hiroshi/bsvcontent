from flaskapp import app
from flask import request, redirect, url_for, render_template, flash, make_response
import os


@app.route('/')
def index():
    html = render_template('index.html', a = 'index', title="Index")
    return html

@app.route('/hello')
def hello():
    html = render_template('index.html', a = 'aaaa', title="HelloTitle")
    return html
