from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the app
api = Flask(__name__)

# Define a route
@api.route('/')
def index():
    return render_template('index.html')