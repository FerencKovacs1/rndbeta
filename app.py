from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')



if __name__  == '__main__':
    app.run(debug=True)
