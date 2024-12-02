from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ContatoForm(FlaskForm):
    nome = StringField()
    email = StringField()
    assunto = StringField()
    mensagem = StringField()
    btnSubmit = SubmitField()