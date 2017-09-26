import unittest
from app.models import User, Category, Recipe


class MinimalTestUser(unittest.TestCase):
    def set_up(self):
        self._user = User("xcode", "Ibrahim Mbaziira", "code.ibra@gmail.com", "inetutils")

    def test_create_user(self):
        self.assertIsInstance(self._user, User, 'User not created')


class MinimalTestCategory(unittest.TestCase):
    def set_up(self):
        self._category = Category("category name")

    def test_create_user(self):
        self.assertIsInstance(self._category, Category, 'Category not created')


class MinimalTestRecipe(unittest.TestCase):
    def set_up(self):
        self._recipe = Recipe("recipe name", "recipe category", "description", "ingredients")

    def test_create_user(self):
        self.assertIsInstance(self._recipe, Recipe, 'Recipe not created')
