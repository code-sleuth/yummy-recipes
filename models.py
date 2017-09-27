# Defined classes User, Category and Recipe
class User:
    def __init__(self, username, fullname, email, password):
        self._username = username
        self._fullname = fullname
        self._email = email
        self._password = password
        self._users = []
        self._users_list = []

    def check_user_login(self, username, password):
        self._username = username
        self._password = password

        for index1, item in enumerate(self._users):
            for index2, item2 in enumerate(item):
                if self._users[index1][index2] == self._username and self._users[index1][3] == self._password:
                    return "User credentials ok"
                return "Wrong username or password"

    def add_new_user(self, username, fullname, email, password):
        self._username = username
        self._fullname = fullname
        self._email = email
        self._password = password
        self._users_list = [self._username, self._fullname, self._email, self._password]

        # get existing username and passwords into lists
        get_username_index_in_lists = [username[0] for username in self._users]
        get_email_index_in_lists = [email[2] for email in self._users]

        if self._username not in get_username_index_in_lists and self._email not in get_email_index_in_lists:
            self._users.append(self._users_list)
            return "User Added"
        return "email or username already exists"

    # user cannot edit username
    # they can however edit the full name, password and email
    def edit_user(self, username, new_fullname, new_email, new_password):
        self._username = username
        self._fullname = new_fullname
        self._email = new_email
        self._password = new_password

        for index1, item in enumerate(self._users):
            for index2, item2 in enumerate(item):
                if self._users[index1][index2] == self._username:
                    self._users[index1][1] = self._fullname
                    self._users[index1][2] = self._email
                    self._users[index1][3] = self._password
                    return "Updated user successfully"
                return "Failed to update user"

    def delete_user(self, username):
        self._username = username

        for index1, item in enumerate(self._users):
            for index2, item2 in enumerate(item):
                if self._users[index1][index2] == self._username:
                    self._users.pop(index1)
                    return "User deleted successfully"
                return "Failed to delete user"

    # this is important when testing login, edits, deletes
    def increment_users_list(self, username, new_fullname, new_email, new_password):
        self._username = username
        self._fullname = new_fullname
        self._email = new_email
        self._password = new_password
        self._users_list = [self._username, self._fullname, self._email, self._password]
        self._users.append(self._users_list)
        return self._users


class Category:

    def __init__(self, name):
        self._name = name
        self._old_name = ""
        self._categories = []

    def add_category(self, category):
        self._name = category
        if self._name not in self._categories:
            self._categories.append(self._name)
            return "category added successfully"
        return "category  exists"

    def edit_category(self, new_name, old_name):
        self._old_name = old_name
        self._name = new_name
        if self._old_name in self._categories:
            self._categories = [self._name for self._old_name in self._categories]
            return "Category updated successfully"
        return "select category to edit"

    def delete_category(self, category):
        self._name = category
        if self._name in self._categories:
            self._categories.remove(self._name)
            return "category deleted"
        return "category does not exist"

    def get_category(self, category):
        self._name = category
        for self._name in self._categories:
            return self._name
        return "category does not exist"

    # this is important for testing edits, deletes
    def increment_categories_list(self, category):
        self._name = category
        self._categories.append(self._name)
        return self._categories


class Recipe:

    def __init__(self, name="", category="", details="", ingredients=""):
        self._recipe = name
        self._category = category
        self._details = details
        self._ingredients = ingredients
        self._recipe_list = []
        self._recipes = []

    def add_recipe(self, name, category, details, ingredients):
        self._recipe = name
        self._category = category
        self._details = details
        self._ingredients = ingredients

        # get existing recipe names
        get_recipe_name = [name[0] for name in self._recipes]
        self._recipe_list = [self._recipe, self._category, self._details, self._ingredients]

        if self._recipe not in get_recipe_name:
            self._recipes.append(self._recipe_list)
            return "Recipe added"
        return "recipe already exists"

    def edit_recipe(self, name, category, details, ingredients):
        self._recipe = name
        self._category = category
        self._details = details
        self._ingredients = ingredients
        old_recipe_name = name

        for index1, item in enumerate(self._recipes):
            for index2, item2 in enumerate(item):
                if self._recipes[index1][index2] == old_recipe_name:
                    self._recipes[index1][0] = self._recipe
                    self._recipes[index1][1] = self._category
                    self._recipes[index1][2] = self._details
                    self._recipes[index1][3] = self._ingredients
                    return "recipe updated"
                return "Failed to update recipe"

    def delete_recipe(self, name):
        self._recipe = name

        for index1, item in enumerate(self._recipes):
            for index2, item2 in enumerate(item):
                if self._recipes[index1][index2] == self._recipe:
                    self._recipes.pop(index1)
                    return "recipe deleted successfully"
                return "failed to delete recipe"

    # this is important when testing  edits, deletes
    def increment_recipe_list(self, name, category, details, ingredients):
        self._recipe = name
        self._category = category
        self._details = details
        self._ingredients = ingredients
        self._recipe_list = [self._recipe, self._category, self._details, self._ingredients]
        self._recipes.append(self._recipe_list)
        return self._recipes