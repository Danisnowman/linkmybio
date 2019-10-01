#FLASK
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
import os,optparse
import yaml

environment=os.getenv("ENVIRONMENT", "development")

with open("links.yaml", 'r') as stream:
    try:
        links = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

@app.route("/")
def home():
    return render_template("home.html", links=links)


if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)