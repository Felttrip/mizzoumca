from flask import Flask
import os
from flask import Flask, abort, flash, redirect, render_template, request, url_for
import slack

app = Flask(__name__)

@app.route('/')
def landing_view():
   return render_template('landing.html')

@app.route('/home')
def home():
   messages = slack.notification_history()
   return render_template('home.html', messages=messages)


@app.route('/register')
def register():
   return render_template('register.html')


if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

