from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# Create your tests here.

class SnakesTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url= reverse('home')
        actual=self.client.get(url).status_code
        expected=200
        self.assertEqual(actual,expected)
    def test_about_page_status_code(self):
        url= reverse('about')
        actual=self.client.get(url).status_code
        expected=200
        self.assertEqual(actual,expected)
    def test_home_url_template(self):
        url= reverse('home')
        actual=self.client.get(url)
        expected='home.html'
        self.assertTemplateUsed(actual, expected)
    def test_about_url_template(self):
        url= reverse('about')
        actual=self.client.get(url)
        expected='about.html'
        self.assertTemplateUsed(actual, expected)