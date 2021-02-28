import pytest
from django.test import Client
from settings import BASE_DIR
from calculator.views import *


@pytest.mark.parametrize('template_name, key_of_context',
                         (('index', 'form'),
                          ('database', 'expressions'),
                          ('expression_details', 'expression'),
                          ('delete_expression', 'expression')))
def test_check_path_to_template(template_name, key_of_context):
    path_to_template = BASE_DIR + f'/calculator/templates/calculator/{template_name}.html'
    content_of_template = open(path_to_template, 'r')
    assert key_of_context in content_of_template.read()


class TestViews:
    client = Client()
    paths = {'index': reverse('index'),
             'database': reverse('database'),
             'delete': reverse('delete', kwargs={'id': 15}),
             'details': reverse('details', kwargs={'id': 15})}

    @pytest.mark.django_db
    def test_key_of_context_of_database_page(self):
        path = self.paths['database']
        response = self.client.get(path)
        print(response.context)
        assert self.key_of_context_of_database_page in response.context

    @pytest.mark.django_db
    def test_key_of_context_of_delete_page(self):
        path = self.paths['delete']
        response = self.client.get(path)
        assert self.key_of_context_of_delete_page in response.context

    @pytest.mark.django_db
    def test_key_of_context_of_details_page(self):
        path = self.paths['details']
        response = self.client.get(path)
        assert self.key_of_context_of_detail_page in response.context

    def test_template_using_of_index_page(self):
        path = self.paths['index']
        response = self.client.get(path)
        for template in response.templates:
            print(template.name)
        assert 'calculator/index.html' in [template.name for template in response.templates]

    @pytest.mark.django_db
    def test_template_using_of_database_page(self):
        path = self.paths['database']
        response = self.client.get(path)
        assert 'calculator/database.html' in [template.name for template in response.templates]

    @pytest.mark.django_db
    def test_template_using_of_details_page(self):
        path = self.paths['details']
        response = self.client.get(path)
        # print(response.templates)
        for template in response.templates:
            print(template.name)
        # assert 'calculator/expression_details.html' in [template.name for template in response.templates]
