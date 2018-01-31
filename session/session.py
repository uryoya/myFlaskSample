from flask import Flask, render_template, session, url_for, redirect, request

app = Flask(__name__)
app.secret_key = 'SECURE_SECRET_KEY'
USERNAME = 'uryoya'
PASSWORD = 'password'

@app.route('/')
def index():
    signined = 'username' in session
    print(signined)
    username = session['username'] if signined else ''
    return render_template('index.html', signined=signined, username=username)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html', message=None)
    if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
        session['username'] = USERNAME
        return redirect(url_for('index'))
    else:
        return render_template('signin.html', message='ユーザ名かパスワードが間違っています。')

@app.route('/signout', methods=['GET'])
def signout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

