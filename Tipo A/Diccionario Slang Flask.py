# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 22:43:19 2021

@author: Abraham
"""

from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()





app = Flask(__name__)


@app.route("/")
def Index():
    return "Hello World"

@app.route("/add_contact")
def add_contact():
    return "Add contact"

@app.route("/edit")
def edit_contact():
    return "Edit contact"

@app.route("/delete")
def delete_contact():
    return "Delete contact"







if __name__ == "__main__":
    app.run(port =5000,debug= True)

