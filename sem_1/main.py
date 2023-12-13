from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def main_page():
    return render_template('index.html')


@app.route('/men/')
def html_mens():
    return render_template('men.html')


@app.route('/women/')
def html_womens():
    return render_template('women.html')


@app.route('/accessoires/')
def html_accessories():
    return render_template('accessoires.html')


if __name__ == '__main__':
    app.run()
