import unittest
from business import Business

class BusinessTestCase(unittest.TestCase):

	def test_create_buiness(self):
		business = Business()
		response = business.create_business("hi","andela")
		self.assertEqual(response["message"], "Business added successfully")

	def test_cannot_create_duplicate(self):
		pass