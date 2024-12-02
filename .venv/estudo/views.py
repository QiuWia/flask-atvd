from estudo import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    usuario = 'quilvia'
    return render_template('index.html', usuario=usuario)



