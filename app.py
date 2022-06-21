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

@app.route('/order')
def order_page1():
    return render_template('order.html')


catalog_cookies = {
    'chocolate chip': {'price': '4$', 'calories': 200},
    'peanut butter': {'price': '5$', 'calories': 300},
    'kinder': {'price': '5$', 'calories': 250},
    'amsterdam': {'price': '5.5$', 'calories': 250},
    'nutella': {'price': '4.5$', 'calories': 300},
}
@app.route('/clear')
def clear_func():
    return redirect(url_for('catalog_func'))

@app.route('/order')
def goToOrder_func():

    return redirect('/signUp')

@app.route('/catalog')
def catalog_func():
    if 'cookie_name' in request.args:
        cookie_name = request.args['cookie_name']
        if cookie_name in catalog_cookies:
            return render_template('assignment3_1.html',
                                   cookie_name=cookie_name,
                                   cookie_price=catalog_cookies[cookie_name]['price'],
                                   cookie_calories=catalog_cookies[cookie_name]['calories'])
        elif cookie_name == '':
            return render_template('assignment3_1.html',
                                   catalog_cookies=catalog_cookies)
        else:
            return render_template('assignment3_1.html',
                                   message='Sorry, we do not have this kind of cookie.')
    return render_template('assignment3_1.html',
                           catalog_cookies=catalog_cookies)

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
                                   name=catalog_Users[user_name]['name'],
                                   email=catalog_Users[user_name]['email'])
        elif user_name == '':
            return render_template('assignment3_2.html',
                                   catalog_Users=catalog_Users)
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
                                       message1='Wrong password!')
        else:
            return render_template('assignment3_2.html',
                                   message1='Please log in!')
    return render_template('assignment3_2.html')

@app.route('/log_out')
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('login_func'))


