from flask import Flask
from flask import render_template

# Or just in one line"
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # The local link (the root): http://127.0.0.1:5000/
def home():  # or name it "main" or name it "index"
    # module_name = "Practical Python"
    page_title = "Flask Framework Website"
    copyright = "copyright 2021 - Practical Python Module - Canadian Business College"
    # return render_template('index.html')

    # We can pass these 3 variables with their values to the function render_template() after the first argument: "index.html"
    return render_template('index.html', name="Practical Python", title="Flask Framework Website", copy="copyright 2021 - Practical Python Module - Canadian Business College")

    # Or we can use this statement:

    # Using the same syntax (template): @object_name.route('the URL')


@app.route('/about')  # The local link: http://127.0.0.1:5000/about
# Most of the cases the function name could be the same as the URL value we are passing to the route (not mandatory)
def about():
    return render_template('about.html')


@app.route('/portfolio')  # The local link: http://127.0.0.1:5000/portfolio
def portfolio():
    return render_template('portfolio.html')


@app.route('/contact')  # The local link: http://127.0.0.1:5000/contact
def contact():
    return render_template('contact.html')
