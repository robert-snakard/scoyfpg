from flask import render_template, flash, redirect
from app import app
from .forms import urlForm, emptyForm

i = 0

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/<int:i>', methods=['GET', 'POST'])
def video(i):
    form = urlForm()
    if form.validate_on_submit():
        return render_template('video.html',
                               title='Playlist {}'.format(i),
                               url_data=form.url_val.data,
                               form=form)
    return render_template('video.html',
                           title='Playlist {}'.format(i),
                           form=form)
