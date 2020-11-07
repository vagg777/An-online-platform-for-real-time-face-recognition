import os
import urllib
import cv2                              # pip install opencv-python
from flask import *                     # pip install Flask
import MySQLdb                          # pip install mysqlclient
from time import gmtime, strftime
import time
import numpy as np
import datetime
import urllib.request
from cameraController import *
from scipy.spatial import distance      # pip install scipy
import math
from EnglishLanguage import *
from GreekLanguage import *

app = Flask(__name__)
mydb = MySQLdb.connect(db="criminal_detection", host="localhost", user="root", passwd="", charset='utf8')
camera_feed_1_location = "RU6 Lab"
site_language = "Greek"
detection_time = 0.0
average_detection_time = 0.0
video_filter = ""
global_full_name = ""
login_role = ""
loggedin_user_email = ""

@app.route('/manage_users', methods=['GET', 'POST'])
def manage_users():
    global site_language
    global login_role
    if site_language == "Greek":
        manageUser = ManageUserGR()
        header = HeaderGR()
        messages = MessagesGR()
        manage = ManageGR()
        insertUser = InsertUserGR()
    else:
        manageUser = ManageUserEN()
        header = HeaderEN()
        messages = MessagesEN()
        manage = ManageEN()
        insertUser = InsertUserEN()
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM users")
        result = sql.fetchall()
        if result:
            if site_language == "Greek":
                if site_language == "Greek":
                    result = users_translate_to_Greek(manageUser, result)
            return render_template('manage_users.html', result=result, header=header, messages=messages, manageUser=manageUser, manage=manage, login_role=login_role, insertUser=insertUser)
        else:
            return render_template('manage_users.html', error=messages.norecordfound, header=header, messages=messages, manageUser=manageUser, manage=manage, login_role=login_role, insertUser=insertUser)
    elif request.method == 'POST':
        try:
            user_id = str(request.form["id"])
            user_username = str(request.form["username"])
            user_password = str(request.form["password"])
            user_email = str(request.form["email"])
            user_fullname = str(request.form["full_name"])
            user_gender = str(request.form["gender"])
            user_biography = str(request.form["biography"])
            user_work_phone = str(request.form["work_phone"])
            user_mobile_phone = str(request.form["mobile_phone"])
            user_role = str(request.form["role"])
            user_avatar = str(request.form["avatar"])
            sql = mydb.cursor()
            query = """UPDATE users SET username=%s, password=%s, email=%s, full_name=%s, gender=%s, biography=%s, work_phone=%s, mobile_phone=%s, role=%s, avatar=%s WHERE user_id=%s"""
            query_input = (user_username, user_password, user_email, user_fullname, user_gender, user_biography, user_work_phone, user_mobile_phone, user_role, user_avatar, user_id)
            sql.execute(query, query_input)
            mydb.commit()
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users")
            result = sql.fetchall()
            if result:
                if site_language == "Greek":
                    if site_language == "Greek":
                        result = users_translate_to_Greek(manageUser, result)
            return render_template('manage_users.html', success=messages.recordupdated, result=result, header=header, messages=messages, manageUser=manageUser, login_role=login_role, insertUser=insertUser)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users")
            result = sql.fetchall()
            return render_template('manage_users.html', error=messages.sqlerror, result=result, header=header, messages=messages, manageUser=manageUser, login_role=login_role, insertUser=insertUser)
        finally:
            pass



