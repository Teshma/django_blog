from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from . import views
from .models import CV
from .forms import CVForm

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

    ##TODO
    def test_can_create_new_cv(self):
        form = CVForm(data={"title": "my cv"})
        if form.is_valid():
            new_cv = form.save(commit=False)
            new_cv.save()
        else:
            self.assertEqual(form.errors, 0)
        self.assertEqual(CV.objects.count(), 1)
    
    """ def test_add_cv_section_on_edit_cv_page(self):
        response = self.client.get("/cv/edit", d ata = {"section_text": "test"})

        self.assertEqual(CVSection.objects.count(), 1)
        cv_section = CVSection.objects.first()
        self.assertEqual(cv_section.text, "test") """