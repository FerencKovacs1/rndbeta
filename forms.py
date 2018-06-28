from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError
from flask_wtf import Form



class ContactForm(Form):
  name = TextField("Név",  [validators.Required("Írd ide a neved.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Nem megfelelő Email formátum")])
  subject = TextField("Tárgy",  [validators.Required("Please enter a subject.")])
  message = TextAreaField("Üzenet",  [validators.Required("Please enter a message.")])
  submit = SubmitField("Küldés")
