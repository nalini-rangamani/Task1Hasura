from src import app
from flask import Flask, request
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


# Uncomment to add a new URL at /new

# @app.route("/json")
# def json_message():
#     return jsonify(message="Hello World")
