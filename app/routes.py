from app import app
from flask import render_template, url_for

@app.route('/')
def index():
    return render_template("index.html.jinja")

@app.route('/k1')
def k1():
    return render_template('k1.html.jinja')

@app.route('/k2')
def k2():
    return render_template('k2.html.jinja')

@app.route('/k3')
def k3():
    return render_template('k3.html.jinja')

@app.route('/k4')
def k4():
    return render_template('k4.html.jinja')

@app.route('/k5')
def k5():
    return render_template('k5.html.jinja')

@app.route('/k6')
def k6():
    return render_template('k6.html.jinja')

@app.route('/k7')
def k7():
    return render_template('k7.html.jinja')

@app.route('/k8')
def k8():
    return render_template('k8.html.jinja')

@app.route('/k9')
def k9():
    return render_template('k9.html.jinja')

@app.route('/k10')
def k10():
    return render_template('k10.html.jinja')

@app.route('/k11')
def k11():
    return render_template('k11.html.jinja')

@app.route('/k12')
def k12():
    return render_template('k12.html.jinja')