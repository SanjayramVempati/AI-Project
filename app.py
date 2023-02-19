from flask import Flask, render_template, url_for, flash, redirect, request, app
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
from forms import LoginForm


from flask import Flask

app = Flask(__name__)

DB_NAME = "ai.db"


@app.route('/index')
def index():
  return render_template('index.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/login2', methods=['GET','POST'])
def login2():
  return render_template('login2.html')

@app.route('/about')
def about():
  return render_template('about.html', title='About')

@app.route('/learn')
def learn():
  return render_template('learn.html', title='Learn')

@app.route('/ourteam')
def ourteam():
  return render_template('ourteam.html', title='Our Team')

@app.route('/quiz')
def quiz():
  return render_template('quiz.html', title="Test")