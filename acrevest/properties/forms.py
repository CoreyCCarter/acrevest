# posts/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DecimalField, IntegerField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
	size = DecimalField('Size(in acres)', validators=[DataRequired()])
	city = StringField('City', validators=[DataRequired()])
	county = StringField('County')
	state = StringField('State') 
	postal_code =  IntegerField('Postal Code')
	country = StringField('Country', validators=[DataRequired()])
	description = TextAreaField('Property Description', validators=[DataRequired()])
	submit = SubmitField('List Property')

