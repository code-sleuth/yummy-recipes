from flask import Flask, render_template, request, url_for, redirect
from models import User, Category, Recipe

# create instance of flask
# change default templates folder to Designs folder
app = Flask(__name__, template_folder="Designs")
app.config['SECRET_KEY'] = 'i wont tell if you do not'


# lists to store returned user values
USERS = []
db_logged_in_user = []

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
    ms=''
    _username = request.form["username"]
    _fullname = request.form["fullname"]
    _email = request.form["email"]
    _password = request.form["password"]
    _confirm = request.form["confirmpassword"]
    global USERS
    if _username and _fullname and _email and _password:
        if _password != _confirm:
            # global USERS
            ms = "Failed to add User: Password does not match"
            return render_template("login.html", category_info=CATEGORY, info=USERS,
                                   rec=RECIPES, det=db_logged_in_user, ms=ms)

        for i, user_list in enumerate(USERS):
            print(user_list[i])
            if user_list[i] == _username or user_list[2] == _email:
                ms = "Failed to add User: Username or Email address already used"
                return render_template("login.html", category_info=CATEGORY, info=USERS,
                                   rec=RECIPES, det=db_logged_in_user, ms=ms)

        if len(_password) < 4:
            ms = "Failed to add User: Password Should be at least 4 characters long"
            return render_template("login.html", category_info=CATEGORY, info=USERS,
                                   rec=RECIPES, det=db_logged_in_user, ms=ms)

        _user_obj = User()
        if _user_obj.add_new_user(_username, _fullname, _email, _password) == "User Added":
            # add this information to lists

            db_user_info = _user_obj.get_users()

            if not USERS:
                USERS = db_user_info
            else:
                USERS.append(db_user_info[0])

            return render_template("login.html", category_info=CATEGORY, info=USERS,
                                   rec=RECIPES, det=db_logged_in_user,
                                   ms='User added SUCCESSFULLY. Now Use Your credentials to login')
        return render_template("login.html", category_info=CATEGORY, info=USERS,
                               rec=RECIPES, det=db_logged_in_user, ms='failed to add user')
    return url_for('main')


# update user
@app.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if request.method == "POST":
        msg = ''
        _username = request.form["username"]
        _fullname = request.form["fullname"]
        _email = request.form["email"]
        _password = request.form["password"]

        _user_obj = User()
        global USERS
        _user_obj.set_users(USERS)

        if request.method == "POST":
            if _username and _fullname and _email and _password:
                if _user_obj.edit_user(_username, _fullname, _email, _password) == "Updated user details":
                    return render_template("dashboard.html", msg='Updated details', rec=RECIPES, det=db_logged_in_user)
                return render_template("dashboard.html", rec=RECIPES, det=db_logged_in_user)
    else:
        msg = "Login"
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS, rec=RECIPES,
                               det=db_logged_in_user)


# add category
@app.route("/add_category", methods=['GET', 'POST'])
def add_category():
    if request.method == "POST":
        msg = ''
        _category = request.form["category"]
        _category_obj = Category()
        global db_category_list
        global db_category_name
        global CATEGORY

        if _category in CATEGORY:
            cms = 'Category already exists. use different name'
            return render_template('dashboard.html', cms=cms, category_list=CATEGORY, info=USERS, rec=RECIPES,
                                   det=db_logged_in_user)

        if _category:
            if _category_obj.add_category(_category):
                db_category_list = _category_obj.get_all_categories()
                if not CATEGORY:
                    CATEGORY = db_category_list
                else:
                    CATEGORY.append(db_category_list[0])

                return render_template("dashboard.html", category_list=CATEGORY, info=USERS, rec=RECIPES,
                                       det=db_logged_in_user)
            else:
                msg = "Failed to add category"
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS,
                               rec=RECIPES, det=db_logged_in_user)
    else:
        msg = "Login"
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS, rec=RECIPES,
                               det=db_logged_in_user)


