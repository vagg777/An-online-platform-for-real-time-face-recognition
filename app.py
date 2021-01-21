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
from scipy.spatial import distance      # pip install scipy
import math
from EnglishLanguage import *
from GreekLanguage import *
from camera import *
from faceRecognition import *
import ffmpeg
import logging
import threading
import time
from PIL import Image



app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)
mydb = MySQLdb.connect(db="criminal_detection", host="localhost", user="root", passwd="", charset='utf8')
camera_feed_1_URL = "http://192.168.1.122:8080/video"   # Android Xiaomi Redmi Note 7
camera_feed_2_URL = "http://192.168.1.111:8080/video"   # Android Tablet Huawei Mediapad T3
camera_feed_1_location = "Floor 0 - Camera 1"
camera_feed_2_location = "Floor 0 - Camera 2"
site_language = "Greek"
site_theme = "Dark Theme"
site_fontsize = 14
last_known_location = ""
video_filter = "no"
global_full_name = "Baggelis_Michos"
loggedin_role = ""
loggedin_email = ""
loggedin_user = ""
welcome = ""
login = ""
messages = ""
header = ""
home = ""
insertUser = ""
manageUser = ""
insertCriminal = ""
manageCriminal = ""
manageLivefeed = ""
manage = ""
settings = ""
contact = ""
signup = ""




def nothing(x):
    pass




def checkUserSettings(theme, language, fontsize):
    global welcome
    global login
    global messages
    global header
    global home
    global insertUser
    global manageUser
    global insertCriminal
    global manageCriminal
    global manageLivefeed
    global manage
    global settings
    global contact
    global signup
    global site_fontsize
    global site_language
    global site_theme
    if site_language == "Greek":
        welcome = WelcomeGR()
        signup = SignupGR()
        login = LoginGR()
        messages = MessagesGR()
        header = HeaderGR()
        home = HomeGR()
        insertUser = InsertUserGR()
        manageUser = ManageUserGR()
        insertCriminal = InsertCriminalsGR()
        manageCriminal = ManageCriminalGR()
        manageLivefeed = ManageLivefeedGR()
        manage = ManageGR()
        settings = SettingsGR()
        contact = ContactGR()
    else:
        welcome = WelcomeEN()
        signup = SignupEN()
        login = LoginEN()
        messages = MessagesEN()
        header = HeaderEN()
        home = HomeEN()
        insertUser = InsertUserEN()
        manageUser = ManageUserEN()
        insertCriminal = InsertCriminalsEN()
        manageCriminal = ManageCriminalEN()
        manageLivefeed = ManageLivefeedEN()
        manage = ManageEN()
        settings = SettingsEN()
        contact = ContactEN()
    site_theme = theme
    site_language = language
    site_fontsize = fontsize


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
        if user_list[11] == "Dark Theme":
            user_list[11] = settings.darkTheme
        elif user_list[11] == "Light Theme":
            user_list[11] = settings.lightTheme
        if user_list[12] == "English":
            user_list[12] = settings.english
        elif user_list[12] == "Greek":
            user_list[12] = settings.greek
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
    if user_list[11] == "Dark Theme":
        user_list[11] = settings.darkTheme
    elif user_list[11] == "Light Theme":
        user_list[11] = settings.lightTheme
    if user_list[12] == "English":
        user_list[12] = settings.english
    elif user_list[12] == "Greek":
        user_list[12] = settings.greek
    user = tuple(user_list)
    return user




