from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import re
from datetime import datetime
import mysql.connector
from mysql.connector import FieldType
import connect

app = Flask(__name__)

dbconn = None
connection = None

def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(user=connect.dbuser, \
    password=connect.dbpass, host=connect.dbhost, \
    database=connect.dbname, autocommit=True)
    dbconn = connection.cursor()
    return dbconn

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/blog")
def bloglists():
    connection = getCursor()
    connection.execute("SELECT * FROM posts;")
    bloglist = connection.fetchall()
    print(bloglist)
    return render_template("blog.html", blogList = bloglist) 


def get_post(post_id):
    


@app.route("post/<int:post_id>")
def post(post_id):
    post = ""
    return render_template('post.html', post = post)



