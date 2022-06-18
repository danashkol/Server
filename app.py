from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify


app = Flask(__name__)
app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1000)

@app.route('/')
def home_page1():
    return render_template('home page.html')

@app.route('/signUp')
def signUp_page1():
    return render_template('sign up.html')


catalog_Price = {
    'chocolate chip': '4$',
    'peanut butter': '5$',
    'kinder': '5$',
    'amsterdam': '5.5$',
    'nutella': '4.5$'
}
catalog_Calories = {
    'chocolate chip': 200,
    'peanut butter': 300,
    'kinder': 250,
    'amsterdam': 250,
    'nutella': 300
}

@app.route('/catalog')
def catalog_func():
    if 'cookie_name' in request.args:
        cookie_name = request.args['cookie_name']
        if cookie_name in catalog_Price:
            return render_template('assignment3_1.html',
                                   cookie_name=cookie_name,
                                   cookie_price=catalog_Price[cookie_name],
                                   coolie_calories=catalog_Calories[cookie_name])
        else:
            return render_template('assignment3_1.html',
                                   message='Sorry, we do not have this kind of cookie.')
    return render_template('assignment3_1.html',
                           catalog_Price=catalog_Price)

catalog_Users = {
'User1': {'name': 'Yossi', 'email': 'yos@gmail.com'},
'User2': {'name': 'Shimon', 'email': 'shim@gmail.com'},
'User3': {'name': 'Romi', 'email': 'romi@gmail.com'},
'User4': {'name': 'Noam', 'email': 'noam@gmail.com'},
'User5': {'name': 'Lior', 'email': 'lior@gmail.com'},
}
@app.route('/search')
def users_func():
    if 'user_name' in request.args:
        user_name = request.args['user_name']
        if user_name in catalog_Users:
            return render_template('assignment3_2.html',
                                   user_name=user_name,
                                   name=catalog_Users[user_name],
                                   email=catalog_Users[user_name])
        else:
            return render_template('assignment3_2.html',
                                   message='This user does not exist')
    return render_template('assignment3_2.html',
                           catalog_Users=catalog_Users)

user_dict = {
    'User1': '1234',
    'User2': '2345',
    'User3': '3456',
    'User4': '4567',
    'User5': '5678'
}

@app.route('/log_in', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in user_dict:
            pas_in_dict = user_dict[username]
            if pas_in_dict == password:
                session['username'] = username
                session['logedin'] = True
                return render_template('assignment3_2.html',
                                       username=username)
            else:
                return render_template('assignment3_2.html',
                                       message='Wrong password!')
        else:
            return render_template('assignment3_2.html',
                                   message='Please log in!')
    return render_template('assignment3_2.html')