def criminals_translate_to_Greek(manageCriminal, result_list):
    counter = 0
    for row in result_list:
        criminal_list = list(row)
        if criminal_list[5] == "Black":
            criminal_list[5] = manageCriminal.black
        elif criminal_list[5] == "Brown":
            criminal_list[5] = manageCriminal.brown
        elif criminal_list[5] == "Green":
            criminal_list[5] = manageCriminal.green
        elif criminal_list[5] == "Blue":
            criminal_list[5] = manageCriminal.blue
        elif criminal_list[5] == "Dark Brown":
            criminal_list[5] = manageCriminal.darkbrown
        elif criminal_list[5] == "Amber":
            criminal_list[5] = manageCriminal.amber
        elif criminal_list[5] == "Gray":
            criminal_list[5] = manageCriminal.gray
        if criminal_list[9] == "Male":
            criminal_list[9] = manageCriminal.male
        if criminal_list[9] == "Female":
            criminal_list[9] = manageCriminal.female
        if criminal_list[9] == "Other":
            criminal_list[9] = manageCriminal.other
        result_list[counter] = tuple(criminal_list)
        counter = counter + 1
    result = tuple(result_list)
    return result



@app.route('/')
def start():
    return render_template('welcome.html', welcome=welcome, site_theme=site_theme, site_language=site_language, site_fontsize = site_fontsize, header=header)




@app.route('/welcome')
def welcome():
    return render_template('welcome.html', welcome=welcome, site_theme=site_theme, site_language=site_language, site_fontsize = site_fontsize, header=header)




