import csv
from flask import Flask, render_template, url_for, request, redirect
from admin import general_information, experience, projects
import os
from flask_mail import Mail
from flask_mail import Message

SMTP_SERVER = os.environ.get("SMTP_SERVER", "")
PORT = os.environ.get("PORT", 0)
RECEPIENT_EMAIL = os.environ.get("RECEPIENT_EMAIL", "")   
PASSWORD = os.environ.get("PASSWORD", "")

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']= SMTP_SERVER
app.config['MAIL_PORT'] = PORT
app.config['MAIL_USERNAME'] = RECEPIENT_EMAIL
app.config['MAIL_PASSWORD'] = PASSWORD
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
mail.connect()

@app.route('/thank-you')
def thank_you():
    return render_template('thankyou.html')

@app.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        try:
            msg = Message(subject=subject, sender = email, recipients = [RECEPIENT_EMAIL])
            msg.body = f"Name: {name}" + "\n" + f"Message: {message}"
            
            mail.send(msg)
            
            return redirect(url_for("thank_you"))
        except Exception as e:
            return str(e)
    return render_template('index.html', information=general_information, exp=experience, projects=projects)

@app.route('/portfolio-details/<int:portfolio_id>')
def portfolio_details(portfolio_id):
    return render_template('portfolio-details.html', details=projects[portfolio_id-1])

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


if __name__ == "__main__":
    app.run(debug=True)