from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.test import TestCase
from django.core.urlresolvers import resolve, reverse


class TestHomePage(TestCase):

    def test_root_url_resolves_to_home_view(self):
        self.assertEqual(reverse('home'), '/')
        self.assertEqual(reverse('monitor.views.home'), '/')

    def test_home_page(self):
        request = HttpRequest()
        func, args, kwargs = resolve('/')
        response = func(request)
        self.assertIsInstance(response, HttpResponse)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>LAMA</title>', response.content)
        self.assertTrue(b'</html>')
