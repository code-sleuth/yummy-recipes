from flask import Flask, render_template

# create instance of flask
# change default templates folder to Designs folder
app = Flask(__name__, template_folder="Designs")


@app.route("/")
def main():
    return render_template("home.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run()

