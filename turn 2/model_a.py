import unittest
from customer_data_enrichment import enrich_data

class TestCustomerDataEnrichment(unittest.TestCase):

	def test_valid_data_enrichment(self):
		input_data = {
			"name": "John Doe",
			"email": "johndoe@example.com",
			"age": 30
		}
		expected_output = {
			"name": "John Doe",
			"email": "johndoe@example.com",
			"age": 30,
			"location": "New York",  # Dummy enrichment data
			"is_premium": False       # Dummy enrichment data
		}
		result = enrich_data(input_data)
		self.assertEqual(result, expected_output)

	def test_invalid_data_enrichment(self):
		input_data = {
			"name": "",
			"email": "invalidemail",
			"age": "thirty"
		}
		with self.assertRaises(ValueError):
			enrich_data(input_data)

	def test_missing_data_enrichment(self):
		input_data = {
			"email": "jane@example.com",
			"age": 25
		}
		expected_output = {
			"email": "jane@example.com",
			"age": 25,
			"location": None,         # Dummy enrichment data for missing value
			"is_premium": False       # Dummy enrichment data
		}
		result = enrich_data(input_data)
		self.assertEqual(result, expected_output)

	def test_boundary_data_enrichment(self):
		input_data = {
			"name": "A" * 100,
			"email": "a@" + "b" * 249 + ".com",
			"age": 0
		}
		expected_output = {
			"name": "A" * 100,
			"email": "a@" + "b" * 249 + ".com",
			"age": 0,
			"location": "Boundary City",  # Dummy enrichment data
			"is_premium": False
		}
		result = enrich_data(input_data)
		self.assertEqual(result, expected_output)

if __name__ == '__main__':
	unittest.main()
