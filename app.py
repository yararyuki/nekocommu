from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/user")
def user():
    return render_template("myprofile.html")


if __name__ == "__main__":
    app.run(debug=True)
