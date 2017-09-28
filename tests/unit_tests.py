import unittest
from app import app
from models import User, Category, Recipe


class MinimalTestUser(unittest.TestCase):
    def setUp(self):
        self._user = User("xcode", "Ibrahim Mbaziira", "code.ibra@gmail.com", "inetutils")

    def test_create_user(self):
        self.assertIsInstance(self._user, User, 'Failed to create User object')

    def test_check_user_login(self):
        self._user.increment_users_list("ibm", "ibra stacks", "decepticon@gmail.com", "123")
        self.assertEqual(self._user.check_user_login("ibm", "123"), "User credentials ok")

    def test_check_user_login_failed(self):
        self._user.increment_users_list("ibm", "ibra stacks", "decepticon@gmail.com", "123")
        self.assertEqual(self._user.check_user_login("x", "y"), "Wrong username or password", msg="user not in record")

    def test_add_new_user(self):
        self.assertEqual(self._user.add_new_user("dan", "Daniel Sunku", "danny@gmail.com", "dannyboy"), "User Added")

    def test_add_user_failed(self):
        self._user.add_new_user("dan", "Daniel Sunku", "danny@gmail.com", "dannyboy")
        self.assertEqual(self._user.add_new_user("dan", "Daniel Sunku", "danny@gmail.com", "dannyboy"), "User exists")

    def test_edit_user(self):
        self._user.increment_users_list("dan", "Daniel Sunku", "danny@gmail.com", "dannyboy")
        self.assertEqual(self._user.edit_user("dan", "Daniel Sun", "dan@gmail.com", "dboy"), "Updated user details")

    def test_edit_user_failed(self):
        self._user.increment_users_list("dan", "Daniel Sunku", "danny@gmail.com", "dannyboy")
        self.assertEqual(self._user.edit_user("da", "Daniel Sun", "dan@gmail.com", "dboy"), "Failed to update user")

    def test_delete_user(self):
        self._user.increment_users_list("dan", "Daniel Sunku", "danny@gmail.com", "dannyboy")
        self.assertEqual(self._user.delete_user("dan"), "User deleted successfully")

    def test_delete_user_failed(self):
        self._user.increment_users_list("dan", "Daniel Sunku", "danny@gmail.com", "dannyboy")
        self.assertEqual(self._user.delete_user("da"), "Failed to delete user", msg="User doesn't exist")


class MinimalTestCategory(unittest.TestCase):
    def setUp(self):
        self._category = Category("Ice Tea")

    def test_create_category(self):
        self.assertIsInstance(self._category, Category, 'Failed to create category object')

    def test_add_category(self):
        self.assertEqual(self._category.add_category("Pineapple Punch"), "category added successfully")

    def test_add_category_failed(self):
        self._category.increment_categories_list("Foodie Category")
        self.assertEqual(self._category.add_category("Foodie Category"), "category  exists")

    def test_edit_category(self):
        self._category.increment_categories_list("Pineapple Punch")
        self.assertEqual(self._category.edit_category("apple Punch", "Pineapple Punch"), "Category updated")

    def test_edit_category_failed(self):
        self._category.increment_categories_list("Pineapple Punch")
        self.assertEqual(self._category.edit_category("apple Punch", "Pine Punch"), "category doesn't exist")

    def test_delete_category(self):
        self._category.increment_categories_list("Fruits Salad")
        self.assertEqual(self._category.delete_category("Fruits Salad"), "category deleted")

    def test_delete_category_failed(self):
        self._category.increment_categories_list("Fruits Salad")
        self.assertEqual(self._category.delete_category("Mango"), "category does not exist", msg="Category not found")

    def test_get_category(self):
        self._category.increment_categories_list("My Category")
        self.assertEqual(self._category.get_category("My Category"), "My Category")

    def test_get_category_failed(self):
        self._category.increment_categories_list("Another One")
        self.assertEqual(self._category.get_category("XO"), "category does not exist", msg="Category not found")


class MinimalTestRecipe(unittest.TestCase):
    def setUp(self):
        self._recipe = Recipe()

    def test_create_recipe(self):
        self.assertIsInstance(self._recipe, Recipe, "Failed to create recipe object")

    def test_add_recipe(self):
        self._recipe.increment_recipe_list("Fries", "Potatos", "Smashed fries", "Oil")
        self.assertEqual(self._recipe.add_recipe("Carrot spice", "spices", "minced", "sun dry"), "Recipe added")

    def test_add_recipe_failed(self):
        self._recipe.increment_recipe_list("Fries", "Potatos", "Smashed fries", "Oil")
        self.assertEqual(self._recipe.add_recipe("Fries", "Potatos", "Smashed fries", "Oil"), "recipe already exists")

    def test_edit_recipe(self):
        self._recipe.increment_recipe_list("Fries", "Potatos", "Smashed fries", "Oil")
        self.assertEqual(self._recipe.edit_recipe("Fries", "Potat", "Smashed All", "Olive oil"), "recipe updated")

    def test_edit_recipe_failed(self):
        self._recipe.increment_recipe_list("Fries", "Potatos", "Smashed fries", "Oil")
        self.assertEqual(self._recipe.edit_recipe("Fry", "Potato", "Smashed All", "Olive oil"), "Failed recipe update")

    def test_delete_recipe(self):
        self._recipe.increment_recipe_list("Fries", "Potatos", "Smashed fries", "Oil")
        self.assertEqual(self._recipe.delete_recipe("Fries"), "recipe deleted successfully")

    def test_delete_recipe_failed(self):
        self._recipe.increment_recipe_list("Fries", "Potatos", "Smashed fries", "Oil")
        self.assertEqual(self._recipe.delete_recipe("none"), "failed to delete recipe", msg="Recipe doesn't exist")


class MinimalTestFlask(unittest.TestCase):
    # test login page, index page and dashboard
    def get_ping(self):
        ping = app.test_client(self)
        return ping

    def test_login_page(self):
        pong = self.get_ping().get('/', content_type="html/text")
        self.assertIn(b'Yummy Recipes - Login', pong.data)

    def test_index_page(self):
        pong = self.get_ping().get('/home', content_type="html/text")
        self.assertIn(b'Yummy Recipes - Home', pong.data)

    def test_dashboard_page(self):
        pong = self.get_ping().get('/dashboard', content_type="html/text")
        self.assertIn(b'Yummy Recipes - Dashboard', pong.data)


if __name__ == "__main__":
    unittest.main()
