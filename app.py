from flask import Flask, render_template, request, json, flash, url_for, redirect, session
from models import User, Category, Recipe

# create instance of flask
# change default templates folder to Designs folder
app = Flask(__name__, template_folder="Designs")
app.config['SECRET_KEY'] = 'i wont tell if you do not'


# lists to store returned user values
USERS = []
db_user_name = []
db_user_info = []

# lists to store category values
db_category_list = []
db_category_name = []
CATEGORY = []

# lists to store recipe values
RECIPES = []
db_recipes_list = []
db_one_recipe_list = []


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
                global db_user_name
                global db_user_info
                global USERS
                db_user_name = _user_obj.get_user_name()
                db_user_info = _user_obj.get_user_credentials()
                if not USERS:
                    USERS = db_user_info
                else:
                    USERS.append(db_user_info[0])

                return render_template("dashboard.html", category_info=CATEGORY, info=USERS, name=db_user_name,
                                       rec=RECIPES)
            return render_template("login.html")
    except Exception as e:
        return json.dumps({'error': str(e)})


# update user
@app.route('/update_user', methods=['GET', 'POST'])
def update_user():
    msg = ''
    _username = request.form["username"]
    _fullname = request.form["fullname"]
    _email = request.form["email"]
    _password = request.form["password"]

    _user_obj = User()
    global db_user_name
    global db_user_info
    global USERS
    db_user_name = _user_obj.get_user_name()
    db_user_info = _user_obj.get_user_credentials()
    _user_obj.set_users(USERS)

    if request.method == "POST":
        if _username and _fullname and _email and _password:
            if _user_obj.edit_user(_username, _fullname, _email, _password) == "Updated user details":
                return render_template("dashboard.html", info=db_user_info, name=db_user_name, msg='Updated details',
                                       rec=RECIPES)
            return render_template("dashboard.html", info=db_user_info, name=db_user_name, rec=RECIPES)


# add category
@app.route("/add_category", methods=['GET', 'POST'])
def add_category():
    msg = ''
    try:
        _category = request.form["category"]
        _category_obj = Category()

        if _category:
            if _category_obj.add_category(_category):
                global db_category_list
                global db_category_name
                global CATEGORY
                db_category_list = _category_obj.get_all_categories()

                if not CATEGORY:
                    CATEGORY = db_category_list
                else:
                    CATEGORY.append(db_category_list[0])

                return render_template("dashboard.html", category_list=CATEGORY, info=USERS,
                                       name=db_user_name, rec=RECIPES)
            else:
                msg = "Failed to add category"
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS,
                               name=db_user_name, rec=RECIPES)
    except Exception as ex:
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS,
                               name=db_user_name, rec=RECIPES)


# edit category
@app.route('/edit_category', methods=['GET', 'POST'])
def edit_category():
    msg = ''
    try:
        _old_name = request.form["select_item"]
        _new_name = request.form["optcategory"]
        _category_obj = Category()

        global db_category_list
        global db_category_name
        global CATEGORY
        _category_obj.set_categories(CATEGORY)

        if _old_name and _new_name:
            if _category_obj.edit_category(_new_name, _old_name):
                db = _category_obj.get_all_categories()
                CATEGORY = db
                return render_template('dashboard.html', msg=msg, category_list=CATEGORY, info=USERS, name=db_user_name,
                                       rec=RECIPES)
            else:
                msg = "Failed to edit category"
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS,
                               name=db_user_name, rec=RECIPES)

    except Exception as ex:
        return render_template("dashboard.html", msg=msg, category_list=db_category_list, info=USERS,
                               name=db_user_name, rec=RECIPES)


# delete category
@app.route('/delete_category', methods=['GET', 'POST'])
def delete_category():
    msg = ''
    _name = request.form["item"]
    _del = request.form['deletecategory']
    global CATEGORY
    _obj_cat = Category()
    _obj_cat.set_categories(CATEGORY)

    if _name and _del:
        if _obj_cat.delete_category(_name):
            db = _obj_cat.get_all_categories()
            CATEGORY = db
            return render_template('dashboard.html', msg=msg, category_list=CATEGORY, info=USERS, name=db_user_name,
                                   rec=RECIPES)
        else:
            return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS, name=db_user_name,
                                   rec=RECIPES)


