from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('sign_in.html')


@app.get('/sign_in')
def get_page():
    return render_template('index.html')


@app.post('/sign_in')
def login():
    user = request.form.get('name')
    age = request.form.get('age')
    context = {
        'name': user,
        'age': age
    }
    if int(age) >= 16:
        return render_template('index.html', **context)
    return render_template('error_404.html')


if __name__ == '__main__':
    app.run()
