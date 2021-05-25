from flask import Flask
from flask import render_template

# Or just in one line"
from flask import Flask, render_template, request

# Because we are going to use/read/open our json file(s) "cars.json" and "cbc.json":
# First import the JSON library because we're going to be passing the data
# that's coming in as JSON.
# (module) json
import json

app = Flask(__name__)

# The route for home page is "/" => Example: # https://canadianbusinesscollege.com/


@app.route('/')  # The local link (the root): http://127.0.0.1:5000/
def home():  # or name it "main" or name it "index"

    # just declaring 3 local variables:
    module_name = "Practical Python"
    page_title = "Flask Framework Website"
    copyright = "Copyright 2021 - Practical Python Module - Canadian Business College"

    # rendering the pure index.html page without passing any data
    # return render_template('index.html')

    # Render the HTML template and passing some data (python variables)

    # First Way: to assign the values directly into each parameter:
    # We can pass these 3 variables with their values to the function render_template() after the first argument: "index.html"
    # return render_template('index.html', name="Practical Python", title="Flask Framework Website", copy="copyright 2021 - Practical Python Module - Canadian Business College")

    # Second Way:
    # > assign the values into local variables (inside this function)
    # > assign these variables into each parameter:
    return render_template('index.html', module_name=module_name, page_title=page_title, cr=copyright)

    # Using the same syntax (template): @object_name.route('the URL')


# creating more pages: about - portfolio - contact
# ================================================

@app.route('/about')  # The local link: http://127.0.0.1:5000/about
# Most of the cases the function name could be the same as the URL value we are passing to the route (not mandatory)
def about():
    page_title = "About Flask Framework"
    # create a list (array):
    skills = ["HTML and CSS", "JavaScript", "Python",
              "Flask Framework", "Django Framework", "Databases"]
    return render_template('about.html', skills=skills, page_title=page_title)


# NOTE:
# Please notice that we should remove page_title local variables from home() and about() views(functions)
# as we did a better option in base.html file (I will keep them for the learning purpose)

@app.route('/portfolio')  # The local link: http://127.0.0.1:5000/portfolio
def portfolio():
    # We will start learning about JSON in Python
    # Below is our own examples with using a list variable named "cars_data"
    # initialize and empty list (array) called "cars_data"
    cars_data = []
    # Just a review about using "with open":
    """
    with open(filename) as f:
        # My Code
    """
    # We are reading from file using python method with JSON:
    # with open ("data/file_name.json", "r") as json_data
    # first argument: data/file_name.json for our json file full path
    # second argument: r for reading (Optional)
    # we can refer to this file as "json_data" for example (yes, it could be any varaible name your prefer)
    # which is a name that we pick for the info we receive from this file
    with open('data/cars.json', 'r') as json_data:
        # for testing:
        # print(json_data) # <_io.TextIOWrapper name='data/cars.json' mode='r' encoding='cp1252'>
        # print(type(json_data)) # <class '_io.TextIOWrapper'>
        # using json object with its method named "load()"
        cars_data = json.load(json_data)
        # for testing:
        # print(cars_data)
        # [{'type': 'Honda', 'model': 2019, 'color': 'white'}, {'type': 'Fiat', 'model': 2010, 'color': 'blue'}, {'type': 'Volvo', 'model': 2012, 'color': 'red'}]

    # Below is just an extra adding for more practising
    # open(file, mode)
    # file: Your file name with the full path
    # mode: open the file for reading or writing
    # mode is an optional string that specifies the mode in which the file is opened.
    # It defaults to 'r' which means open for reading in text mode.
    # Other common values are 'w' for writing (truncating the file if it already exists),
    # 'x' for creating and writing to a new file,
    # and 'a' for appending (which on some Unix systems,
    # means that all writes append to the end of the file regardless
    # of the current seek position)
    with open('data/cbc.json') as cbc_json_data:
        cbc_data = json.load(cbc_json_data)
        # for testing:
        # print(type(cbc_data))  # <class 'list'>
        # print(cbc_data)
        # The output:
        """
        [
            {
                'campus': 'Toronto',
                'phone': '905-123-1234',
                'programs': ['FSSD', 'MDM', 'DMWD', 'SW Eng.', 'APA', 'MHA', 'DBA']
            },

            {
                'campus': 'Mississauga',
                'phone': '905-123-1222',
                'programs': ['FSSD', 'MDM', 'DMWD', 'BS', 'APA', 'PF', 'Law']
            },

            {
                'campus': 'Scarborough',
                'phone': '905-123-1235',
                'programs': ['FSSD', 'MDM', 'DMWD', 'SW Eng.', 'APA', 'Law']
            }
        ]
        """

    # Just for practice, using for loop to print the json info of "cars_data" => a list of JSON object:
    # cars_data is just a list/array:
    for car in cars_data:
        print(car)
    # output
    """
    {'type': 'Honda', 'model': 2019, 'color': 'white'}
    {'type': 'Fiat', 'model': 2010, 'color': 'blue'}
    {'type': 'Volvo', 'model': 2012, 'color': 'red'}
    """

    # We just want to display this format for our client:
    # Honda
    # 2019
    # white
    for car in cars_data:
        # 1) Print the value of the key "type"
        print(car['type'])

        # 2) Print the value of the key "model"
        print(car['model'])

        # 3) Print the value of the key "color"
        print(car['color'])
    # output:
    """
    Honda
    2019
    white
    Fiat
    2010
    blue
    Volvo
    2012
    red
    """
    # At the end we will pass the values of:
    # > cars_data into this parameter "cars"
    # > cbc_data into this parameter "cbc"
    return render_template('portfolio.html', cars=cars_data, cbc=cbc_data)


