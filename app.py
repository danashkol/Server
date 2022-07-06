import requests as requests
from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
import time
import random
from flask import request, session, jsonify
import mysql.connector

import asyncio
import aiohttp

app = Flask(__name__)
app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1000)

from pages.assignment_4.assignment_4 import assignment_4
app.register_blueprint(assignment_4)


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
    return redirect('/order')


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
    'User1': {'name': 'Yossi', 'email': 'yos@gmail.com', 'password': '1234'},
    'User2': {'name': 'Shimon', 'email': 'shim@gmail.com', 'password': '2345'},
    'User3': {'name': 'Romi', 'email': 'romi@gmail.com', 'password': '3456'},
    'User4': {'name': 'Noam', 'email': 'noam@gmail.com', 'password': '4567'},
    'User5': {'name': 'Lior', 'email': 'lior@gmail.com', 'password': '5678'},
}

@app.route('/insertDict', methods=['POST'])
def insertDict():
    for user in catalog_Users:
        username = request.args['user_name']
        name = request.args['name']
        email = request.args['email']
        password = request.args['password']
        query = "INSERT INTO users (userName,name, email, password) VALUES ('%s','%s', '%s', '%s')" % (
            username, name, email, password)
        interact_db(query=query, query_type='commit')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='Root',
                                         database='one')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value



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


@app.route('/log_in', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in catalog_Users:
            pas_in_dict = catalog_Users[username]['password']
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


@app.route('/session')
def session_func():
    return jsonify(dict(session))


