from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class urlForm(Form):
    url_val = StringField('url_val', validators=[DataRequired()])
