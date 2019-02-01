##  Second, Flask

### Flask Basics

Flask is a web framework to build web applications. Easy to install and use.

To install Flask, 
``` sh
$  pip install Flask
```
We need to set up.

``` sh
$  export FLASK_APP=hello.py
```
Also, to enter the debug mode:

``` sh
$  export FLASK_ENV=development
```
And finally to run it 

``` sh
$  python3.6 hello.py 
```
This code will run flask automatically via ngrok. It will assign an unique url can be opened in a web browser.

### Flask Files

* html files: each Flask app needs html files to interact with the web browser. These files store in "templates" folder
* the app file: a file contains the source code (like hello.py)
* other files: such as classes
