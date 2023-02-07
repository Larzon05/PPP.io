from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def my_homepage():
    return render_template('index.html')

@app.route('/index.html')
def my_homepage2():
    return render_template('index.html')

@app.route('/projects.html')
def my_projects():
    return render_template('projects.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def my_contact():
    return render_template('contact.html')