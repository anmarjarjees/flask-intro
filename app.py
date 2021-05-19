from flask import Flask
from flask import render_template

# Or just in one line"
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # The local link (the root): http://127.0.0.1:5000/
def home():  # or name it "main" or name it "index"

    # just declaring 3 local variables:
    module_name = "Practical Python"
    page_title = "Flask Framework Website"
    copyright = "copyright 2021 - Practical Python Module - Canadian Business College"

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
    return render_template('portfolio.html')


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
