import os
import urllib
import cv2 #pip install opencv-python
from flask import Flask, render_template, redirect, url_for, request, Response  # pip install Flask
from flask_login import current_user, LoginManager  # pip install flask-login
import MySQLdb  # pip install mysqlclient
from time import gmtime, strftime
from camera import *
import numpy as np
import time

face_cascade = cv2.CascadeClassifier("static/haarcascade/haarcascade_frontalface_alt2.xml")
ds_factor = 0.6
mydb = MySQLdb.connect(db="criminal_detection", host="localhost", user="root", passwd="")
camera_feed_1_location = "RU6 Lab"

def live_statistics(frame, pos, video_width, video_height, milliseconds):
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.5
    text_color = (0, 0, 255)  # BGR text color = White
    text1 = "Time: " + strftime("%d/%m/%Y %H:%M:%S", gmtime())
    cv2.putText(frame, text1, pos, font_face, scale, text_color, 1, cv2.LINE_AA)
    text2 = "Video Quality: " + str(video_width) + "x" + str(video_height) + " px"
    cv2.putText(frame, text2, (20, 40), font_face, scale, text_color, 1, cv2.LINE_AA)
    text3 = "Milliseconds active: " + str(milliseconds) + "msecs"
    cv2.putText(frame, text3, (20, 60), font_face, scale, text_color, 1, cv2.LINE_AA)
    text4 = "Live"
    cv2.rectangle(frame, (575, 0), (630, 20), (0, 0, 255), 0)
    cv2.circle(frame, (620, 10), 7, (0, 0, 255), -1)
    cv2.putText(frame, text4, (580, 14), font_face, scale, (0, 0, 255), 1, cv2.LINE_AA)


# Image Filters
def apply_invert(image):
    return cv2.bitwise_not(image)

def verify_alpha_channel(image):
    try:
        image.shape[3]
    except IndexError:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    return image

def apply_sepia(image, intensity=0.5):
    image = verify_alpha_channel(image)
    image_h, image_w, image_c = image.shape
    blue = 20
    green = 66
    red = 112
    sepia_bgra = (blue, green, red, 1)
    overlay = np.full((image_h, image_w, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, image, 1.0, 0, image)
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    return image

def apply_color_overlay(image, intensity=0.5, blue=0, green=0, red=0):
    image = verify_alpha_channel(image)
    image_h, image_w, image_c = image.shape
    color_bgra = (blue, green, red, 1)
    overlay = np.full((image_h, image_w, 4), color_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, image, 1.0, 0, image)
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    return image

def alpha_blend(f_1, f_2, mask):
    alpha = mask / 255.0
    image = cv2.convertScaleAbs(f_1 * (1 - alpha) + f_2 * alpha)
    return image

def apply_circle_blur(image, intensity=0.5):
    image = verify_alpha_channel(image)
    image_h, image_w, image_c = image.shape
    y = int(image_h / 2)
    x = int(image_w / 2)
    radius = int(y / 2)
    center = (x, y)
    mask = np.zeros((image_h, image_w, 4), dtype='uint8')
    cv2.circle(mask, center, radius, (255, 255, 255), -1, cv2.LINE_AA)
    mask = cv2.GaussianBlur(mask, (21, 21), 11)
    blured = cv2.GaussianBlur(image, (21, 21), 11)
    blended = alpha_blend(image, blured, 255 - mask)
    image = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
    return image

avg_time = 0.00
sum_time = 0
iterations = 0
total = 0

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self, video_filter, global_full_name):

        global iterations
        iterations = iterations + 1
        t0 = time.time()
        success, image = self.video.read()
        image = cv2.resize(image, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        invert = apply_invert(image)
        sepia = apply_sepia(image)
        redish = apply_color_overlay(image, intensity=0.5, red=230, blue=10)
        circle_blur = apply_circle_blur(image)
        face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
        path1 = r'C:\Users\Vaggelis\PycharmProjects\criminal-detection\static\Screenshots'
        path = os.path.join(path1, global_full_name, 'Camera Feed 1')
        if not os.path.exists(path):
            os.makedirs(path)
        path2 = os.path.join(path1, global_full_name)
        if not os.path.exists(path2):
            os.makedirs(path2)
        for (x, y, w, h) in face_rects:
            timestr = time.strftime("%d-%m-%Y, %H-%M-%S")
            if video_filter == "no":
                cv2.imwrite(os.path.join(path, timestr + '.jpg'), image)
                cv2.imwrite(os.path.join(path2, 'comparison.jpg'), image)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if video_filter == "gray":
                cv2.imwrite(os.path.join(path, timestr + '(GRAY).jpg'), gray)
                cv2.imwrite(os.path.join(path2, 'comparison.jpg'), gray)
                cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if video_filter == "invert":
                cv2.imwrite(os.path.join(path, timestr + '(INVERT).jpg'), invert)
                cv2.imwrite(os.path.join(path2, 'comparison.jpg'), invert)
                cv2.rectangle(invert, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if video_filter == "sepia":
                cv2.imwrite(os.path.join(path, timestr + '(SEPIA).jpg'), sepia)
                cv2.imwrite(os.path.join(path2, 'comparison.jpg'), sepia)
                cv2.rectangle(sepia, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if video_filter == "redish":
                cv2.imwrite(os.path.join(path, timestr + '(REDISH).jpg'), redish)
                cv2.imwrite(os.path.join(path2, 'comparison.jpg'), redish)
                cv2.rectangle(redish, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if video_filter == "blur":
                cv2.imwrite(os.path.join(path, timestr + '(BLUR).jpg'), circle_blur)
                cv2.imwrite(os.path.join(path2, 'comparison.jpg'), circle_blur)
                cv2.rectangle(circle_blur, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imwrite(os.path.join(path2, 'last-updated.jpg'), image)
            break
        if video_filter == "no":
            ret, jpeg = cv2.imencode('.jpg', image)
        if video_filter == "gray":
            ret, jpeg = cv2.imencode('.jpg', gray)
        if video_filter == "invert":
            ret, jpeg = cv2.imencode('.jpg', invert)
        if video_filter == "sepia":
            ret, jpeg = cv2.imencode('.jpg', sepia)
        if video_filter == "redish":
            ret, jpeg = cv2.imencode('.jpg', redish)
        if video_filter == "blur":
            ret, jpeg = cv2.imencode('.jpg', circle_blur)
        path2 = r'C:\Users\Vaggelis\PycharmProjects\criminal-detection\static\Screenshots'
        path3 = os.path.join(path2, global_full_name)
        if not os.path.exists(path3):
            os.makedirs(path3)
        path4 = os.path.join(path3, 'comparison.jpg')
        path5 = os.path.join(path3, 'database_image.jpg')
        img_bgr = cv2.imread(path4)
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(path5, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.5
        loc = np.where(res >= threshold)
        detected = "false"
        for pt in zip(*loc[::-1]):
            #cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
            detected = "true"
        if detected == "true":
            t1 = time.time()
            global avg_time
            global sum_time
            global total
            total = t1 - t0
            sum_time = sum_time + total
            avg_time = sum_time/iterations
            cv2.imwrite(os.path.join(path3, 'detected.jpg'), img_bgr)
            sql = mydb.cursor()
            query = """UPDATE criminals SET last_location= %s WHERE full_name = %s"""
            global_full_name = global_full_name.replace("_", " ")
            query_input = (camera_feed_1_location, global_full_name)
            sql.execute(query, query_input)
            mydb.commit()
            sql.close()
        return jpeg.tobytes(), total, avg_time