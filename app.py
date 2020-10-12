import os
import urllib
import cv2  # pip install opencv-python
from flask import Flask, render_template, redirect, url_for, request, Response  # pip install Flask
from flask_login import current_user, LoginManager  # pip install flask-login
import MySQLdb  # pip install mysqlclient
from time import gmtime, strftime
import time
import numpy as np
import datetime
import urllib.request
from camera import *
from scipy.spatial import distance
import math
from EnglishLanguage import *
from GreekLanguage import *

# create the application object and connect to db
app = Flask(__name__)
mydb = MySQLdb.connect(db="criminal_detection", host="localhost", user="root", passwd="")
video_filter = ""
global_full_name = ""
detection_time = 0.0
average_detection_time = 0.0
camera_feed_1_location = "RU6 Lab"
site_language = "Greek"


def nothing(x):
    pass


''' ==============GN/EN Ready [100%]=============='''
@app.route('/')
def start():
    global site_language
    if site_language == "Greek":
        welcome = WelcomeGR()
    else:
        welcome = WelcomeEN()
    return render_template('welcome.html', welcome=welcome)


''' ==============GN/EN Ready [100%]=============='''
@app.route('/welcome')
def welcome():
    global site_language
    if site_language == "Greek":
        welcome = WelcomeGR()
    else:
        welcome = WelcomeEN()
    return render_template('welcome.html', welcome=welcome)


@app.route('/home')
def home():
    global site_language
    return render_template('home.html')


''' ==============GN/EN Ready [100%]=============='''
@app.route('/manage')
def manage():
    global site_language
    if site_language == "Greek":
        header = HeaderGR()
        manage = ManageGR()
        messages = MessagesGR()
    else:
        header = HeaderEN()
        manage = ManageEN()
        messages = MessagesEN()
    return render_template('manage.html', header=header, manage=manage, messages=messages)


''' ==============GN/EN Ready [100%]=============='''
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    global site_language
    if site_language == "Greek":
        header = HeaderGR()
        contact = ContactGR()
        messages = MessagesGR()
    else:
        header = HeaderEN()
        contact = ContactEN()
        messages = MessagesEN()
    if request.method == 'GET':
        return render_template('contact.html', header=header, contact=contact)
    elif request.method == 'POST':
        try:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            subject = request.form['subject']
            sql = mydb.cursor()
            sql.execute("INSERT INTO contact (first_name, last_name, email, subject) VALUES (%s,%s,%s,%s)",
                        (firstname, lastname, email, subject))
            mydb.commit()
            sql.close()
            message = "You have successfully submitted your contact form!"
            return render_template('contact.html', success=message, header=header, contact=contact)
        except MySQLdb.Error as error:
            message = str(error)
            return render_template('contact.html', error=message, header=header, contact=contact)
        finally:
            pass


''' ==============GN/EN Ready [100%]=============='''
@app.route('/login', methods=['GET', 'POST'])
def login():
    global site_language
    if site_language == "Greek":
        login = LoginGR()
    else:
        login = LoginEN()
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sql = mydb.cursor()
        sql.execute("SELECT username FROM users WHERE username ='" + username + "' AND password = +'" + password + "'")
        user = sql.fetchone()
        if user:
            if len(user) is 1:
                return render_template('home.html')
        else:
            error = 'Invalid Credentials! Please try again.'
    return render_template('login.html', error=error, login=login)


''' ==============GN/EN Ready [100%]=============='''
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    global site_language
    if site_language == "Greek":
        signup = SignupGR()
    else:
        signup = SignupEN()
    if request.method == 'GET':
        return render_template('signup.html', signup=signup)
    elif request.method == 'POST':
        try:
            username = str(request.form["username"])
            password = str(request.form["password"])
            email = str(request.form["email"])
            fullname = str(request.form["full_name"])
            role = str(request.form["role"])
            avatar = str(request.form["avatar"])
            sql = mydb.cursor()
            sql.execute(
                "INSERT INTO users (username, password, email, full_name, role, avatar) VALUES(%s,%s,%s,%s,%s,%s)",
                (username, password, email, fullname, role, avatar))
            mydb.commit()
            sql.close()
            success = 'User ' + username + "successfully added to the database"
            return render_template('contact.html', success=success, signup=signup)
        except MySQLdb.Error as error:
            message = str(error)
            return render_template('contact.html', error=message, signup=signup)
        finally:
            pass


