"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, request
from SkolWebApp import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/search.html')
def search():
    return app.send_static_file('../search.html')

@app.route('/process_search', methods=['POST'])
def process_search():
    user_input = request.form['query']  # Get the value of the 'query' input field
    result = process_query(user_input)  # Call the Python function
    return f"You entered: {user_input}. Results: {result}"

def process_query(query):
    # Example processing function
    return f"Processed: {query}"

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
