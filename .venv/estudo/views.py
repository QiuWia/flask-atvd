from estudo import app
from flask import render_template

@app.route('/')
def homepage():
    usuario = 'quilvia'
    return render_template('index.html', usuario=usuario)
