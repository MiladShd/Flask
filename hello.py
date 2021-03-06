from app import app
from flask import Flask, url_for
from flask import render_template, flash, redirect
from flask_ngrok import run_with_ngrok
from config import Config
from forms import LoginForm , Test_insert
from forms import Test_form
import pandas as pd 
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


import requests
import json
from json import loads
import mysql.connector
from mysql.connector import Error

global connection

app = Flask(__name__)
login = LoginManager(app)
app.config.from_object(Config)
run_with_ngrok(app)  # Start ngrok when app is run

#db = SQLAlchemy(app)
#migrate = Migrate(app, db)


def form_ID_func(connection,form_ID):
	func_id = form_ID.ID.data
	user_string = read_ID(connection,func_id)
	userFunc_json = json.loads((user_string).iloc[0,1])
	res_tablename = (user_string).iloc[0,2]
	result = result_query(connection, userFunc_json)
	#flash('result is {}'.format(result))
	res_update(connection, res_tablename, userFunc_json["python_Query"][0], result)
	return result


def form_insert_func(connection,form2):
	test_insert_sql(connection, form2.table_form.data, form2.columns_form.data,form2.selectQuery_form.data,form2.pythonQuery_form.data, form2.resultTable_form.data)
	#flash('Juuun')
	#flash(pd.read_sql(form2.selectQuery_form.data, connection))
	#flash("""{"sql_Query":["%s"],"python_Query":["%s"]}"""%(form2.selectQuery_form.data,form2.pythonQuery_form.data))
	userFunc_json = json.loads("""{"sql_Query":["%s"],"python_Query":["%s"]}"""%(form2.selectQuery_form.data,form2.pythonQuery_form.data))
	result = result_query(connection, userFunc_json)
	res_update(connection, form2.resultTable_form.data, userFunc_json["python_Query"][0], result)
	return (result)
	
	
	
def read_ID(connection,func_id):
	funcLoc = pd.read_sql(f"select * from functions where func_id = {func_id}", connection) #Info from Table functions from the database
	return funcLoc		
	
def result_query(connection, jsonString):
	Table = pd.read_sql(jsonString["sql_Query"][0],connection)
	return str(eval(jsonString["python_Query"][0]))

	


def check_table_exists(connection, tablename):
    dbcur = connection.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False	

def create_table(connection, tablename):
	dbcur = connection.cursor()
	dbcur.execute("""
        CREATE TABLE {0} (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, u_query VARCHAR(255), result VARCHAR(255))
        """.format(tablename))
	
#print(checkTableExists(connection,'functions'))
#def user_defined_data(fucn_id,connection):


def res_update(connection, tablename, query, result):
	dbcur = connection.cursor()
	if (check_table_exists(connection, tablename) == False):
		create_table(connection, tablename)
	dbcur.execute(""" INSERT INTO {0} ( u_query, result) VALUES ('{1}','{2}');""".format(tablename, query , result))
		
	
def test_insert_sql(connection, table,column,sqlQ,pythQ,resTable):
	jsonString="""{"tables":[%s],"columns":[%s],"sql_Query":["%s"],"python_Query":["%s"]}"""%(table,column,sqlQ,pythQ)
	#flash(jsonString)
	dbcur = connection.cursor()
	dbcur.execute(""" INSERT INTO functions ( user_function, result) VALUES ('%s','%s');"""%( jsonString , resTable))


@app.route('/')
@app.route('/index')
def index():
	global connection
	try:
		connection = mysql.connector.connect(host='localhost',
								 database='----',
								 user='-----',
								 password='-------', autocommit=True)
		if connection.is_connected():
			db_Info = connection.get_server_info()
			flash("Connected to MySQL database... MySQL Server version on ",db_Info)
	
	except Error as e :
		flash("Error while connecting to MySQL", e)

#	flash(pd.read_sql("select * from functions where func_id = 3", connection))
	
	
	user = {'username': 'A1'}
	posts = [
		{
            'author': {'username': 'B1'},
            'body': 'B2'
		},
        {
            'author': {'username': 'C1'},
            'body': 'C2'
        }
    ]
	return render_template('index.html', title='Home', user=user, posts=posts)
 


@app.route('/test',methods=['GET','POST'])
def test():
	global connection
	#by ID
	form_ID = Test_form(prefix='form1')
	form2 = Test_insert(prefix='form2')
	
	#form_insert = Test_insert()
	if form_ID.validate_on_submit():
		result= form_ID_func(connection, form_ID)
		return render_template('test_succed.html', title='test_succed_past_data', ID = result)		
	elif form2.validate_on_submit():
		result = form_insert_func(connection,form2)
		return render_template('test_succed.html', title='test_succed_Insert', ID=result)
	else:
		flash('The ID is invalid')
		return render_template('test.html', title='test_failed', form1=form_ID, form2 = form2)

	


if __name__ == '__main__':
    
	app.run()
	