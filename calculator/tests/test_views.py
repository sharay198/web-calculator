import pytest
from django.test import Client
from django.urls import reverse, resolve
from settings import BASE_DIR


# Create your tests here.


class TestUrls:

    def test_path_of_index_page(self):
        path = reverse('index')
        # print(resolve(path).view_name)
        assert resolve(path).view_name == 'index'

    def test_path_of_database_page(self):
        path = reverse('database')
        print(resolve(path).view_name)
        assert resolve(path).view_name == 'database'


class TestViews:
    client = Client()
    paths = {'index': reverse('index'), 'database': reverse('database')}
    key_of_context_of_index_page = 'form'
    key_of_context_of_database_page = 'exps'
    key_of_context_of_exp_detail_page = 'exp'

    def test_equlity_key_of_context_of_index_page_with_template(self):

        index_page = open(BASE_DIR + '/calculator/templates/calculator/index.html', 'r')
        assert self.key_of_context_of_index_page in index_page.read()

    def test_equlity_key_of_context_of_database_page_with_template(self):
        database_page = open(BASE_DIR + '/calculator/templates/calculator/database.html', 'r')
        assert self.key_of_context_of_database_page in database_page.read()

    def test_equlity_key_of_context_of_exp_detail_page_with_template(self):
        exp_detail_page = open(BASE_DIR + '/calculator/templates/calculator/exp_detail.html', 'r')
        assert self.key_of_context_of_exp_detail_page in exp_detail_page.read()

    def test_key_of_context_of_index_page(self):
        path = self.paths['index']
        response = self.client.get(path)
        assert self.key_of_context_of_index_page in response.context

    def test_key_of_context_of_database_page(self):
        path = self.paths['database']
        response = self.client.get(path)
        assert self.key_of_context_of_database_page in response.context

    @pytest.mark.django_db
    def test_key_of_context_of_database_page(self):
        path = self.paths['database']
        response = self.client.get(path)
        assert self.key_of_context_of_database_page in response.context

    def test_template_using_of_index_page(self):
        path = self.paths['index']
        response = self.client.get(path)
        assert 'calculator/index.html' in [template.name for template in response.templates]

    @pytest.mark.django_db
    def test_template_using_of_database_page(self):
        path = self.paths['database']
        response = self.client.get(path)
        assert 'calculator/database.html' in [template.name for template in response.templates]
