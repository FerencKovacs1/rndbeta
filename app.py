from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm
from flask_mail import Message, Mail

application = Flask(__name__)
app = application
mail = Mail()


app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'yepense@gmail.com'
app.config["MAIL_PASSWORD"] = 'Humu78945107'

mail.init_app(app)




@app.route('/', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('main.html', form=form)
    else:
      msg = Message(form.subject.data, sender='yepense@gmail.com', recipients=['yepense@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return redirect(url_for('contact'))


  elif request.method == 'GET':
    return render_template('main.html', form=form)





if __name__  == '__main__':
    app.run(debug=True)
