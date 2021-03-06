from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from random import randint
import json
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('ID астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username_captain = StringField('ID капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')


@app.route('/<title>')
@app.route('/index/<title>')
def colon(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('train.html', name=prof, title='Тренировка')


@app.route('/list_prof/<param>')
def list_prof(param):
    return render_template('jobs.html', name=param, title='Профессии')


@app.route('/answer', methods=['POST', 'GET'])
@app.route('/auto_answer', methods=['POST', 'GET'])
def answer():
    return render_template('auto_answer.html', title='Регистрация')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '''Login successful'''
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    staff = ['Энди Уир', 'Марк Мёрфи', 'Виктор Викторов', 'Венката Капур', 'Шон Бин', 'Тедди Сандерс']
    return render_template('distribution.html', people=staff)


@app.route('/table/<sex>/<int:age>')
def room_decor(sex, age):
    return render_template('table.html', sex=sex, age=age)


@app.route('/member')
def member():
    with open('staff.json', encoding='utf-8') as f:
        file = f.read()
    file_json = json.loads(file)
    return render_template('member.html', member=file_json[str(randint(1, 5))])


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    files = list(os.listdir('static/img/views'))
    print(files)
    if request.method == 'POST':
        file = request.files['file']
        number = len(files) + 1
        file.save(f'static/img/views/{number}.jpg')
        files = list(os.listdir('static/img/views'))
        return render_template('photo_upload.html', files=files)
    elif request.method == 'GET':
        files = list(os.listdir('static/img/views'))
        return render_template('photo_upload.html', files=files)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')