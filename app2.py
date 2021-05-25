from flask import Flask
app = Flask(__name__)

# Part1:
# Creating a website with these 4 pages:
# The home/main page
# About us page
# Portfolio page
# Contact page

# Part2:
# we need to have a different and unique URL for every page
# for home page == always ==> ('/')
# for about us page == we can name it ==> ('/about') ==> we need to add the decorator route('/') [Already done :-)]
# for Portfolio page == we can name it  ==> ('/portfolio') ==> we need to add the decorator route('/portfolio')
# for cotact page == we can name it  ==> ('/contact') ==> we need to add the decorator route('/contact')

# Part3:
# Note to review: When we call a decorator, it must be folowed by a function to be used by this decorator
# each route() statement has to have its own function
# each function will be in charge for calling and rendering the required page template!
# for example:
# the function home(): => should render the index.html page
# and so on for the rest:
# the function about(): => should render the about.html page
# the function portfolio(): => should render the portfolio.html page


@app.route('/')  # The local link (the root): http://127.0.0.1:5000/
# creating a function that belongs to this url inside the route method: ('/'):
# since this the url to land our visitors to the home page,
# we can name our function "home()" instead of "hello_world"
# and yes you can pick any name for your functions
def home():  # or name it "main" or name it "index"
    # for testing we will make our function return a simple text or also adding HTML
    return ('<h1>Welcome to Flask Framework</h1> <h2>Hello world!</h2> <h3>Python Micro Framework</h3> <hr> <p>Here is my first try with Flask! I do like it :-) and I hope you will like it. Just be patient!</p>')

    # NOTE:
    # we don't want to just return a one message with html elements!
    # we want to return/render a full html page!
    # So later we need to route to an actual html pages
    # We will do it next


# The way to define or call any HTML page is using pure Python function:
# any_name() => it's a function (method) because it has ( and )

# and so on with any page you want to display:
# we need to specify a unique route route with a unique function
# for example, to open the about content(page)
# we can set the "URL" for route method to be '/about'


# Using the same syntax (template): @object_name.route('the URL')

# step 1: specify the route name
@app.route('/about')  # The local link: http://127.0.0.1:5000/about
# Most of the cases the function name could be the same as the URL value we are passing to the route (not mandatory)
# step 2: creating the view (function)
def about():
    return("<h1>About working with Flask Framework</h1>")


# step 1: specify the route name
@app.route('/portfolio')  # The local link: http://127.0.0.1:5000/portfolio
# step 2: creating the view (function)
def portfolio():
    return("<h1>My amazing portfolio</h1>")


# step 1: specify the route name
@app.route('/contact')  # The local link: http://127.0.0.1:5000/contact
# step 2: creating the view (function)
def contact():
    return("<h1>Contact Us</h1")


# A much better practice is to keep our HTML out of your code entirely
# by using templates, so that your code is concerned only
# with data values and not with rendering.

# Each function (which is also called a view) is controlled by its route = > # so every view has it's own route controller
