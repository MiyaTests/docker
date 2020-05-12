from flask import Flask, redirect, url_for, render_template, request, flash
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html", content="testing")

@app.route("/login", methods = ["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>" 

@app.route("/admin")
def adimin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug = True)