''' ==============GN/EN Ready [100%]=============='''
@app.route('/insert_criminals', methods=['GET', 'POST'])
def insert_criminals():
    global site_language
    if site_language == "Greek":
        insertCriminal = InsertCriminalsGR()
        header = HeaderGR()
        messages = MessagesGR()
    else:
        insertCriminal = InsertCriminalsEN()
        header = HeaderEN()
        messages = MessagesEN()
    if request.method == 'GET':
        return render_template('insert_criminals.html', messages = messages, insertCriminal = insertCriminal, header = header)
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
            sql = mydb.cursor()
            sql.execute(
                "INSERT INTO criminals (full_name, age, height, weight, eye_color, biography, portrait, last_location) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (criminal_full_name, criminal_age, criminal_height, criminal_weight, criminal_eye_color,
                 criminal_biography, criminal_portrait, criminal_last_location))
            mydb.commit()
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM criminals")
            result = sql.fetchall()
            message = criminal_full_name + " successfully added to the database!"
            return render_template('manage_criminals.html', success=message, result=result, messages = messages, insertCriminal = insertCriminal, header = header)
        except MySQLdb.Error as error:
            message = str(error)
            return render_template('insert_criminals.html', error=message, messages = messages, insertCriminal = insertCriminal, header = header)
        finally:
            pass

''' ==============GN/EN Ready [100%]=============='''
@app.route('/insert_users', methods=['GET', 'POST'])
def insert_users():
    global site_language
    if site_language == "Greek":
        insertUser= InsertUserGR()
        header = HeaderGR()
        messages = MessagesGR()
    else:
        insertUser = InsertUserEN()
        header = HeaderEN()
        messages = MessagesEN()
    if request.method == 'GET':
        return render_template('insert_users.html', header = header, messages = messages, insertUser = insertUser)
    elif request.method == 'POST':
        try:
            username = str(request.form["username"])
            password = str(request.form["password"])
            email = str(request.form["email"])
            full_name = str(request.form["full_name"])
            role = str(request.form["role"])
            avatar = str(request.form["avatar"])
            sql = mydb.cursor()
            sql.execute(
                "INSERT INTO users (username, password, email, full_name, role, avatar) VALUES (%s,%s,%s,%s,%s,%s)",
                (username, password, email, full_name, role, avatar))
            mydb.commit()
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM criminals")
            result = sql.fetchall()
            message = username + " successfully added from the database!"
            return render_template('manage_users.html', success=message, result=result,  header = header, messages = messages, insertUser = insertUser)
        except MySQLdb.Error as error:
            message = str(error)
            return render_template('insert_users.html', error=message,  header = header, messages = messages, insertUser = insertUser)
        finally:
            pass


@app.route('/remove_criminals', methods=['GET', 'POST'])
def remove_criminals():
    global site_language
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
                message = criminal_full_name + " successfully deleted from the database!"
                sql.close()
                sql = mydb.cursor()
                sql.execute("SELECT * FROM criminals")
                result = sql.fetchall()
                return render_template('manage_criminals.html', success=message, result=result)
            else:
                message = "No criminal named " + criminal_full_name + " exists in the database!"
                sql.close()
                sql = mydb.cursor()
                sql.execute("SELECT * FROM criminals")
                result = sql.fetchall()
                return render_template('manage_criminals.html', error=message, result=result)
        except MySQLdb.Error as error:
            message = str(error)
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM criminals")
            result = sql.fetchall()
            return render_template('manage_criminals.html', error=message, result=result)
        finally:
            pass


@app.route('/remove_users', methods=['GET', 'POST'])
def remove_users():
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
                message = user_username + " successfully deleted from the database!"
                sql.close()
                sql = mydb.cursor()
                sql.execute("SELECT * FROM users")
                result = sql.fetchall()
                return render_template('manage_users.html', success=message, result=result)
            else:
                message = "No username " + user_username + " exists in the database!"
                sql.close()
                sql = mydb.cursor()
                sql.execute("SELECT * FROM users")
                result = sql.fetchall()
                return render_template('manage_users.html', error=message, result=result)
        except MySQLdb.Error as error:
            message = str(error)
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users")
            result = sql.fetchall()
            return render_template('manage_users.html', error=message, result=result)
        finally:
            pass

