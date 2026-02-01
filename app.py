# app.py
from flask import (Flask, render_template, request, redirect, url_for, flash, session)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# -------------------------------------------------
# RUN APP
# -------------------------------------------------
if __name__ == "__main__":
    # debug=True reloads the app when you change the code (useful during development)
    app.run(debug=True)