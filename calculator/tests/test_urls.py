from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve


class TestUrls:

    def test_path_of_index_page(self):
        path = reverse('index')
        # print(resolve(path).view_name)
        assert resolve(path).view_name == 'index'

    def test_path_of_database_page(self):
        path = reverse('database')
        print(resolve(path).view_name)
        assert resolve(path).view_name == 'database'

    def test_path_of_detail_page(self):
        path = reverse('details', kwargs={'id': 5})
        print(resolve(path).view_name)
        assert resolve(path).view_name == 'details'

    def test_path_of_delete_page(self):
        path = reverse('delete', kwargs={'id': 5})
        print(resolve(path).view_name)
        assert resolve(path).view_name == 'delete'