# The local link: http://127.0.0.1:5000/contact
@app.route('/contact')
def contact():
    return render_template('contact.html')


# and so on for any page
# in case if we have a page named "services.html":
# This function is just for reviewing (we don't have services.html):
@app.route('/services')  # <= The URL
def services():
    # we don't have this template:
    return render_template('services.html')


# Our basic/old campus view:
"""
@app.route("/campus")
def campus():
    return render_template("campus.html")
"""


# This function is connected with the form (view for the form):
# This page 'process.html' (html template) should be rendered after submiting the form
# Don't forget that any page we display in the browser
# has to have its URL and its function
# Note:
# By default, a route only answers to GET requests.
# In all our above example, route() methods used the "GET" request "by default"
# Example: we just wrote: @app.route('/') instead of writing: @app.route('/', methods=['GET'])
# now this one is different request, it's not a GET request, it's a POST request
# We will write (output) the user's input into this page
# You can use the "methods" argument of the route() decorator to handle different HTTP methods.
@app.route('/process', methods=["POST"])
def process():
    # get the user input
    # pass the info to our template: process.html

    # After testing the process function by adding methods=["POST"]
    # we need to make it work as a real form now:
    # creating 3 python variables to get the user input: first name, last name, email (for now) [checkboxes/radio buttons later]
    # using the "global request object" to react to the data that a client sends to the server
    # To access the form data (data transmitted in a POST or PUT request) you can use the form attribute named "name".
    # The values in between the brackets are the value for name attributes

    # flask.request
    # To access incoming request data, you can use the global request object.
    # Flask parses incoming request data for you and gives you access to it through that global object.
    # Internally Flask makes sure that you always get the correct data for the active thread if you are in a multithreaded environment.
    # Link: https://flask.palletsprojects.com/en/2.0.x/api/?highlight=request#flask.request

    # for testing:
    print(request.form)
    """
    ImmutableMultiDict(
        [
            ('first-name', 'Alex'), 
            ('last-name', 'Chow'), 
            ('email', 'alexchow@idontknowwhatsgoingon.ca'), 
            ('skills', 'HTML and CSS'), 
            ('skills', 'JavaScript'), 
            ('skills', 'Python'), 
            ('skills', 'PHP'), 
            ('subscribe', 'y')
        ])
    """

    # Let's think/assume that dictionary is like a list (array)
    # Notice that:
    # array (list) has numeric index (starting with 0) to access its values
    # dictionary has text index to access its values: key => value
    # example: we can take the value of "Alex" (the first name) by just typing request.form['first-name']
    # for testing:
    # print(request.form['first-name'])  # Alex
    # print(request.form['last-name'])  # Chow

    # The following way is based on Flask docs:
    # any_varaible = request.form['name_attr_value']
    first_name = request.form['first-name']

    # or the other way like many developers do, is by using the method get()
    # first_name = request.form.get('first-name')

    # last_name= request.form['last-name']
    # or the other way:
    last_name = request.form.get('last-name')

    email = request.form['email']
    # or the other way: email = request.form.get('email')

    # This way will not with a list of value:
    # skills = request.form['skills']
    # print (skills) # will ONLY return the first selected box: HTML and CSS

    # The solution:
    # with checkboxes we need to use form.getlist()
    skills = request.form.getlist('skills')  # for checkboxes
    # ['HTML and CSS', 'JavaScript', 'Python', 'PHP', 'C#', 'MySQL', 'SQL Server']
    print(skills)
    # or the other way: last_name = request.form.getlist('last-name')

    subscribe = request.form['subscribe']  # either "y" or "n" in small letter

    # all print() function below are just for testing:
    print(type(first_name))  # <class 'str'>
    print("first_name: ", first_name)
    # Or f string:
    print(f"last_name: {last_name}")
    print("email: ", email)
    print("skills: ", skills)  # ['JavaScript', 'Python', 'PHP', 'MySQL']

    # Using Flak/Python Validation: empty or not

    # But now let's check if any field is empty or not:
    # The "None" keyword is used to define a null value, or no value at all (similar to null in JavaScript)

    # None is not the same as 0, False, or an empty string.
    # None is a datatype of its own (NoneType) and only None can be None

    if first_name == "" or last_name == "" or email == "":
        # for testing:
        print("Field(s) is/are empty!")  # for us as developer!
        # If any required field has been left empty, we should render the same page "contact.html"
        return render_template('contact.html', empty_field=True, first_name=first_name, last_name=last_name, email=email)
    else:  # this else block will never run unless all the three fields are NOT empty
        # We only need to direct the user to the process.html page if he/she has completed filling the form
        return render_template('process.html', first_name=first_name, last_name=last_name, email=email, skills=skills, sub=subscribe)


