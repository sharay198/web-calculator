import pytest
from django.test import Client
from django.urls import reverse, resolve


# Create your tests here.

class TestUrls:

    def test_index_url(self):
        path = reverse('index')
        # print(resolve(path).view_name)
        assert resolve(path).view_name == 'index'

    def test_exp_list_url(self):
        path = reverse('database')
        # print(resolve(path).view_name)
        assert resolve(path).view_name == 'database'


class TestViews:
    client = Client()
    paths = {'index': reverse('index'), 'database': reverse('database')}
    key_of_context = 'form'

    def test_key_of_context(self):

        path = self.paths['index']
        response = self.client.get(path)
        assert self.key_of_context in response.context

    def test_template_using_of_index_page(self):

        path = self.paths['index']
        response = self.client.get(path)
        # print(dir(response))
        templates = response.templates
        print()
        for i in templates:
            print(i.name)
        # print(templates[0].name)

    @pytest.mark.django_db
    def test_template_using_of_database_page(self):

        path = self.paths['database']
        response = self.client.get(path)
        # print(dir(response))
        templates = response.templates
        print()
        for i in templates:
            print(i.name)
