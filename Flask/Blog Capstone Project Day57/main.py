from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/blog")
def get_blog():
    my_data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    return render_template('index.html', blog_data=my_data.json())

@app.route("/blog/post/<num>")
def get_post(num):
    print(num)
    my_data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    return render_template('post.html', page_number=num, blog_data=my_data.json())


if __name__ == "__main__":
    app.run(debug=True)
