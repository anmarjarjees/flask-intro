from flask import Flask
from flask import render_template

# Or just in one line"
from flask import Flask, render_template

app = Flask(__name__)


# Template Rendering:
# To render a template you can use the render_template() method.
# flask.render_template(template_name_or_list, **context)
# Renders a template from the template folder with the given context.

# The link: https://flask.palletsprojects.com/en/2.0.x/quickstart/#rendering-templates

# Parameters:
# template_name_or_list (required) – the name of the template to be rendered (the HTML page name),
# or an iterable with template names the first one existing will be rendered

# context (optional) – the variables that should be available in the context of the template.
# in other words, the variables that we want to pass to our html page


@app.route('/')  # The local link (the root): http://127.0.0.1:5000/
# remember we can pick any name for our functions
# functions names are not visible to the users only the URL value of the route() method
def home():  # or name it "main" or name it "index"
    # for testing we will make our function return a simple text or also adding HTML
    # instead of just returning a message, we want to return a full html page!
    # we will return the built-in Flask function named "render_template()"
    # and this built-in function "render_template()" => will open the page that we are passing as an argument to the function
    # render_template()" => will open our page index.html
    return render_template('index.html')

    # Using the same syntax (template): @object_name.route('the URL')


# and so on with any page you want to display:
# we need to specify a unique route route with a unique function
# for example, to open the about content(page)
# we can set the "URL" for route method to be '/about'
# the full url/about => open for ur the about.html page
@app.route('/about')  # The local link: http://127.0.0.1:5000/about
# Most of the cases the function name could be the same as the URL value we are passing to the route (not mandatory)
def about():
    return render_template('about.html')


# the full url/portfolio => open for ur the portfolio.html page
@app.route('/portfolio')  # The local link: http://127.0.0.1:5000/portfolio
def portfolio():
    return render_template('portfolio.html')


@app.route('/contact')  # The local link: http://127.0.0.1:5000/contact
def contact():
    return render_template('contact.html')


# templates folder
# Flask will look for templates in the templates folder.
# So if your application is a module, this folder is next to that module,
# if it’s a package it’s actually inside your package:
"""
Case 1: a module:

/application.py
/templates
    /hello.html
"""
