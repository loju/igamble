from django.urls import resolve
from django.test import TestCase

from .views import IndexView


class IndexViewTest(TestCase):

    def test_url_resolves_to_index_view(self):
        index = resolve('/')
        self.assertIn(IndexView.__name__, index.view_name)
