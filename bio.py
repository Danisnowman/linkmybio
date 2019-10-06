#FLASK
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
from social_media import *
import os, optparse, yaml

environment=os.getenv("ENVIRONMENT", "development")

social_media_list = []

with open("links.yaml", 'r') as stream:
    try:
        links = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
link_list = links.get("links")

for i in range(len(link_list)):
    # print(link_list[i].get(i+1).get("name"))
    name = link_list[i].get(i+1).get("name")
    enable = link_list[i].get(i+1).get("enable")
    link = link_list[i].get(i+1).get("link")
    description = link_list[i].get(i+1).get("description")

    social_media = SocialMedia(name, enable, link, description)
    social_media_list.append(social_media)




@app.route("/")
def home():
    return render_template("home.html",  social_media_list=social_media_list, links=links)


if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    link_list = links.get("links")


    app.run(host="0.0.0.0",debug=debug)