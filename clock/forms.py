from flask.ext.wtf import Form
from wtforms import IntegerField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange


class AlarmForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    days = StringField('Day(s)', validators=[DataRequired()])
    hour = IntegerField('Hour', validators=[DataRequired(), NumberRange(0, 23)])
    minute = IntegerField('Minute', validators=[DataRequired(), NumberRange(0, 59)])
    action = SelectField('Action', choices=[('play_songs', 'Play Songs')])
    param = IntegerField('Num', validators=[DataRequired()])
    submit = SubmitField('Okay')
