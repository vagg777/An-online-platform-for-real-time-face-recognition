# An online platform for real time face recognition

## 1. Introduction
Undoubtedly, face recognition does have a very large variety of services and applications, beginning from human identification and surveillance and coming as far as e marketing and advertising for customers. The ability to efficiently recognize individuals through a combination of their facial characteristics (e g their eyes) is certainly an important phenomenon. So, the goal of recognizing peers through their faces is something already apparent on our everyday lives.

In our days, face recognition is more and more utilized in order to search and identify shoplifters, retail criminals, or people with a history of frauds or crimes. This means that their pictures can, after being processed, be matched against a large criminal database. As a result, this can prevent and reduce crime rates by identifying criminals from installed cameras.

## 2. The idea
All existing face recognition approaches can be used, extended and efficiently deployed for a wide variety of application in our everyday lives, ranging from outdoor face recognition for crime detection up to indoor object recognition and pattern matching. This is an extension of the existing facial identification approaches by proposing an online platform/website that can be used from the police forces.

This approach builds upon existing work and suggests not an algorithm, but a complete systemic approach through a crime detection platform to be used in police headquarter/precincts. The platform considers the Haar Cascade algorithm for the facial recognition detection and extends it by performing real-time recognition from the connected cameras in the system.

The platform supports two different types of users:
* Police employees in the headquarters/precincts
* Police Administrators, with a higher level of access and also responsible for database maintenance

The main features of the platform include:
* inserting, editing and deleting user and criminal information
* applying 6 different filters in the livestream cameras (no, gray, sepia, redish, blur, inverted)
* searching for criminals based on their picture through a livestream camera feed and identify them

As for the criminal identification, it is made possible through image pattern recognition between the provided criminal’s image and snapshots of identified faces from the livestream feed.

![enter image description here](https://i.ibb.co/zNCp9Rb/Picture14.png)

Image 1: The live feed facial recognition approach

The Live Feed section offers six different options for video filters, enabling the user to select the best filter, depending on the relevant situation of the physical surroundings (e.g. broad light, dark environment).

## 3. Tools needed

* Project Version : `Final`
* IDE Version : `InteliJ Pycharm 2019.3.3 Community Version`
* Programming Language : `Python`
* Web framework: `Flask`
* Python Version : `3.6.0`
* SQL Version : `MySQL RDBMS (XAMPP)`
* CSS Version : `Boostrap 4.0.0`


## 4. Building the database (MySQL)

The database of the platform consists of 3 different tables, the `users` table, the `criminals` table and the `contact` table.

![enter image description here](https://i.ibb.co/YW1ttbx/1.png)

Image 2: The Database Schema

## 5. The online platform

![enter image description here](https://i.ibb.co/m5xSXyX/2.png)

Image 3: The welcoming page

![enter image description here](https://i.ibb.co/vJxPJys/3.png)

Image 4: The Login page

![enter image description here](https://i.ibb.co/4SJ525K/4.png)

Image 5: The Signup page

![enter image description here](https://i.ibb.co/s3HMnXV/5.png)

Image 6: The Home page

![enter image description here](https://i.ibb.co/Js5nqHj/6.png)

Image 7: The Management page

![enter image description here](https://i.ibb.co/ZVdxywZ/7.png)

Image 8: The Management page for the criminals (same idea for users)

![enter image description here](https://i.ibb.co/R4BjbHQ/8.png )

Image 9: Inserting a new criminal (same idea for users)

![enter image description here](https://i.ibb.co/pfm8gtm/9.png)

Image 10: Updating an existing user (same idea for criminals)

![enter image description here](https://i.ibb.co/W5J53Tn/10.png)

Image 11: Deleting an existing user (same idea for criminals)

![enter image description here](https://i.ibb.co/DKG1Vkp/11.png)

Image 12: Report an issue to the system administrators

![enter image description here](https://i.ibb.co/W3zVv0C/12.png)

Image 13: Selecting a criminal to search in live feed and the video filter

![enter image description here](https://i.ibb.co/bLX2YLw/13.png)

Image 14: The livestream page, including the last known location and all live feeds

![enter image description here](https://i.ibb.co/4JbN3Lg/14.png)

Image 15: Error Handling

![enter image description here](https://i.ibb.co/F8Lssp0/15.png)

Image 16: Error Handling

![enter image description here](https://i.ibb.co/ChPx27b/16.png)

Image 17: My Profile section

![enter image description here](https://i.ibb.co/X46zC01/17.png)

Image 18: My Settings section

![enter image description here](https://i.ibb.co/KsDpLQS/19.png)

Image 19: Changing the settings to Dark theme, 12 font size and Greek Language

![enter image description here](https://i.ibb.co/w48KVrn/18.png)

Image 20: Changing the settings to Dark theme, 12 font size and Greek Language

![enter image description here](https://i.ibb.co/Xsjb3g9/20.png)

Image 21: Mobile responsiveness 

![enter image description here](https://i.ibb.co/f9Ssz1F/Capture.png)

Image 22: The 6 different face recognition filters

![enter image description here](https://i.ibb.co/BLYgFmY/Picture13.png)

Image 23: Screenshots are saved inside a folder with the criminal's name, the datetime and the filter type are appended in the filename

# 6. Deploying the platform

The steps to deploy the website should be the following:

1. Creating the database
You may login in any MySQL database management panel and create a new database. You may use the `criminal_detection` name for your database. Make sure you select the UTF-8 encoding (collation `utf8_general_ci`). Both `app.py` and `camera.py` files include the following line for a connection to the MySQL database:
`mydb = MySQLdb.connect(db="criminal_detection", host="localhost", user="root", passwd="")`
You may update this according to your localhost setup and credentials.
2. Populating the database
Select your database (e.g. the `criminal_detection`) and import the `criminal_detection.sql` file, which includes the creation of the tables and the data population
3. Running the `app.py` file
This is the main file which includes the necessary app routings towards the HTML pages, alongside with the relevant data processing. The `camera.py` file is only called in the livestream page.
4. That's it! You have successfully deployed the website...
