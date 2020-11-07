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
from app import *

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

@app.route('/manage_criminals', methods=['GET', 'POST'])
def manage_criminals():
    global site_language
    global login_role
    if site_language == "Greek":
        manageCriminal = ManageCriminalGR()
        header = HeaderGR()
        messages = MessagesGR()
    else:
        manageCriminal = ManageCriminalEN()
        header = HeaderEN()
        messages = MessagesEN()
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM criminals")
        result = sql.fetchall()
        if result:
            if site_language == "Greek":
                result_list = list(result)
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
            return render_template('templates/manage_criminals.html', result=result, header = header, messages=messages, manageCriminal=manageCriminal, login_role=login_role)
        else:
            return render_template('templates/manage_criminals.html', error=messages.norecordfound, header=header, messages = messages, manageCriminal=manageCriminal, login_role=login_role)
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
                    result_list = list(result)
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
            return render_template('manage_criminals.html', success=messages.recordupdated, result=result, header=header, messages=messages, manageCriminal=manageCriminal, login_role=login_role)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            sql = mydb.cursor()
            sql.execute("SELECT * FROM criminals")
            result = sql.fetchall()
            if result:
                if site_language == "Greek":
                    result_list = list(result)
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
            return render_template('manage_criminals.html', error=messages.sqlerror, result=result, header=header, messages=messages, manageCriminal=manageCriminal, login_role=login_role)
        finally:
            pass



@app.route('/insert_criminals', methods=['GET', 'POST'])
def insert_criminals():
    global site_language
    global login_role
    if site_language == "Greek":
        manageCriminal = ManageCriminalGR()
        insertCriminal = InsertCriminalsGR()
        header = HeaderGR()
        messages = MessagesGR()
    else:
        manageCriminal = ManageCriminalEN()
        insertCriminal = InsertCriminalsEN()
        header = HeaderEN()
        messages = MessagesEN()
    if request.method == 'GET':
        return render_template('insert_criminals.html', messages=messages, insertCriminal=insertCriminal, manageCriminal=manageCriminal, header=header, login_role=login_role)
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
                    result_list = list(result)
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
            return render_template('manage_criminals.html', success=messages.successinsertcriminal, result=result, insertCriminal=insertCriminal, manageCriminal=manageCriminal, header=header, login_role = login_role)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            return render_template('insert_criminals.html', error=messages.sqlerror, messages=messages, insertCriminal=insertCriminal, manageCriminal=manageCriminal, header=header, login_role=login_role)
        finally:
            pass



@app.route('/remove_criminals', methods=['GET', 'POST'])
def remove_criminals():
    global site_language
    global login_role
    if site_language == "Greek":
        header = HeaderGR()
        messages = MessagesGR()
        manageCriminal = ManageCriminalGR()
    else:
        header = HeaderEN()
        messages = MessagesEN()
        manageCriminal = ManageCriminalEN()
    if request.method == 'POST':
        try:
            criminal_id = str(request.form["row.0"])
            criminal_full_name = str(request.form["row.1"])
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
                        result_list = list(result)
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
                return render_template('manage_criminals.html', success=message, result=result, header=header, manageCriminal=manageCriminal, login_role=login_role)
            else:
                message = messages.nocriminalleft + criminal_full_name + messages.nocriminalright
                sql.close()
                sql = mydb.cursor()
                sql.execute("SELECT * FROM criminals")
                result = sql.fetchall()
                if result:
                    if site_language == "Greek":
                        result_list = list(result)
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
                return render_template('manage_criminals.html', error=message, result=result, header=header, manageCriminal=manageCriminal, messages=messages, login_role=login_role)
        except MySQLdb.Error as error:
            messages.sqlerror = str(error)
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM criminals")
            result = sql.fetchall()
            if result:
                if site_language == "Greek":
                    result_list = list(result)
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
            return render_template('manage_criminals.html', error=messages.sqlerror, result=result, header=header, manageCriminal=manageCriminal, messages=messages, login_role=login_role)
        finally:
            pass