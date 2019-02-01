#  Third, Python Code

## Connect to a database:
Following code is used to connect to a mysql connector. Substitute the database name,  user and password to connect to your database.
* Autocommit: if it is False, every sql query should be commit after execution. 
```
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

```

## Forms

### ID Form:
this form just get an ID and find the queries in a table named `function` and execute it. In the end it update the specified table with query and result.

### Insert Forms
These forms first ask the user input the SQL and Python Queries and the table s/he wants to update. Convert the data to `json`, Insert in `functions` table and then run the queries and update the destination table.   

### The functions
```
@app.route('/index')
def index():
#...
```
This line will find the index.html file in the templates and render it.

