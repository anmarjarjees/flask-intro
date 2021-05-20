from flask import Flask
from flask import render_template

# Or just in one line"
from flask import Flask, render_template

# Because we are going to use/read/open our json file(s) "cars.json" and "cbc.json":
# First import the JSON library because we're going to be passing the data
# that's coming in as JSON.
# (module) json
import json

app = Flask(__name__)


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
# ===================
@app.route('/about')  # The local link: http://127.0.0.1:5000/about
# Most of the cases the function name could be the same as the URL value we are passing to the route (not mandatory)
def about():
    page_title = "About Flask Framework"
    # create a list (array):
    skills = ["HTML and CSS", "JavaScript", "Python",
              "Flask Framework", "Django Framework", "Databases"]
    return render_template('about.html', skills=skills, page_title=page_title)


@app.route('/portfolio')  # The local link: http://127.0.0.1:5000/portfolio
def portfolio():
    # We will start learning about JSON in Python
    # Below is our own examples with using a list variable named "cars_data"
    # initialize and empty list (array) called "cars_data"
    cars_data = []
    # Just a review about using "with open":
    """
    with open(filename) as f:
        #My Code
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

    return render_template('portfolio.html', cars=cars_data, cbc=cbc_data)


@app.route('/contact')  # The local link: http://127.0.0.1:5000/contact
def contact():
    return render_template('contact.html')


# and so on for any page
# in case if we have a page named "services.html":
# This function is just for reviewing (we don't have services.html):
@app.route('/services')  # <= The URL
def services():
    # we don't have this template:
    return render_template('services.html')


@app.route("/campus")
def campus():
    return render_template("campus.html")

# ******************************************************************
# MVC: Model View Controller
# Model: the data (information) we want to display (from database, JSON file, Other resource)
# View: the html pages (the templates) that we need to view to the user
# Controller: the file that monitor the app by calling/running the required view (functions)
# in this example is the current app.py file
