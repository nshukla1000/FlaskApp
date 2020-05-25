from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home/<string:name>/<int:id>")
def hello(name, id):
    return "Hello World 3 " + name + str(id)

if __name__ == "__main__":
    app.run(debug=True)
