from flask import Flask, render_template, request, json, flash, url_for, redirect, session
from models import User, Category, Recipe

# create instance of flask
# change default templates folder to Designs folder
app = Flask(__name__, template_folder="Designs")
app.config['SECRET_KEY'] = 'super secret key'

# lists to store returned user values
db_user_info = []
db_users_all = []
db_user_name = []

# lists to store category values
db_category_list = []
db_category_name = []


# when a user registers successfully, they are redirected to the dashboard
# user details can be found when you click user details on the dashboard menu
@app.route('/add_user', methods=['GET', 'POST'])
def signup():
    try:
        _username = request.form["username"]
        _fullname = request.form["fullname"]
        _email = request.form["email"]
        _password = request.form["password"]

        if _username and _fullname and _email and _password:
            _user_obj = User(_username, _fullname, _email, _password)
            if _user_obj.add_new_user(_username, _fullname, _email, _password) == "User Added":
                # add this information to lists
                db_user_name = _user_obj.get_user_name()
                db_user_info = _user_obj.get_user_credentials()

                return render_template("dashboard.html", info=db_user_info, name=db_user_name)
            return render_template("login.html")
    except Exception as e:
        return json.dumps({'error': str(e)})


# update user
@app.route('/update_user', methods=['GET', 'POST'])
def update_user():
    try:
        _username = request.form["username"]
        _fullname = request.form["fullname"]
        _email = request.form["email"]
        _password = request.form["password"]

        if _username and _fullname and _email and _password:
            _user_obj = User()
            if _user_obj.edit_user(_username, _fullname, _email, _password) == "Updated user details":
                db_user_name = _user_obj.get_user_name()
                db_user_info = _user_obj.get_user_credentials()
                return render_template("dashboard.html", info=db_user_info, name=db_user_name)
            return render_template("login.html")
    except Exception as e:
        return json.dumps({'error': str(e)})


# add category
@app.route("/add_category", methods=['GET', 'POST'])
def add_category():
    msg = ''
    try:
        _category = request.form["category"]

        if _category:
            _category_obj = Category(_category)
            if _category_obj.add_category(_category):
                db_category_list = _category_obj.get_all_categories()
                return render_template("dashboard.html", category_list=db_category_list, info=db_user_info,
                                       name=db_user_name)
            else:
                msg = "Failed to add category"
        return render_template("dashboard.html", msg=msg, category_list=db_category_list, info=db_user_info,
                               name=db_user_name)
    except Exception as ex:
        return render_template("dashboard.html", msg=msg, category_list=db_category_list, info=db_user_info,
                               name=db_user_name)


# edit category
@app.route('/edit_category', methods=['GET', 'POST'])
def edit_category():
    msg = ''
    try:
        _new_name = request.form["opt"]
        _new_name = str(_new_name)
        _category = request.form["category"]
        if _category:
            _category_obj = Category("")
            if _category_obj.edit_category(_new_name, _category):
                # db_category_list = _category_obj.get_all_categories()
                return render_template("dashboard.html", msg=msg, category_list=db_category_list, info=db_user_info,
                                       name=db_user_name)
            else:
                msg = "Failed to edit category"
        return render_template("dashboard.html", msg=msg, category_list=db_category_list, info=db_user_info,
                               name=db_user_name)

    except Exception as ex:
        return render_template("dashboard.html", msg=msg, category_list=db_category_list, info=db_user_info,
                               name=db_user_name)


# basic login
# username = admin
# password = pass
@app.route("/", methods=['GET', 'POST'])
def main():
    error = ""
    try:
        if request.method == "POST":
            _username = request.form['username']
            _password = request.form['password']

            if _username == 'admin' and _password == 'pass':
                return redirect(url_for('dashboard'))
            else:
                error = "Invalid credentials. Username: admin -  Password: pass for testing"

        return render_template("login.html", error=error)
    except Exception as e:
        flash(e)
        return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", category_list=db_category_list, info=db_user_info, name=db_user_name)


@app.route("/home")
def home():
    return render_template("home.html", category_list=db_category_list, info=db_user_info, name=db_user_name)


if __name__ == "__main__":
    app.run(debug=True)

