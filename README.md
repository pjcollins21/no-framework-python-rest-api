No Framework REST api in Python 3
Content tags: pure python rest api, python only rest api,
python rest api no flask, python rest api no framework
Author@Patrick Collins
Date: 30-Aug-2021

Tasked to create a no-framework API for an employment
opportunity. I've spent a good deal of my free time in
the last few months working in Flask, this task set me
back to ground 0. There's not a lot of documentation for
this online, a few examples of simple no-framework web 
servers, but no full blown REST api with SQL or similar.

This work is loosely based on the tutorial found here:

https://youtu.be/dgvLegLW6ek

This is spaghetti code and not very polished. It only 
includes a 'GET all records' and a 'POST'. I might 
improve this over time, but you should be able to puzzle
out other REST calls.

Tech: Python3 with modules:
    http.server, cgi, sqlite3, json
	
Feel free to use this code as a base for other work or
code challenges/projects. If you land a sweet gig, etc.
with the help of this project, I accept appreciation in
the form of currency, high-end guitars, and alcoholic 
beverages. :-P

Instructions:
1. Clone or download project
2. Install modules or initialize venv 
(I think they're built in...)
3. Run gitty_generator.py to create, initialize, and insert
   sample data into DB.
4. Run gitApp.py
5. Test GET in browser or Postman
6. Test POST in Postman or similar
