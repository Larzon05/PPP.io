from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_homepage():
    return render_template('index.html')

@app.route('/<string:page_name>')
def my_homepage2(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            'Did not save to database'
    else:
        return 'something went wrong'

def write_to_file(data):
    with open('database.txt',mode='a', encoding='utf-8') as db:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        
        text_file = db.write(f'\nName: {name}, email: {email}, subject: {subject}, message: {message}')
        
def write_to_csv(data):
    with open('database.csv',mode='a', encoding='utf-8',newline='') as db_csv:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        
        csv_file = csv.writer(db_csv,'excel')
        csv_file.writerow([name,email,subject,message])