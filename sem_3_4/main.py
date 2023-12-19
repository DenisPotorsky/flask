from models import User, db
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from reg_form import LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.sqlite'
app.config['SECRET_KEY'] = 'secretkey'
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        name = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'Вы успешно зарегистрировались!'
    return render_template('index.html', form=form)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Created db successfully!')


if __name__ == '__main__':
    app.run()
