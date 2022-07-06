from flask import Blueprint, render_template, redirect, url_for
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

assignment_4 = Blueprint('assignment_4', __name__,
                         static_folder='static',
                         template_folder='templates')



@assignment_4.route('/partB')
def partB():
    return render_template('partB.html')


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


@assignment_4.route('/assignment4')
def assignment4():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment4.html', users=users_list)


def isExist_func(username):
    isExist = False
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    for user in users_list:
        if username == user.userName:
            isExist = True,
            return isExist
    return isExist


@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    isExist = isExist_func(username)
    if isExist:
        return render_template('assignment4.html', message5='this username already exists',
                               users=users_list)
    if not isExist:
        query = "INSERT INTO users (userName,name, email, password) VALUES ('%s','%s', '%s', '%s')" % (
            username, name, email, password)
        interact_db(query=query, query_type='commit')
        query1 = 'select * from users'
        users_list = interact_db(query1, query_type='fetch')
        return render_template('assignment4.html',
                               message3='User Inserted',
                               users=users_list)
    return render_template('assignment4.html',
                           message3='User Inserted',
                           users=users_list)


@assignment_4.route('/update_user', methods=['POST'])
def update_user_func():
    query1 = 'select * from users'
    users_list = interact_db(query1, query_type='fetch')
    username = request.form['usernameU']
    isExist = isExist_func(username)
    if not isExist:
        return render_template('assignment4.html', message6='this username does not exists', users=users_list)
    if isExist:
        query = 'select * from users'
        users_list = interact_db(query, query_type='fetch')
        for user in users_list:
            if username == user.userName:
                if request.form['nameU'] == "":
                    Uname = user.name
                else:
                    Uname = request.form['nameU']
                if request.form['emailU'] == "":
                    email = user.email
                else:
                    email = request.form['emailU']
                if request.form['passwordU'] == "":
                    password = user.password
                else:
                    password = request.form['emailU']
        query = "UPDATE users SET name = '%s', email = '%s', password = '%s' where userName = '%s'" % (
            Uname, email, password, username)
        interact_db(query=query, query_type='commit')
        query1 = 'select * from users'
        users_list = interact_db(query1, query_type='fetch')
        return render_template('assignment4.html',
                               message3='User Updated',
                               users=users_list)
        return render_template('assignment4.html',
                           message3='User Updated',
                               users=users_list)


@assignment_4.route('/delete_user', methods=['POST'])
def delete_user_func():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    username = request.form['usernameD']
    isExist = isExist_func(username)
    if username == '':
        return render_template('assignment4.html',
                               message4='no user selected',
                               users=users_list)
    elif not isExist:
        return render_template('assignment4.html',
                               message4='this user does not exist',
                               users=users_list)
    else:
        query = "DELETE FROM users WHERE userName='%s';" % username
        interact_db(query, query_type='commit')
        query1 = 'select * from users'
        users_list = interact_db(query1, query_type='fetch')
        return render_template('assignment4.html',
                               message3='User Deleted',
                               users=users_list)
    return render_template('assignment4.html',
                           message3='User Deleted',
                           users=users_list)


@assignment_4.route('/users', methods=['GET'])
def get_usersList():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    users_array = []
    for user in users_list:
        users_array.append({
            'username': user.userName,
            'name': user.name,
            'email': user.email
        })
    return jsonify(users_array)


@assignment_4.route('/outer_source', methods=['GET', 'POST'])
def outer_source():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    id = request.form['id']
    intId = int(request.form['id'])
    if intId > 12:
        return render_template('partB.html', message1="no user with this id", users=users_list)
    else:
        result = requests.get('https://reqres.in/api/users/' + id)
        return render_template('partB.html', user=result.json()['data'], users=users_list)


@assignment_4.route('/restapi_users/', defaults={'USER_ID': 6})
@assignment_4.route('/restapi_users/<int:USER_ID>')
def get_user(USER_ID):
    query = "select * from users where id='%s'" % USER_ID
    user = interact_db(query, query_type='fetch')
    if user:
        return jsonify(user)
    else:
        return jsonify({
            'error': '404',
            'message': 'User not found!!'
        })


