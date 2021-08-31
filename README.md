No Framework REST api in Python 3
Content tags: pure python rest api, python only rest api,
python rest api no flask, python rest api no framework
Author@Patrick Collins
Date: 30-Aug-2021

I recently created a no-framework REST api in python as 
a code challenge. I had been working in Flask, so it was
an interesting project. There's not a lot of documentation for
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

Instructions:
1. Clone or download project
2. Install modules or initialize venv 
(I think they're built in...)
3. Run gitty_generator.py to create, initialize, and insert
   sample data into DB.
4. Run gitApp.py
5. Test GET in browser or Postman
6. Test POST in Postman or similar
