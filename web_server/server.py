import csv
import smtplib
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def my_homepage():
    return render_template('index.html')


@app.route('/<string:page_name>')
def my_homepage2(page_name):
    return render_template(page_name)

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method =='POST':
#         try:
#             data = request.form.to_dict()
#             #write_to_file(data)
#             write_to_csv(data)
#             return redirect('/thankyou.html')
#         except:
#             'Did not save to database'
#     else:
#         return 'something went wrong'


def write_to_file(data):
    with open('database.txt', mode='a', encoding='utf-8') as db:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']

        text_file = db.write(
            f'\nName: {name}, email: {email}, subject: {subject}, message: {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', encoding='utf-8', newline='') as db_csv:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']

        csv_file = csv.writer(db_csv, 'excel')
        csv_file.writerow([name, email, subject, message])


@app.route("/submit_form", methods=["POST"])
def send_email():
    name = request.form.get("name")
    sender_email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")
    transmitter_email = os.environ.get('TRANSMITTER_EMAIL')
    transmitter_login = os.environ.get('TRANSMITTER_LOGIN')
    receiver_email = os.environ.get('RECEIVER_EMAIL')

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(transmitter_email, transmitter_login)
        email_text = f"From: {name}<{sender_email}>\nSubject: {subject}\n\n{message}\nThis message is from:<{sender_email}>"
        server.sendmail(transmitter_email,
                        receiver_email, email_text.encode("utf-8"))
        server.quit()
        return redirect('/thankyou.html')
    except Exception as e:
        return f"Failed to send email: {e}"


if __name__ == "__main__":
    app.run()
