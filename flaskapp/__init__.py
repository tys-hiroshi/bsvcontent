from flask import Flask

app = Flask(__name__)
app.config.from_object('flaskapp.config')

import flaskapp.views

# 画像のアップロード先のディレクトリ
UPLOAD_FOLDER = './flaskapp/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

