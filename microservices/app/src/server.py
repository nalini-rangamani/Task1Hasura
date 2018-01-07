from src import app
from flask import Flask, request,send_file
from flask import make_response
from flask import render_template
import requests
# from flask import jsonify


@app.route("/")
def home():
    return "Hasura Hello World Nalini"

@app.route('/authors')
def proxy_example():
#for author id and number of posts
	posts = requests.get("https://jsonplaceholder.typicode.com/posts")
	posts_data=posts.json()
#get author name and other authordetails
	author = requests.get("https://jsonplaceholder.typicode.com/users")
	author_data=author.json()
	retStr=""
	Userid_old = posts_data[0]["userId"]
	Number_of_posts=0
	j=0
	for i in range(len(posts_data)):
		if posts_data[i]["userId"]==Userid_old:
			Number_of_posts = Number_of_posts + 1
		else:
			if Userid_old==author_data[j]["id"]:
#get author name
				retStr += author_data[j]["name"] + " " + str(Number_of_posts) + "<br>"
				j=j+1
			Number_of_posts=1
			Userid_old=posts_data[i]["userId"]			
	retStr +=  author_data[j]["name"] + " " + str(Number_of_posts) + "\r\n"
	return retStr

#set cookies with my name and age
@app.route('/setcookie')
def setcookie():
	resp = make_response('Setting both the cookies !!')
	resp.set_cookie('name', 'Nalini')
	resp.set_cookie('age',str(10))
	return resp 

#get cokies both name and age and display them on the browser
@app.route('/getcookies')
def getcookie():
	ret_name = request.cookies.get('name')
	ret_age = request.cookies.get('age')
	return 'Name is ' + ret_name + ' Age is ' + ret_age 
 

#render a html page
@app.route('/html')
def display_html():
	return render_template("SimpleHtml.htm")

#display an image
@app.route('/image')
def display_image():
	return send_file("SimpleImage.jpeg",mimetype='image/gif')

# Uncomment to add a new URL at /new

# @app.route("/json")
# def json_message():
#     return jsonify(message="Hello World")