@app.route('/login', methods=['GET', 'POST'])
def login():
    global loggedin_role
    global loggedin_user
    global loggedin_email
    global site_theme
    global site_language
    global site_fontsize
    if request.method == 'GET':
        return render_template('login.html', login=login, loggedin_role=loggedin_role, loggedin_user=loggedin_user, messages=messages, site_theme=site_theme, site_language=site_language, site_fontsize = site_fontsize, header=header)
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        sql = mydb.cursor()
        sql.execute("SELECT username, role, email, theme, language, fontsize FROM users WHERE email ='" + email + "' AND password = +'" + password + "'")
        user = sql.fetchall()
        if user:
            if len(user) is 1:
                loggedin_role = user[0][1]
                loggedin_user = user[0][0]
                loggedin_email = user[0][2]
                site_theme = user[0][3]
                site_language = user[0][4]
                site_fontsize = user[0][5]
                checkUserSettings(site_theme, site_language, site_fontsize)
                return render_template('home.html', header=header, loggedin_role=loggedin_role, messages=messages, home=home, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        else:
            return render_template('login.html', login=login, messages=messages, error=messages.invalidcredentials, loggedin_role=loggedin_role, site_theme=site_theme, site_language=site_language, site_fontsize = site_fontsize, header=header)



@app.route("/signup", methods=['GET', 'POST'])
def signup():
    global loggedin_role
    if request.method == 'GET':
        return render_template('signup.html', signup=signup, messages=messages, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_theme=site_theme, site_language=site_language, site_fontsize = site_fontsize, header=header)
    elif request.method == 'POST':
        try:
            username = str(request.form["username"])
            password = str(request.form["password"])
            email = str(request.form["email"])
            fullname = str(request.form["full_name"])
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
            sql.execute("INSERT INTO users (user_id, username, password, email, full_name, gender, biography, work_phone, mobile_phone, role, avatar) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (user_id, username, password, email, fullname, gender, biography, work_phone, mobile_phone, role, avatar))
            mydb.commit()
            sql.close()
            loggedin_role = role
            return render_template('home.html', success=messages.successsignup, signup=signup, loggedin_role=loggedin_role, loggedin_user=loggedin_user, messages=messages, header=header, home=home, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            return render_template('signup.html', error=messages.sqlerror, signup=signup, loggedin_role=loggedin_role, messages=messages, header=header, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        finally:
            pass



@app.route('/logout')
def logout():
    global loggedin_role
    global loggedin_user
    global loggedin_email
    loggedin_role = ""
    loggedin_email = ""
    loggedin_user = ""
    return render_template('welcome.html', header=header, welcome=welcome, loggedin_role=loggedin_role, loggedin_user=loggedin_user, loggedin_email=loggedin_email, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)



@app.route('/home')
def home():
    return render_template('home.html', header=header, home=home, loggedin_role=loggedin_role, messages=messages, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)



@app.route('/manage')
def manage():
    return render_template('manage.html', header=header, manage=manage, loggedin_role=loggedin_role, loggedin_user=loggedin_user, messages=messages, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html', header=header, contact=contact, messages=messages, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
    elif request.method == 'POST':
        try:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            subject = request.form['subject']
            sql = mydb.cursor()
            sql.execute("SELECT MAX(contact_id) FROM contact;")
            id = sql.fetchone()
            contact_id = id[0]
            contact_id = contact_id + 1
            sql.execute("INSERT INTO contact (contact_id, first_name, last_name, email, subject) VALUES (%s,%s,%s,%s,%s)", (contact_id, firstname, lastname, email, subject))
            mydb.commit()
            sql.close()
            return render_template('contact.html', success=messages.successcontactform, header=header, contact=contact, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_fontsize = site_fontsize, site_theme=site_theme, site_language=site_language)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            return render_template('contact.html', error=messages.sqlerror, header=header, contact=contact, loggedin_role = loggedin_role, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        finally:
            pass



@app.route('/manage_users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM users")
        result = sql.fetchall()
        if result:
            if site_language == "Greek":
                result = users_translate_to_Greek(manageUser, result)
            return render_template('manage_users.html', result=result, header=header, messages=messages, manageUser=manageUser, manage=manage, loggedin_role=loggedin_role, insertUser=insertUser, loggedin_user=loggedin_user, site_language=site_language, site_fontsize = site_fontsize, site_theme=site_theme)
        else:
            return render_template('manage_users.html', error=messages.norecordfound, header=header, messages=messages, manageUser=manageUser, manage=manage, loggedin_role=loggedin_role, insertUser=insertUser, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
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
                        result = users_translate_to_Greek(manageUser, result)
            return render_template('manage_users.html', success=messages.recordupdated, manage=manage, result=result, header=header, messages=messages, manageUser=manageUser, loggedin_role=loggedin_role, insertUser=insertUser, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users")
            result = sql.fetchall()
            return render_template('manage_users.html', error=messages.sqlerror, result=result, manage=manage,  header=header, messages=messages, manageUser=manageUser, loggedin_role=loggedin_role, insertUser=insertUser, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        finally:
            pass



@app.route('/insert_users', methods=['GET', 'POST'])
def insert_users():
    if request.method == 'GET':
        return render_template('insert_users.html', header=header, messages=messages, insertUser=insertUser, manage=manage, manageUser=manageUser, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
    elif request.method == 'POST':
        try:
            username = str(request.form["username"])
            email = str(request.form["email"])
            full_name = str(request.form["full_name"])
            password = str(request.form["password"])
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
            if result:
                if site_language == "Greek":
                    result = users_translate_to_Greek(manageUser, result)
            return render_template('manage_users.html', success=messages.successinseruser, result=result, header=header, insertUser=insertUser, manage=manage, manageUser=manageUser, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users")
            result = sql.fetchall()
            if result:
                if site_language == "Greek":
                    result = users_translate_to_Greek(manageUser, result)
            return render_template('manage_users.html', error=messages.sqlerror, result=result, header=header, insertUser=insertUser, manageUser=manageUser, manage=manage, messages=messages, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_fontsize = site_fontsize, site_theme=site_theme, site_language=site_language)
        finally:
            pass



@app.route('/remove_users', methods=['GET', 'POST'])
def remove_users():
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM users")
        result = sql.fetchall()
        if result:
            if site_language == "Greek":
                result = users_translate_to_Greek(manageUser, result)
        return render_template('manage_users.html', result=result, header=header, manageUser=manageUser, insertUser=insertUser, manage=manage, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
    if request.method == 'POST':
        try:
            user_id = str(request.form["delete_user_id"])
            user_username = str(request.form["delete_user_username"])
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
                        result = users_translate_to_Greek(manageUser, result)
                return render_template('manage_users.html', success=message, result=result, header=header, insertUser=insertUser, manage=manage, manageUser=manageUser, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_fontsize = site_fontsize, site_theme=site_theme, site_language=site_language)
            else:
                message = messages.nouserleft + user_username + messages.nouserright
                sql.close()
                sql = mydb.cursor()
                sql.execute("SELECT * FROM users")
                result = sql.fetchall()
                if result:
                    if site_language == "Greek":
                        result = users_translate_to_Greek(manageUser, result)
                return render_template('manage_users.html', error=message, result=result, header=header, insertUser=insertUser, manage=manage, manageUser=manageUser, messages=messages, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_theme=site_theme,  ite_fontsize = site_fontsize, site_language=site_language)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users")
            result = sql.fetchall()
            if result:
                if site_language == "Greek":
                    result = users_translate_to_Greek(manageUser, result)
            return render_template('manage_users.html', error=messages.sqlerror, result=result, insertUser=insertUser, header=header,manage=manage, manageUser=manageUser, messages=messages, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_fontsize = site_fontsize, site_theme=site_theme, site_language=site_language)
        finally:
            pass



@app.route('/manage_criminals', methods=['GET', 'POST'])
def manage_criminals():
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM criminals")
        result = sql.fetchall()
        if result:
            if site_language == "Greek":
                result = criminals_translate_to_Greek(manageCriminal, list(result))
            return render_template('manage_criminals.html', result=result, header=header, insertCriminal=insertCriminal, manage=manage, messages=messages, manageCriminal=manageCriminal, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        else:
            return render_template('manage_criminals.html', error=messages.norecordfound, header=header, manage=manage, insertCriminal=insertCriminal, messages=messages, manageCriminal=manageCriminal, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
    elif request.method == 'POST':
        try:
            criminal_id = str(request.form["criminal_id"])
            criminal_full_name = str(request.form["criminal_full_name"])
            criminal_age = str(request.form["criminal_age"])
            criminal_height = str(request.form["criminal_height"])
            criminal_weight = str(request.form["criminal_weight"])
            criminal_eye_color = str(request.form["criminal_eye_color"])
            criminal_bio = str(request.form["criminal_bio"])
            criminal_portrait = str(request.form["criminal_portrait"])
            criminal_last_location = str(request.form["criminal_last_location"])
            criminal_gender = str(request.form["criminal_gender"])
            sql = mydb.cursor()
            query = """UPDATE criminals SET full_name= %s, age=%s, height=%s, weight=%s, eye_color=%s, biography=%s, portrait=%s, last_location=%s, gender=%s WHERE criminal_id = %s"""
            query_input = (
            criminal_full_name, criminal_age, criminal_height, criminal_weight, criminal_eye_color, criminal_bio, criminal_portrait, criminal_last_location, criminal_gender, criminal_id)
            sql.execute(query, query_input)
            mydb.commit()
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM criminals")
            result = sql.fetchall()
            if result:
                if site_language == "Greek":
                    result = criminals_translate_to_Greek(manageCriminal, list(result))
            return render_template('manage_criminals.html', manage=manage, success=messages.recordupdated, insertCriminal=insertCriminal, result=result, header=header, messages=messages, manageCriminal=manageCriminal, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            sql = mydb.cursor()
            sql.execute("SELECT * FROM criminals")
            result = sql.fetchall()
            if result:
                if site_language == "Greek":
                    result = criminals_translate_to_Greek(manageCriminal, list(result))
            return render_template('manage_criminals.html', error=messages.sqlerror, manage=manage, result=result, header=header, insertCriminal=insertCriminal, messages=messages, manageCriminal=manageCriminal, loggedin_role=loggedin_role, loggedin_user=loggedin_user, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        finally:
            pass



@app.route('/insert_criminals', methods=['GET', 'POST'])
def insert_criminals():
    if request.method == 'GET':
        return render_template('insert_criminals.html', loggedin_user=loggedin_user, messages=messages, manage=manage, insertCriminal=insertCriminal, manageCriminal=manageCriminal, header=header, loggedin_role=loggedin_role, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
    elif request.method == 'POST':
        try:
            criminal_full_name = str(request.form["fullname"])
            criminal_age = str(request.form["age"])
            criminal_height = str(request.form["height"])
            criminal_weight = str(request.form["weight"])
            criminal_eye_color = str(request.form["eye_color"])
            criminal_biography = str(request.form["biography"])
            criminal_portrait = str(request.form["portrait"])
            criminal_last_location = str(request.form["last_location"])
            criminal_gender = str(request.form["gender"])
            sql = mydb.cursor()
            sql.execute("SELECT MAX(criminal_id) FROM criminals;")
            id = sql.fetchone()
            criminal_id = id[0]
            criminal_id = criminal_id + 1
            sql.execute("INSERT INTO criminals (criminal_id, full_name, age, height, weight, eye_color, biography, portrait, last_location, gender) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (criminal_id, criminal_full_name, criminal_age, criminal_height, criminal_weight, criminal_eye_color,criminal_biography, criminal_portrait, criminal_last_location, criminal_gender))
            mydb.commit()
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM criminals")
            result = sql.fetchall()
            if result:
                if site_language == "Greek":
                    result = criminals_translate_to_Greek(manageCriminal, list(result))
            return render_template('manage_criminals.html', loggedin_user=loggedin_user, success=messages.successinsertcriminal, manage=manage, result=result, insertCriminal=insertCriminal, manageCriminal=manageCriminal, header=header, loggedin_role=loggedin_role, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            return render_template('manage_criminals.html', loggedin_user=loggedin_user, error=messages.sqlerror, manage=manage, messages=messages, insertCriminal=insertCriminal, manageCriminal=manageCriminal, header=header, loggedin_role=loggedin_role, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        finally:
            pass



@app.route('/remove_criminals', methods=['GET', 'POST'])
def remove_criminals():
    if request.method == 'POST':
        try:
            criminal_id = str(request.form["delete_criminal_id"])
            criminal_full_name = str(request.form["delete_criminal_full_name"])
            sql = mydb.cursor()
            sql.execute("SELECT * FROM criminals WHERE criminal_id ='" + criminal_id + "'")
            user = sql.fetchall()
            if user:
                sql.execute("DELETE FROM criminals WHERE criminal_id ='" + criminal_id + "'")
                mydb.commit()
                sql.close()
                message = messages.deletedcriminalleft + criminal_full_name + messages.deletedcriminalright
                sql.close()
                sql = mydb.cursor()
                sql.execute("SELECT * FROM criminals")
                result = sql.fetchall()
                if result:
                    if site_language == "Greek":
                        result = criminals_translate_to_Greek(manageCriminal, list(result))
                return render_template('manage_criminals.html', loggedin_user=loggedin_user, success=message, insertCriminal=insertCriminal, manage=manage, result=result, header=header, manageCriminal=manageCriminal, loggedin_role=loggedin_role, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
            else:
                message = messages.nocriminalleft + criminal_full_name + messages.nocriminalright
                sql.close()
                sql = mydb.cursor()
                sql.execute("SELECT * FROM criminals")
                result = sql.fetchall()
                if result:
                    if site_language == "Greek":
                        result = criminals_translate_to_Greek(manageCriminal, list(result))
                return render_template('manage_criminals.html', loggedin_user=loggedin_user, error=message, result=result, insertCriminal=insertCriminal, manage=manage, header=header, manageCriminal=manageCriminal, messages=messages, loggedin_role=loggedin_role, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM criminals")
            result = sql.fetchall()
            if result:
                if site_language == "Greek":
                    result = criminals_translate_to_Greek(manageCriminal, list(result))
            return render_template('manage_criminals.html', loggedin_user=loggedin_user, error=messages.sqlerror, result=result, insertCriminal=insertCriminal, manage=manage, header=header, manageCriminal=manageCriminal, messages=messages, loggedin_role=loggedin_role, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        finally:
            pass



@app.route('/settings', methods=['GET', 'POST'])
def settings():
    global site_language
    global site_theme
    global site_fontsize
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM users WHERE email ='" + loggedin_email + "'")
        user = sql.fetchall()
        if user:
            if site_language == "Greek":
                user = single_user_translate_to_Greek(manageUser, list(user[0]))
            else:
                user = user[0]
            return render_template('settings.html', loggedin_user=loggedin_user, header=header, messages=messages, loggedin_role=loggedin_role, manageUser=manageUser, user=user, settings=settings, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        else:
            return render_template('settings.html', header=header, messages=messages, manageUser=manageUser, loggedin_role=loggedin_role, user=user, settings=settings, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
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
            sql.execute("SELECT * FROM users WHERE email ='" + loggedin_email + "'")
            user = sql.fetchall()
            if user:
                if site_language == "Greek":
                    user = single_user_translate_to_Greek(manageUser, list(user[0]))
                else:
                    user = user[0]
                return render_template('settings.html', loggedin_user=loggedin_user, header=header, messages=messages, loggedin_role=loggedin_role, manageUser=manageUser, user=user, settings=settings, profilesuccess=messages.yourchanges, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users WHERE email ='" + loggedin_email + "'")
            user = sql.fetchall()
            if user:
                if site_language == "Greek":
                    user = single_user_translate_to_Greek(manageUser, list(user[0]))
                else:
                    user = user[0]
                return render_template('settings.html', loggedin_user=loggedin_user, header=header, messages=messages, loggedin_role=loggedin_role, manageUser=manageUser, user=user, settings=settings, profileerror=messages.sqlerror, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        finally:
            pass


@app.route('/menu_settings', methods=['GET', 'POST'])
def menu_settings():
    global site_language
    global site_theme
    global site_fontsize
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM users WHERE email ='" + loggedin_email + "'")
        user = sql.fetchall()
        if user:
            if site_language == "Greek":
                user = single_user_translate_to_Greek(manageUser, list(user[0]))
            else:
                user = user[0]
            return render_template('settings.html', loggedin_user=loggedin_user, header=header, messages=messages, loggedin_role=loggedin_role, manageUser=manageUser, user=user, settings=settings, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        else:
            pass
    elif request.method == 'POST':
        try:
            user_id = str(request.form["id"])
            user_theme = str(request.form["theme"])
            user_language = str(request.form["language"])
            user_fontsize = str(request.form["fontsize"])
            sql = mydb.cursor()
            query = """UPDATE users SET theme=%s, language=%s, fontsize=%s WHERE user_id=%s"""
            query_input = (user_theme, user_language, user_fontsize, user_id)
            sql.execute(query, query_input)
            mydb.commit()
            sql.close()
            sql = mydb.cursor()
            site_theme = user_theme
            site_language = user_language
            site_fontsize = user_fontsize
            checkUserSettings(site_theme, site_language, site_fontsize)
            sql.execute("SELECT * FROM users WHERE email ='" + loggedin_email + "'")
            user = sql.fetchall()
            if user:
                if site_language == "Greek":
                    user = single_user_translate_to_Greek(manageUser, list(user[0]))
                else:
                    user = user[0]
                return render_template('settings.html', loggedin_user=loggedin_user, header=header, messages=messages, loggedin_role=loggedin_role, manageUser=manageUser, user=user, settings=settings, appearancesuccess=messages.yourchanges, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users WHERE email ='" + loggedin_email + "'")
            user = sql.fetchall()
            if user:
                if site_language == "Greek":
                    user = single_user_translate_to_Greek(manageUser, list(user[0]))
                else:
                    user = user[0]
                return render_template('settings.html', loggedin_user=loggedin_user, header=header, messages=messages, loggedin_role=loggedin_role, manageUser=manageUser, user=user, settings=settings, appearanceerror=messages.sqlerror, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        finally:
            pass




@app.route('/live_feed', methods=['GET', 'POST'])
def live_feed():
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM criminals")
        result = sql.fetchall()
        if result:
            return render_template('manage_livefeed.html', loggedin_user=loggedin_user, result=result, header=header, messages=messages, manageCriminal=manageCriminal, manageLivefeed=manageLivefeed, loggedin_role=loggedin_role, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
        else:
            return render_template('manage_livefeed.html', loggedin_user=loggedin_user, error=messages.norecordsfound, header=header, messages=messages, manageCriminal=manageCriminal, manageLivefeed=manageLivefeed, loggedin_role=loggedin_role, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)




@app.route('/search_livefeed', methods=['GET', 'POST'])
def search_live_feed():
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM criminals")
        result = sql.fetchall()
        return render_template('manage_livefeed.html', loggedin_user=loggedin_user, messages=messages, result=result, header=header, message=messages, manageCriminal=manageCriminal, manageLivefeed=manageLivefeed, loggedin_role=loggedin_role, site_theme=site_theme, site_fontsize = site_fontsize, site_language=site_language)
    elif request.method == 'POST':
        global video_filter
        global global_full_name
        global last_known_location
        criminal_id = str(request.form["row.0"])
        criminal_full_name = str(request.form["row.1"])
        video_filter = str(request.form["filter"])
        criminal_full_name = criminal_full_name.replace(" ", "_")
        global_full_name = criminal_full_name
        # TODO: Check from which camera, the last updated.jpg image was found
        screenshotsPath = os.path.abspath("static/Screenshots")
        detected_image = ""
        #detected_image1 = screenshotsPath + "//" + criminal_full_name + "//Camera1-last-updated.jpg"
        #detected_image2 = screenshotsPath + "//" + criminal_full_name + "//Camera2-last-updated.jpg"
        detected_image1 = "static/Screenshots/" + criminal_full_name + "/Camera1-last-updated.jpg"
        detected_image2 = "static/Screenshots/" + criminal_full_name + "/Camera2-last-updated.jpg"
        detected_image1_mod_time = os.path.getmtime(detected_image1)
        detected_image2_mod_time = os.path.getmtime(detected_image2)
        print(detected_image1_mod_time)
        print(detected_image2_mod_time)
        if (detected_image1_mod_time < detected_image2_mod_time):
            detected_image = detected_image2
            last_known_location = camera_feed_2_location
        else:
            detected_image = detected_image1
            last_known_location = camera_feed_1_location
        detected_image = detected_image.replace("/static/static", "/")
        print(detected_image)
        cameraFeedPath1 = os.path.join(screenshotsPath, global_full_name, camera_feed_1_location)
        cameraFeedPath2 = os.path.join(screenshotsPath, global_full_name, camera_feed_2_location)
        if not os.path.exists(cameraFeedPath1):
            os.makedirs(cameraFeedPath1)
        if not os.path.exists(cameraFeedPath2):
            os.makedirs(cameraFeedPath2)
        sql = mydb.cursor()
        query = """SELECT * FROM criminals WHERE criminal_id=%s"""
        query_input = criminal_id
        sql.execute(query, query_input)
        mydb.commit()
        result = sql.fetchall()
        sql.close()
        if result:
            return render_template('search_livefeed.html', loggedin_user=loggedin_user, result=result, detected_image=detected_image, messages=messages, camera_feed_1_location=camera_feed_1_location, camera_feed_2_location=camera_feed_2_location, camera_feed_1_URL=camera_feed_1_URL, camera_feed_2_URL=camera_feed_2_URL, last_known_location=last_known_location, header=header, manageCriminal=manageCriminal, loggedin_role=loggedin_role, site_fontsize=site_fontsize, site_theme=site_theme, site_language=site_language)


def updateDatabaseImages():
    sql = mydb.cursor()
    query = """SELECT * FROM criminals """
    sql.execute(query)
    mydb.commit()
    result = sql.fetchall()
    sql.close()
    if result:
        for criminalFound in result:
            criminal_portrait_URL = criminalFound[7]
            criminal_full_name = criminalFound[1]
            criminal_full_name = criminal_full_name.replace(" ", "_")
            urllib.request.urlretrieve(criminal_portrait_URL, "static/Screenshots/" + criminal_full_name + "/database_image.jpg")
            urllib.request.urlretrieve(criminal_portrait_URL, "static/Screenshots/" + criminal_full_name + "/database_image_resized.jpg")
            detectionResizedImage = Image.open("static/Screenshots/" + criminal_full_name + "/database_image_resized.jpg")
            detectionResizedImage = detectionResizedImage.convert('RGB')
            detectionResizedImage = detectionResizedImage.resize((640, 480), Image.ANTIALIAS)
            detectionResizedImage.save("static/Screenshots/" + criminal_full_name + "/database_image_resized.jpg")

def main():
    if __name__ == '__main__':
        app.run(debug=True)

checkUserSettings(site_theme, site_language, site_fontsize)
updateDatabaseImages()
side_thread = threading.Thread(name='daemon', target=faceRecognition, args=(camera_feed_2_URL, video_filter, global_full_name))
side_thread.setDaemon(True)
side_thread.start()
main()

'''
def record_video(source):
    global global_full_name
    videosPath = os.path.abspath("static/Videos")
    saveRecordingPath = os.path.join(videosPath, global_full_name, camera_feed_1_location, "\\")
    if not os.path.exists(saveRecordingPath):
        os.makedirs(saveRecordingPath)
    FILE_OUTPUT = r'PATH_HERE'
    recordingFile = os.path.join(saveRecordingPath, 'output.avi')
    if os.path.isfile(FILE_OUTPUT):  # Checks and deletes the output file
        os.remove(FILE_OUTPUT)
    #url = "http://192.168.1.122:4747/video"
    #videoPafy = pafy.new(url)
    #best = videoPafy.getbest(preftype="webm")
    #capture = cv2.VideoCapture(1)
    capture = cv2.VideoCapture(source)
    capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'H264'))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoWriter = cv2.VideoWriter(recordingFile, fourcc, 20.0, (640, 480))
    while (True):
        ret, frame2 = capture.read()
        if ret:
            #cv2.imshow('video', frame2)
            videoWriter.write(frame2)
        if cv2.waitKey(1) == 27:
            break
    capture.release()
    videoWriter.release()
    cv2.destroyAllWindows()

def gen(camera):
    while True:
        global video_filter
        global global_full_name
        global last_known_location
        frame, last_known_location = camera.get_frame(video_filter, global_full_name)
        # Denoising phase
        #odd_symmetric_pair = [0, 1, 0, 1]
        #even_symmetric_pair = [0, 0, 1, 1]
        #real_part = 0
        #imagin_part = 0
        #real_part = np.convolve(real_part, even_symmetric_pair, mode="full")  # Equation 1 in paper
        #imagin_part = np.convolve(imagin_part, odd_symmetric_pair, mode="full")  # Equation 1 in paper
        #amplitude = distance.euclidean(real_part, imagin_part)  # Equation 2 in paper
        #phase = math.atan(imagin_part[0] / real_part[0])  # Equation 3 in paper
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/streaming')
def streaming():
    return render_template('streaming.html')
    
@app.route('/video_feed_1')
def video_feed_1():
    global site_language
    return Response(gen(VideoCamera(camera_feed_1_URL)), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_2')
def video_feed_2():
    global site_language
    return Response(gen(VideoCamera(camera_feed_2_URL)), mimetype='multipart/x-mixed-replace; boundary=frame')
'''