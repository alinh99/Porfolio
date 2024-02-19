import csv
from flask import Flask, render_template, url_for, request, redirect
from admin import skills, general_information, experience, projects
from email.mime.text import MIMEText
from smtplib import SMTP_SSL as SMTP
import os

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
        try:
            mail=SMTP(SMTP_SERVER, PORT)
            message = f"Name: {name}" + "\n" + f"Email: {email}" + "\n" + f"Message: {message}"
            msg = MIMEText(message, "plain")
            msg["Subject"] = subject
            msg['From'] = email

            mail.set_debuglevel(False)
            mail.starttls()
            mail.login(general_information["email"], PASSWORD)
            
            mail.sendmail(msg['From'],general_information["email"], msg.as_string())
            return redirect(url_for("thank_you"))
        except Exception as e:
            return str(e)
    return render_template('index.html', skill_length=skills.items(), information=general_information, exp=experience, projects=projects)

@app.route('/portfolio-details/<int:portfolio_id>')
def portfolio_details(portfolio_id):
    return render_template('portfolio-details.html', details=projects[portfolio_id-1])

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csvfile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(csvfile)
        writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong!'

if __name__ == "__main__":
    app.run(debug=True)