''' ==============GN/EN Ready [100%]=============='''
@app.route('/manage_criminals', methods=['GET', 'POST'])
def manage_criminals():
    global site_language
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
            return render_template('manage_criminals.html', result=result, header = header, messages = messages, manageCriminal = manageCriminal)
        else:
            error = 'No records found in the database!'
            return render_template('manage_criminals.html', error=error, header = header, messages = messages, manageCriminal = manageCriminal)
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
            sql = mydb.cursor()
            query = """UPDATE criminals SET full_name= %s, age=%s, height=%s, weight=%s, eye_color=%s, biography=%s, portrait=%s, last_location=%s WHERE criminal_id = %s"""
            query_input = (
            criminal_full_name, criminal_age, criminal_height, criminal_weight, criminal_eye_color, criminal_bio,
            criminal_portrait, criminal_last_location, criminal_id)
            sql.execute(query, query_input)
            mydb.commit()
            message = "Record successfully updated in the database!"
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM criminals")
            result = sql.fetchall()
            return render_template('manage_criminals.html', success=message, result=result, header = header, messages = messages, manageCriminal = manageCriminal)
        except MySQLdb.Error as error:
            message = str(error)
            sql = mydb.cursor()
            sql.execute("SELECT * FROM criminals")
            result = sql.fetchall()
            return render_template('manage_criminals.html', error=message, result=result, header = header, messages = messages, manageCriminal = manageCriminal)
        finally:
            pass

''' ==============GN/EN Ready [100%]=============='''
@app.route('/manage_users', methods=['GET', 'POST'])
def manage_users():
    global site_language
    if site_language == "Greek":
        manageUser = ManageUserGR()
        header = HeaderGR()
        messages = MessagesGR()
    else:
        manageUser = ManageUserEN()
        header = HeaderEN()
        messages = MessagesEN()
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM users")
        result = sql.fetchall()
        if result:
            return render_template('manage_users.html', result=result, header = header, messages = messages, manageUser = manageUser)
        else:
            error = 'No records found in the database!'
            return render_template('manage_users.html', error=error, header = header, messages = messages, manageUser = manageUser)
    elif request.method == 'POST':
        try:
            user_id = str(request.form["id"])
            user_username = str(request.form["username"])
            user_password = str(request.form["password"])
            user_email = str(request.form["email"])
            user_fullname = str(request.form["full_name"])
            user_role = str(request.form["role"])
            user_avatar = str(request.form["avatar"])
            sql = mydb.cursor()
            query = """UPDATE users SET username=%s, password=%s, email=%s, full_name=%s, role=%s, avatar=%s WHERE user_id=%s"""
            query_input = (user_username, user_password, user_email, user_fullname, user_role, user_avatar, user_id)
            sql.execute(query, query_input)
            mydb.commit()
            message = "Record successfully updated in the database!"
            sql.close()
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users")
            result = sql.fetchall()
            return render_template('manage_users.html', success=message, result=result, header = header, messages = messages, manageUser = manageUser)
        except MySQLdb.Error as error:
            message = str(error)
            sql = mydb.cursor()
            sql.execute("SELECT * FROM users")
            result = sql.fetchall()
            return render_template('manage_users.html', error=message, result=result, header = header, messages = messages, manageUser = manageUser)
        finally:
            pass

''' ==============GN/EN Ready [100%]=============='''
@app.route('/live_feed', methods=['GET', 'POST'])
def live_feed():
    global site_language
    if site_language == "Greek":
        manageCriminal = ManageCriminalGR()
        header = HeaderGR()
        messages = MessagesGR()
        manageLivefeed = ManageLivefeedGR()
    else:
        manageCriminal = ManageCriminalEN()
        header = HeaderEN()
        messages = MessagesEN()
        manageLivefeed = ManageLivefeedEN()
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM criminals")
        result = sql.fetchall()
        if result:
            return render_template('manage_livefeed.html', result=result, header = header, messages = messages, manageCriminal = manageCriminal, manageLivefeed = manageLivefeed)
        else:
            error = 'No records found in the database!'
            return render_template('manage_livefeed.html', error=error, header = header, messages = messages, manageCriminal = manageCriminal, manageLivefeed = manageLivefeed)


