from django.test import TestCase
from django.core.urlresolvers import reverse

class Test2(TestCase):
	def test_a(self):
		reverse('view1')

	def test_b(self):
		self.client.get('/view2/', HTTP_HOST='second.test.net')

	def test_c(self):
		reverse('view1')