# add recipe
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    msg = ''
    _recipe_name = request.form["recipename"]
    _category = request.form["category"]
    _description = request.form["description"]
    _ingredients = request.form["ingredients"]

    global RECIPES
    global db_recipes_list
    _recipe_obj = Recipe()
    db_recipes_list = _recipe_obj.get_all_recipes()

    if _recipe_name and _category and _description and _ingredients:
        if _recipe_obj.add_recipe(_recipe_name, _category, _description, _ingredients) == "Recipe added":
            if not RECIPES:
                RECIPES = db_recipes_list
            else:
                RECIPES.append(db_recipes_list[0])
            return render_template("dashboard.html", category_list=CATEGORY, info=USERS, name=db_user_name, rec=RECIPES)
        return render_template("dashboard.html", category_list=CATEGORY, info=USERS, name=db_user_name, rec=RECIPES,
                               msg='failed to add recipe')


# delete category
@app.route('/delete_recipe', methods=['GET', 'POST'])
def delete_recipe():
    msg = ''
    _name = request.form["recipe"]
    _del = request.form['deleterecipe']
    global RECIPES
    _obj_rec = Recipe()
    _obj_rec.set_recipes(RECIPES)

    if _name and _del:
        if _obj_rec.delete_recipe(_name):
            db = _obj_rec.get_all_recipes()
            RECIPES = db
            return render_template('dashboard.html', msg=msg, category_list=CATEGORY, info=USERS, name=db_user_name,
                                   rec=RECIPES)
        else:
            return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS,
                                   name=db_user_name, rec=RECIPES)


# edit recipe
@app.route('/edit_recipe', methods=['GET', 'POST'])
def edit_recipe():
    msg = ''
    try:
        _old_name = request.form["edit_recipe"]
        _new_name = request.form["recipe_name"]
        _new_category = request.form["new_category"]
        _new_description = request.form["new_description"]
        _new_ingredients = request.form["new_ingredients"]
        _rec_obj = Recipe()

        global db_recipes_list
        global db_one_recipe_list
        global RECIPES
        _rec_obj.set_recipes(RECIPES)

        if _old_name and _new_name and _new_category and _new_description and _new_ingredients:
            if _rec_obj.edit_recipe(_old_name, _new_name, _new_category, _new_description, _new_ingredients):
                db = _rec_obj.get_all_recipes()
                RECIPES = db
                return render_template('dashboard.html', msg=msg, category_list=CATEGORY, info=USERS,
                                       name=db_user_name,
                                       rec=RECIPES)
            else:
                return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS,
                                       name=db_user_name, rec=RECIPES)

    except Exception as ex:
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS,
                               name=db_user_name, rec=RECIPES)


# basic login
# username = admin
# password = pass
@app.route("/", methods=['GET', 'POST'])
def main():
    error = ""
    try:
        global USERS
        obj_user_login = User()
        obj_user_login.set_users(USERS)

        if request.method == "POST":
            _username = request.form['username']
            _password = request.form['password']
            if obj_user_login.check_user_login(_username, _password) == "User credentials ok":
                return redirect(url_for('dashboard'))
            elif _username == 'admin' and _password == 'pass':
                return redirect(url_for('dashboard'))
            else:
                error = "Invalid credentials. {Username: admin -  Password: pass} for testing"

        return render_template("login.html", error=error, category_list=CATEGORY, info=USERS, name=db_user_name,
                               rec=RECIPES)
    except Exception as e:
        flash(e)
        return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    global USERS
    return render_template("dashboard.html", category_list=CATEGORY, info=USERS, name=db_user_name, rec=RECIPES)


@app.route("/home")
def home():
    global USERS
    return render_template("home.html", category_list=CATEGORY, info=USERS, name=db_user_name, rec=RECIPES)


if __name__ == "__main__":
    app.run(debug=True)

