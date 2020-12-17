<<<<<<< HEAD
from django.test import TestCase

# Create your tests here.

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')
    def test_get_home(self):
        self.assertEqual(200, self.response.status_code)
    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')
=======
from django.test import TestCase

# Create your tests here.


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get_home(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')
>>>>>>> 2deca4933c26dc4dacde616181fe6ac15f0aff64
