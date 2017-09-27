import unittest

from models import User, Category, Recipe


class MinimalTestUser(unittest.TestCase):
    def setUp(self):
        self._user = User("xcode", "Ibrahim Mbaziira", "code.ibra@gmail.com", "inetutils")

    def test_create_user(self):
        self.assertIsInstance(self._user, User, 'Failed to create User object')

    def test_check_user_login(self):
        self._user.increment_users_list("ibm", "ibra stacks", "decepticon@gmail.com", "123")
        self.assertEqual(self._user.check_user_login("ibm", "123"), "User credentials ok")

    def test_add_new_user(self):
        self.assertEqual(self._user.add_new_user("dan", "Daniel Sunku", "danny@gmail.com", "dannyboy"), "User Added")

    def test_edit_user(self):
        self._user.increment_users_list("dan", "Daniel Sunku", "danny@gmail.com", "dannyboy")
        self.assertEqual(self._user.edit_user("dan", "Daniel Sun", "dan@gmail.com", "dboy"), "Updated user successfully")

    def test_delete_user(self):
        self._user.increment_users_list("dan", "Daniel Sunku", "danny@gmail.com", "dannyboy")
        self.assertEqual(self._user.delete_user("dan"), "User deleted successfully")


class MinimalTestCategory(unittest.TestCase):
    def setUp(self):
        self._category = Category("Ice Tea")

    def test_create_category(self):
        self.assertIsInstance(self._category, Category, 'Failed to create category object')

    def test_add_category(self):
        self.assertEqual(self._category.add_category("Pineapple Punch"), "category added successfully")

    def test_edit_category(self):
        self._category.increment_categories_list("Pineapple Punch")
        self.assertEqual(self._category.edit_category("apple Punch", "Pineapple Punch"), "Category updated successfully")

    def test_delete_category(self):
        self._category.increment_categories_list("Fruits Salad")
        self.assertEqual(self._category.delete_category("Fruits Salad"), "category deleted")

    def test_get_category(self):
        self._category.increment_categories_list("My Category")
        self.assertEqual(self._category.get_category("My Category"), "My Category")


class MinimalTestRecipe(unittest.TestCase):
    def setUp(self):
        self._recipe = Recipe()

    def test_create_recipe(self):
        self.assertIsInstance(self._recipe, Recipe, "Failed to create recipe object")

    def test_add_recipe(self):
        self._recipe.increment_recipe_list("Fries", "Potatos", "Smashed fries", "Oil")
        self.assertEqual(self._recipe.add_recipe("Carrot spice", "spices", "minced", "sun dry"), "Recipe added")

    def test_edit_recipe(self):
        self._recipe.increment_recipe_list("Fries", "Potatos", "Smashed fries", "Oil")
        self.assertEqual(self._recipe.edit_recipe("Fries", "Potat", "Smashed All", "Olive oil"), "recipe updated")

    def test_delete_recipe(self):
        self._recipe.increment_recipe_list("Fries", "Potatos", "Smashed fries", "Oil")
        self.assertEqual(self._recipe.delete_recipe("Fries"), "recipe deleted successfully")

if __name__ == "__main__":
    unittest.main()
