from flask import Flask, render_template
from mod import sum

app = Flask(__name__)
all_posts = [
    {
        'title' : 'post 1',
        'content' : 'some content for post 1',
        'author' : 'Nilesh'
    },
    {
        'title' : 'post 2',
        'content' : 'some content for post 2'
    }
]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts")
def posts():
    return render_template("posts.html", posts=all_posts)

@app.route("/home/<string:name>/<int:id>")
def hello(name, id):
    return "Hello World 3 " + name + str(sum(id, id))

if __name__ == "__main__":
    app.run(debug=True)
