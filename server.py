from flask import Flask, render_template, session, redirect, url_for, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template('index.html', visits=session['visits'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/increment', methods=['POST'])
def increment():
    if 'visits' in session:
        session['visits'] += 2 
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    session['visits'] = 0  
    return redirect(url_for('index'))

@app.route('/custom_increment', methods=['POST'])
def custom_increment():
    increment_value = int(request.form.get('increment_value', 0))
    if 'visits' in session:
        session['visits'] += increment_value
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(debug=True)
