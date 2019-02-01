from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
	
	
class Test_form(FlaskForm):
	ID = IntegerField('ID')
	submit = SubmitField('submit ID')

class Test_insert(FlaskForm):
	table_form = StringField('Insert table/s: ')
	columns_form = StringField('Insert column/s: ')
	selectQuery_form = StringField('Insert select Query: ')
	pythonQuery_form = StringField('Insert Python Query: ')
	resultTable_form = StringField('Insert name of the result table: ')
	submit_insert = SubmitField('Submit these')