@app.route('/search_livefeed', methods=['GET', 'POST'])
def search_live_feed():
    global site_language
    global video_filter
    global global_full_name
    if request.method == 'GET':
        sql = mydb.cursor()
        sql.execute("SELECT * FROM criminals")
        result = sql.fetchall()
        return render_template('manage_livefeed.html', result=result)
    elif request.method == 'POST':
        global detection_time
        global average_detection_time
        global camera_feed_1_location
        detection_time = round(detection_time, 4)
        average_detection_time = round(average_detection_time, 4)
        print("Detection time: " + str(detection_time) + " seconds")
        print("Average Detection time: " + str(average_detection_time) + " seconds")
        criminal_id = str(request.form["row.0"])
        criminal_full_name = str(request.form["row.1"])
        criminal_portrait_URL = str(request.form["row.7"])
        video_filter = str(request.form["filter"])
        criminal_full_name = criminal_full_name.replace(" ", "_")
        global_full_name = criminal_full_name
        criminal_folder_path = "/Screenshots/" + criminal_full_name + "/detected.jpg"
        path1 = r'C:\Users\Vaggelis\PycharmProjects\criminal-detection\static\Screenshots'
        path = os.path.join(path1, global_full_name, "Camera Feed 1")
        if not os.path.exists(criminal_folder_path):
            localtime = "Face not yet detected"
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            modification_time = os.path.getmtime(path)
            localtime = datetime.datetime.fromtimestamp(modification_time)
        urllib.request.urlretrieve(criminal_portrait_URL,
                                   "static/Screenshots/" + criminal_full_name + "/database_image.jpg")
        sql = mydb.cursor()
        query = """SELECT * FROM criminals WHERE criminal_id=%s"""
        query_input = criminal_id
        sql.execute(query, query_input)
        mydb.commit()
        result = sql.fetchall()
        sql.close()
        if result:
            return render_template('search_livefeed.html', result=result, criminal_folder_path=criminal_folder_path,
                                   localtime=localtime, camera_feed_1_location=camera_feed_1_location)


def gen(camera):
    global site_language
    global global_full_name
    while True:
        global average_detection_time
        global detection_time
        frame, detection_time, average_detection_time = camera.get_frame(video_filter, global_full_name)
        # Denoising phase
        odd_symmetric_pair = [0, 1, 0, 1]
        even_symmetric_pair = [0, 0, 1, 1]
        real_part = 0
        imagin_part = 0
        real_part = np.convolve(real_part, even_symmetric_pair, mode="full")  # Equation 1 in paper
        imagin_part = np.convolve(imagin_part, odd_symmetric_pair, mode="full")  # Equation 1 in paper
        amplitude = distance.euclidean(real_part, imagin_part)  # Equation 2 in paper
        phase = math.atan(imagin_part[0] / real_part[0])  # Equation 3 in paper
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def record_video():
    global site_language
    path1 = r'C:\Users\Vaggelis\PycharmProjects\criminal-detection\static\Videos'
    path = os.path.join(path1, global_full_name, "Camera Feed 1/")
    if not os.path.exists(path):
        os.makedirs(path)
    FILE_OUTPUT = r'C:\Users\Vaggelis\PycharmProjects\criminal-detection\static\Videos\output1.avi'
    if os.path.isfile(FILE_OUTPUT):  # Checks and deletes the output file
        os.remove(FILE_OUTPUT)
    capture = cv2.VideoCapture(0)  # Capturing video from webcam:
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoWriter = cv2.VideoWriter(FILE_OUTPUT, fourcc, 20.0, (640, 480))
    while (True):
        ret, frame2 = capture.read()
        if ret:
            cv2.imshow('video', frame2)
            videoWriter.write(frame2)
        if cv2.waitKey(1) == 27:
            break
    capture.release()
    videoWriter.release()
    cv2.destroyAllWindows()


@app.route('/video_feed')
def video_feed():
    global site_language
    record_video()
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)