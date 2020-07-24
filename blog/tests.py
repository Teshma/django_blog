from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from . import views

# Create your tests here.

class CVPageTest(TestCase):
    def test_cv_url_resolves_to_cv_page_view(self):
        found = resolve("/cv")
        self.assertEqual(found.func, views.view_cv)
    
    def test_uses_cv_page_template(self):
        response = self.client.get("/cv")
        self.assertTemplateUsed(response, "blog/cv.html")

    def test_edit_cv_url_resolves_to_edit_cv_page_view(self):
        found = resolve("/cv/edit")
        self.assertEqual(found.func, views.edit_cv)