# edit category
@app.route('/edit_category', methods=['GET', 'POST'])
def edit_category():
    if request.method == "POST":
        msg = ''
        _old_name = request.form["select_item"]
        _new_name = request.form["optcategory"]
        _category_obj = Category()

        global db_category_list
        global db_category_name
        global CATEGORY
        _category_obj.set_categories(CATEGORY)

        if _new_name in CATEGORY:
            cme = 'Category already exists. use different name'
            return render_template('dashboard.html', cme=cme, category_list=CATEGORY, info=USERS, rec=RECIPES,
                                   det=db_logged_in_user)

        if _old_name and _new_name:
            if _category_obj.edit_category(_new_name, _old_name):
                db = _category_obj.get_all_categories()
                CATEGORY = db
                return render_template('dashboard.html', msg=msg, category_list=CATEGORY, info=USERS, rec=RECIPES,
                                       det=db_logged_in_user)
            else:
                msg = "Failed to edit category"
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS, rec=RECIPES,
                               det=db_logged_in_user)
    else:
        msg = "Login"
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS, rec=RECIPES,
                               det=db_logged_in_user)


# delete category
@app.route('/delete_category', methods=['GET', 'POST'])
def delete_category():
    if request.method == "POST":
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
                return render_template('dashboard.html', msg=msg, category_list=CATEGORY, info=USERS, rec=RECIPES,
                                       det=db_logged_in_user)
            else:
                return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS,
                                       rec=RECIPES, det=db_logged_in_user)
    else:
        msg = "Login"
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS, rec=RECIPES,
                               det=db_logged_in_user)


# add recipe
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == "POST":
        msg = ''
        _recipe_name = request.form["recipename"]
        _category = request.form["category"]
        _description = request.form["description"]
        _ingredients = request.form["ingredients"]
        _username = db_logged_in_user[0]

        global RECIPES
        global db_recipes_list
        _recipe_obj = Recipe()
        db_recipes_list = _recipe_obj.get_all_recipes()

        if _recipe_name and _category and _description and _ingredients:
            if _recipe_obj.add_recipe(_recipe_name, _category, _description, _ingredients, _username) == "Recipe added":
                if not RECIPES:
                    RECIPES = db_recipes_list
                else:
                    RECIPES.append(db_recipes_list[0])
                return render_template("dashboard.html", category_list=CATEGORY, info=USERS, rec=RECIPES,
                                       det=db_logged_in_user)
            return render_template("dashboard.html", category_list=CATEGORY, info=USERS, rec=RECIPES,
                                   msg='failed to add recipe', det=db_logged_in_user)
    else:
        msg = "Login"
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS, rec=RECIPES,
                               det=db_logged_in_user)


# delete category
@app.route('/delete_recipe', methods=['GET', 'POST'])
def delete_recipe():
    if request.method == "POST":
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
                                       rec=RECIPES, det=db_logged_in_user)
            else:
                return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS, rec=RECIPES,
                                       det=db_logged_in_user)
    else:
        msg = "Login"
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS, rec=RECIPES,
                               det=db_logged_in_user)


# edit recipe
@app.route('/edit_recipe', methods=['GET', 'POST'])
def edit_recipe():
    if request.method == "POST":
        msg = ''
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
                                       rec=RECIPES, det=db_logged_in_user)
            else:
                return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS, rec=RECIPES,
                                       det=db_logged_in_user)
    else:
        msg="Login"
        return render_template("dashboard.html", msg=msg, category_list=CATEGORY, info=USERS, rec=RECIPES,
                               det=db_logged_in_user)


# basic login
# username = admin
# password = pass
@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        ms = ""
        global USERS
        global db_logged_in_user
        obj_user_login = User()
        obj_user_login.set_users(USERS)

        if request.method == "POST":
            _username = request.form['username']
            _password = request.form['password']
            if obj_user_login.check_user_login(_username, _password) == "User credentials ok":
                db_logged_in_user = obj_user_login.get_logged_in_user(_username)
                return redirect(url_for('dashboard'))
            else:
                ms = "Invalid credentials."

        return render_template("login.html", ms=ms, category_list=CATEGORY, info=USERS, rec=RECIPES,
                               det=db_logged_in_user)
    else:
        ms="Login"
        db_logged_in_user = []
        return render_template("login.html", ms=ms, category_list=CATEGORY, info=USERS, rec=RECIPES,
                               det=db_logged_in_user)


@app.route("/dashboard")
def dashboard():
    global USERS
    return render_template("dashboard.html", category_list=CATEGORY, info=USERS, rec=RECIPES, det=db_logged_in_user)


@app.route("/home")
def home():
    global USERS
    return render_template("home.html", category_list=CATEGORY, info=USERS, rec=RECIPES, det=db_logged_in_user)


if __name__ == "__main__":
    app.run(debug=True)

