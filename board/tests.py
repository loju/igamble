from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase

from .views import IndexView


class IndexViewTest(TestCase):

    def test_url_resolves_to_index_view(self):
        index = resolve('/')
        self.assertEqual(index.view_name, 'board:index')

    def test_index_page_returns_correct_template(self):
        request = HttpRequest()
        response = IndexView(request=request)
        self.assertIn('bonus_form', response.get_context_data().keys())
        self.assertEqual(response.template_name, 'index.html')
