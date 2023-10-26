from flask import Flask , render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello() :
    s1 =  '<p>Hope R. : jm</p>'
    s2 =  '<p>Jack M. : math</p>'
    return s1 + s2

@app.route('/jack')
def wc():
   return render_template('index.html')
