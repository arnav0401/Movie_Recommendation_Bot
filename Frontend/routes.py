from movie import app
from flask import render_template, redirect, url_for, flash

@app.route('/')
def home_page():
        return render_template('home.html')