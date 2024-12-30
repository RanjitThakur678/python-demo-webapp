# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template("index.html", title="Hello World")

from flask import Flask, render_template

app = Flask(__name__)

# Route for the Home page
@app.route('/')
def home():
    return render_template('index.html', title="Home Page")

# Route for the Thanks page
@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == "__main__":
    app.run(debug=True)

