from flask import Flask

# Decorator Function 
# def bold_function(text):
#     def wraper_function():
#         <b>text</b>
#     return wraper_function


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<b>bye Gagnadhar</b>"


if __name__ == "__main__":
    app.run(debug=True)

