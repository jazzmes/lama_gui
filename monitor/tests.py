from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from django.template.loader import render_to_string


class TestHomePage(TestCase):

    def test_root_url_resolves_to_home_view(self):
        self.assertEqual(reverse('home'), '/')
        self.assertEqual(reverse('monitor.views.home'), '/')

    def test_home_page(self):
        request = HttpRequest()
        func, args, kwargs = resolve('/')
        response = func(request)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.content.decode(), render_to_string('home.html'))

