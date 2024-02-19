import csv
from flask import Flask, render_template, url_for, request, redirect
from admin import skills, general_information, experience, projects
from email.mime.text import MIMEText
from smtplib import SMTP_SSL as SMTP
import os
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"

SMTP_SERVER = os.environ.get("SMTP_SERVER", "")
PORT = os.environ.get("PORT", 0)
RECEPIENT_EMAIL = os.environ.get("RECEPIENT_EMAIL", "")   
PASSWORD = os.environ.get("PASSWORD", "")

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
        
        mail=SMTP(host=SMTP_SERVER, port=PORT)
        
        mail.login(general_information["email"], PASSWORD)
        
        contents = f"Name: {name}" + "\n" + f"Email: {email}" + "\n" + f"Message: {message}"

        msg = MIMEText(contents)
        msg["Subject"] = subject
        
        mail.sendmail(email, RECEPIENT_EMAIL, msg=msg.as_string())
        mail.close()
        return redirect(url_for("thank_you"))

    return render_template('index.html', skill_length=skills.items(), information=general_information, exp=experience, projects=projects)

@app.route('/portfolio-details/<int:portfolio_id>')
def portfolio_details(portfolio_id):
    return render_template('portfolio-details.html', details=projects[portfolio_id-1])

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


if __name__ == "__main__":
    app.run(debug=True)