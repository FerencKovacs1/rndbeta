from flask import Flask, render_template, request



5 application = Flask(__name__)

6 app = application

@app.route('/')
def index():
    return render_template('main.html')



if __name__  == '__main__':
    app.run
