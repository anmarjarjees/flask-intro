# the main link: https://flask.palletsprojects.com/en/2.0.x/quickstart/
# Notice that this main file is created in the main project folder
# name it app.py by default also

# Example from Flask Docs:
"""
A Minimal Application
A minimal Flask application looks something like this:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
"""

# Here is a broad overview of some of the most common operations.

# First of all you have to import it from the flask module:
# let's import Flask class
from flask import Flask
# If flask is NOT installed: ModuleNotFoundError: No module named 'flask'

# Creating our application variable with the name "app" by convention which an instance of Flask class:
# Below app is just a name for our object that refers to our current application
# and yes it could be any name you choose (it has no connection with this file name app.py)
# As we have done before: member1 = Member("Alex","1970")
app = Flask(__name__)


# setting a route to direct the app to the home page of our website (will be the index page later)
# We then use the route() decorator to tell Flask what URL should trigger our function.
# inside the route decorator we need to define the path to get into this function:
# so leave it for / for loading the home page
# The home page address for any website (example): domain-name.com/
# # We used just "/" to refer to the home page:
# Home page has "/" at the end : https://canadianbusinesscollege.com/
@app.route('/')
# creating a function that belongs to this url inside the route method: ('/'):
# since this the url to land our visitors to the home page,
# we can name our function "home()" instead of "hello_world"
# and yes you can pick any name for your functions
def hello_world():
    # return 'Hello, World! Finally it works'
    # for testing we will make our function return a simple text or also adding HTML
    return ('<h1>Welcome to Flask Framework</h1> <h2>Hello world!</h2> <h3>Python Micro Framework</h3> <hr> <p>Here is my first try with Flask! I do like it :-) and I hope you will like it. Just be patient!</p>')

    # we don't want to just return a one message with html elements
