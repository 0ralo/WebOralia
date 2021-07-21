from django.test import TestCase


class MainTestCase(TestCase):
	def setUp(self) -> None:
		self.value = 10
		return 100

	def test_is_value_ten(self):
		self.assertEqual(10, self.value)

	def test_is_value_eleven(self):
		self.assertEqual(11, self.value)
