
from flask import Flask, render_template, request, redirect
from flask_wtf.csrf import CSRFProtect
from reg_form import LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'secretkey'
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
# db.init_app(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.password})'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        name = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username=name, email=email, password=password)
        try:
            db.session.add(user)
            db.session.commit()
            return 'Вы успешно зарегистрировались!'
        except Exception as e:
            print(e)
            return 'Возникла ошибка'
    else:
        return render_template('login.html', form=form)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Created db successfully!')


if __name__ == '__main__':
    app.run(port=5005)
