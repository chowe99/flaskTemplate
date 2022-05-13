from flask import render_template, url_for
from app import app


@app.route('/')
@app.route('/index')
def index():

    user = {
        'username': "cod"
    }

    quotes_i_like = [
        {
            'author': {'username': "mum"},
            'text':"he means well"

        },
        {
            'author': {'username': "kawhi leonard"},
            'text': "I'm a fun guy"
        },
        {
            'author': {'username': "bette midler"},
            'text': "the worst part of success is to try to find someone who is happpy for you."
        }
    ]
    return render_template('index.html', title="cod's home page", user=user, quotes=quotes_i_like)

@app.route('/hangman')
def hangman():
    return render_template('Hangman.html')