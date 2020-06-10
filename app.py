from flask import Flask, render_template, request, redirect
import mod as m
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), nullable=False)
   content = db.Column(db.Text, nullable=False)
   author = db.Column(db.String(20), nullable=False, default='N/A')
   date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

   def __repr__(self):
      return 'Blog post ' + str(self.id) + str(self.date_posted)

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

@app.route("/forms" , methods=['GET', 'POST'])
def sums():
    post_num1 = 0
    post_num2 = 0
    if request.method == "POST":
        post_num1 = float(request.form["num1"])
        post_num2 = float(request.form["num2"])
        return render_template("forms.html", sum=m.sum(post_num1,post_num2))
        # return redirect('/forms', sum=post_num1 + post_num2)
    else:
        return render_template("forms.html", sum=post_num1 + post_num2)

@app.route("/posts", methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template("posts.html", posts=all_posts)

@app.route("/home/<string:name>/<int:id>")
def hello(name, id):
    return "Hello World 3 " + name + str(sum(id, id))

if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    app.run(debug=True)



