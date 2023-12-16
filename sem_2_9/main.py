from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/greeting', methods=['GET', 'POST'])
def greeting():
    if request.method == 'POST':
        name = request.form.get('name')
        context = {'name': name}
        return render_template("greeting.html", **context)
    # return redirect(url_for('/index'))
    return redirect("index.html")


@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
