from django.test import TestCase, Client


class MainTestCase(TestCase):
	def setUp(self) -> None:
		self.client = Client()

	def test_are_pages_available(self):
		self.assertEqual(
			200, self.client.get("").status_code
		)
		self.assertEqual(
			200, self.client.get("posts/").status_code
		)
		self.assertEqual(
			200, self.client.get("summary/").status_code
		)
		self.assertEqual(
			200, self.client.get("secret/").status_code
		)
		self.assertEqual(
			200, self.client.get("newpost/").status_code
		)
		self.assertEqual(
			200, self.client.get("new_code/").status_code
		)
		self.assertEqual(
			200, self.client.get("pic/").status_code
		)

