import csv
from flask import Flask, render_template, url_for, request, redirect
from admin import general_information, experiences, projects
from email.mime.text import MIMEText
from smtplib import SMTP_SSL as SMTP
from dotenv import load_dotenv
import os

load_dotenv('.env')

app = Flask(__name__)

SMTP_SERVER = os.environ.get("SMTP_SERVER", "")
PORT = 465
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
        try:
            contents = f"Name: {name}" + "\n" + f"Email: {email}" + "\n" + f"Message: {message}"
            msg = MIMEText(contents)
            msg["Subject"] = subject
            
            with SMTP(SMTP_SERVER, PORT) as server:
                server.ehlo()
                server.login(general_information["email"], PASSWORD)
                server.sendmail(email, RECEPIENT_EMAIL, msg=msg.as_string())
            
            return redirect(url_for("thank_you"))
        except Exception as e:
            return str(e)
    return render_template('index.html', information=general_information, exp=experiences, projects=projects)

@app.route('/portfolio-details/<int:portfolio_id>')
def portfolio_details(portfolio_id):
    details = projects[portfolio_id - 1]
    if "images" in details:
        for image in details['images']:
            image['index'] = details['images'].index(image)
    return render_template('portfolio-details.html', details=details)

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


if __name__ == "__main__":
    app.run(debug=True)