# Our last function is to render an html template "campus.html" for every campus (Toronto, Mississauga, Scarborough)
# We want to change the route to be campus/Toronto or campus/Mississauga or campus/Scarborough
# We CANNOT just write "/campus" we need to specify the campus name also:
# the route URL value: "campus/Toroton" => to get the info for Toronto campus (object)
# the route URL value: "campus/Mississauga" => to get the info for Mississauga campus (object)
# the route URL value: "campus/Scarborough" => to get the info for Scarborough campus (object)
# It's NOT good to create a unique view for every campus!!!:
""""
@app.route("/campus/Toronto")
def campus():
    return render_template("campus.html")
@app.route("/campus/Mississauga")
def campus():
    return render_template("campus.html")
"""

# We need to pass the campus name as variable @app.route("/campus/<campus_name>")
# Using these two symbols < > with a varaible named "campus_name"

# To get the info for every individual campus, we will use the same JSON file "cbc.json"
# Based on the route URL value we retreive the info about that specific campus from the same JSON file:

# Example, If the url is "http://127.0.0.1:5000/campus/Toronto":
# - retrieve the information of Toronto campus from the JSON file
# - display them in the campus.html template page

# The URL value will be visible to the end user


@app.route("/campus/<campus_name>")
# Flask is looking for any varaible in between these < and > which is "campus_name"
# This varaible "campus_name" inside the decorator has to be passed to its function campus()
# If we don't pass it => TypeError: campus() got an unexpected keyword argument 'campus_name'
# NOTE: In Flask any argument we pass into the page function
# has to be a variable that already declared inside the route() method
# In this example: in the route() method we have a varaible named "campus_name"
# So we can pass this varaible "campus_name" to the function campus()
def campus(campus_name):
    # The logic of this function:
    # Step1: We need to retrieve the file "cbc.json":
    # We will repeat the same initial/basic steps to open the JSON file:
    with open('data/cbc.json') as cbc_json_data:
        cbc_data = json.load(cbc_json_data)
        # remember that "cbc_data" => is just a list of JSON object
        # cbc_data = contains the 3 JSON objects (Toronto campus Object, Mississauga campus object, Scarborough campus object)
        # print(cbc_data)
        # We only need one JSON object for that clicked campus

    # Step2: We need to get the information of that specific campus that the user clicked on
    # The logic:
    # Using for loop to iterate through the cbc_data
    # and check if the value of "campus_name" equal to any campus name in our cbc_data
    # we can just retrieve this specifc object

    # We'll create an empty object named "campus", which we're going to use to store our data in later.
    # Giving this object an empty value! This value will be used in case if the name doesn't exist
    campus = {}

    # looping through every object inside the list "cbc_data"
    # We need to iterate through the data array "cbc_data" that we've created.
    # Using the same for loop basic template: for any_item in items_list
    # we can refer to any item with a varaible named "obj"
    for obj in cbc_data:
        # print(obj)
        """
        {'campus': 'Toronto', 'phone': '905-123-1234',
            'programs': ['FSSD', 'MDM', 'DMWD', 'SW Eng.', 'APA', 'MHA', 'DBA']}
        {'campus': 'Mississauga', 'phone': '905-123-1222',
            'programs': ['FSSD', 'MDM', 'DMWD', 'BS', 'APA', 'PF', 'Law']}
        {'campus': 'Scarborough', 'phone': '905-123-1235',
            'programs': ['FSSD', 'MDM', 'DMWD', 'SW Eng.', 'APA', 'Law']}
        """

        """
        obj consisted of three keys:
        - campus
        - phone
        - programs

        we can access every key: obj['key_name']
        """

        # every obj will be an object that has these values: campus, phone, and programs:
        # example for one object:
        # obj=
        # [
        # {'campus': 'Toronto',
        # 'phone': '905-123-1234',
        # 'programs': ['FSSD', 'MDM', 'DMWD', 'SW Eng.', 'APA', 'MHA', 'DBA']
        # }]
        # Notice that "campus_name" could be: Toronto, Mississauga, or Scarborough
        if campus_name == obj['campus']:
            # calling our variable "campus"
            # assigning to it the entire current object for matching campus value
            campus = obj
            # for testing:
            # print("Campus Full Object Info: ", campus)

    # the function arguments: fun_argument (LHS) = variable (RHS)
    return render_template("campus.html", campus=campus)

# ******************************************************************
# MVC: Model View Controller
# Model: the data (information) we want to display (from database, JSON file, Other resource)
# View: the html pages (the templates) that we need to view to the user
# Controller: the file that monitor the app by calling/running the required view (functions)
# in this example is the current app.py file
