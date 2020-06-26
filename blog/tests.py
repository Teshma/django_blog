from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import view_cv

# Create your tests here.

class CVPageTest(TestCase):
    def test_cv_url_resolves_to_cv_page_view(self):
        found = resolve("/cv")
        self.assertEqual(found.func, view_cv)