@app.route('/insert_users', methods=['GET', 'POST'])
def insert_users():
    global site_language
    global login_role
    if site_language == "Greek":
        manageUser = ManageUserGR()
        insertUser= InsertUserGR()
        header = HeaderGR()
        messages = MessagesGR()
    else:
        manageUser = ManageUserEN()
        insertUser = InsertUserEN()
        header = HeaderEN()
        messages = MessagesEN()
    if request.method == 'GET':
        return render_template('insert_users.html', header=header, messages=messages, insertUser=insertUser, manageUser=manageUser, login_role=login_role)
    elif request.method == 'POST':
        try:
            username = str(request.form["username"])
            password = str(request.form["password"])
            email = str(request.form["email"])
            full_name = str(request.form["full_name"])
            gender = str(request.form["gender"])
            biography = str(request.form["biography"])
            work_phone = str(request.form["work_phone"])
            mobile_phone = str(request.form["mobile_phone"])
            role = str(request.form["role"])
            avatar = str(request.form["avatar"])
            sql = mydb.cursor()
            sql.execute("SELECT MAX(user_id) FROM users;")
            id = sql.fetchone()
            user_id = id[0]
            user_id = user_id + 1
            sql.execute("INSERT INTO users (user_id, username, password, email, full_name, gender, biography, work_phone, mobile_phone, role, avatar) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (user_id, username, password, email, full_name, gender, biography, work_phone, mobile_phone, role, avatar))
            mydb.commit()
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users")
            result = sql.fetchall()
            return render_template('manage_users.html', success=messages.successinseruser, result=result, header=header, insertUser=insertUser, manageUser=manageUser, login_role=login_role)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            return render_template('insert_users.html', error=messages.sqlerror, header=header, insertUser=insertUser, manageUser=manageUser, messages=messages, login_role=login_role)
        finally:
            pass



@app.route('/remove_users', methods=['GET', 'POST'])
def remove_users():
    global site_language
    global login_role
    if site_language == "Greek":
        header = HeaderGR()
        messages = MessagesGR()
        manageUser = ManageUserGR()
    else:
        header = HeaderEN()
        messages = MessagesEN()
        manageUser = ManageUserEN()
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM users")
        result = sql.fetchall()
        if result:
            if site_language == "Greek":
                if site_language == "Greek":
                    result = users_translate_to_Greek(manageUser, result)
        return render_template('manage_users.html', result=result, header=header, manageUser=manageUser, login_role=login_role)
    if request.method == 'POST':
        try:
            user_id = str(request.form["row.0"])
            user_username = str(request.form["row.1"])
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users WHERE user_id ='" + user_id + "'")
            user = sql.fetchall()
            if user:
                sql.execute("DELETE FROM users WHERE user_id ='" + user_id + "'")
                mydb.commit()
                sql.close()
                message = messages.deleteduserleft + user_username + messages.deleteduserright
                sql.close()
                sql = mydb.cursor()
                sql.execute("SELECT * FROM users")
                result = sql.fetchall()
                if result:
                    if site_language == "Greek":
                        if site_language == "Greek":
                            result = users_translate_to_Greek(manageUser, result)
                return render_template('manage_users.html', success=message, result=result, header=header, manageUser=manageUser, login_role=login_role)
            else:
                message = messages.nouserleft + user_username + messages.nouserright
                sql.close()
                sql = mydb.cursor()
                sql.execute("SELECT * FROM users")
                result = sql.fetchall()
                if result:
                    if site_language == "Greek":
                        if site_language == "Greek":
                            result = users_translate_to_Greek(manageUser, result)
                return render_template('manage_users.html', error=message, result=result, header=header, manageUser=manageUser, messages=messages, login_role=login_role)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users")
            result = sql.fetchall()
            if result:
                if site_language == "Greek":
                    result = users_translate_to_Greek(manageUser, result)
            return render_template('manage_users.html', error=messages.sqlerror, result=result, header=header, manageUser=manageUser, messages=messages, login_role=login_role)
        finally:
            pass

def users_translate_to_Greek(manageUser, result):
    result_list = list(result)
    counter = 0
    for row in result_list:
        user_list = list(row)
        if user_list[5] == "Male":
            user_list[5] = manageUser.male
        elif user_list[5] == "Female":
            user_list[5] = manageUser.female
        elif user_list[5] == "Other":
            user_list[5] = manageUser.other
        if user_list[9] == "ADMIN":
            user_list[9] = manageUser.admin
        elif user_list[9] == "USER":
            user_list[9] = manageUser.user
        result_list[counter] = tuple(user_list)
        counter = counter + 1
    result = tuple(result_list)
    return result


def single_user_translate_to_Greek(manageUser, user_list):
    if user_list[5] == "Male":
        user_list[5] = manageUser.male
    elif user_list[5] == "Female":
        user_list[5] = manageUser.female
    elif user_list[5] == "Other":
        user_list[5] = manageUser.other
    if user_list[9] == "ADMIN":
        user_list[9] = manageUser.admin
    elif user_list[9] == "USER":
        user_list[9] = manageUser.user
    user = tuple(user_list)
    return user