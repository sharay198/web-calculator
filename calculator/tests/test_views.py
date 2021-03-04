import pytest
from django.test import Client
from web_calculator.settings import BASE_DIR
from calculator.views import *
import os


def get_templates_name():
    path_to_templates = BASE_DIR + f'/calculator/templates/calculator/'
    list_of_templates = os.listdir(path_to_templates)
    list_of_templates.pop(2)  # remove base.html
    return list_of_templates  # ['expression_details.html', 'delete_expression.html', 'database.html', 'index.html']


@pytest.fixture(params=['expression_details.html', 'delete_expression.html', 'database.html', 'index.html'])
def template_name(request):
    template = request.param
    content_of_template = open(template, 'r')
    return content_of_template


# @pytest.fixture(params=[('details', '5'), ('delete', '5'), ('database', ''), ('index', '')])
@pytest.fixture(params=[reverse('index'),
                        reverse('database'),
                        reverse('details', kwargs={'id': 5}),
                        reverse('delete', kwargs={'id': 15})])
def path(request):
    return request.param


def test_view_name(path):
    print(path)


# @pytest.fixture()
# def url_of_the_page(view_name):
#     if view_name == 'details' or view_name == 'delete':
#         path = reverse(view_name, kwargs={'id': 5})
#     else:
#         path = reverse(view_name)
#     return path


@pytest.fixture()
def key_of_context(path):
    # list_of_context = []
    # urls_name = ['details', 'delete', 'database', 'index']
    client = Client()
    # for url in request.params:
    response = client.get(path)
    key_of_context = response.context
    # list_of_context.append(context)
    return key_of_context


@pytest.mark.django_db
def test_key_of_context(key_of_context):
    print(key_of_context)


# @pytest.mark.parametrize('get_templates_name', 'key_of_context', ('get_templates_name', 'key_of_context'))
# @pytest.mark.parametrize('key_of_context', 'key_of_context')
@pytest.mark.django_db
def test_equality_key_of_context_using_in_template_with_key_using_in_views(key_of_context, template_name):
    # path_to_template = BASE_DIR + f'/calculator/templates/calculator/{template_name}.html'
    # assert
    # for template in get_templates_name():
    # content_of_template = open(template_name, 'r')
    #print(key_of_context, template_name)
    assert key_of_context in template_name


# @pytest.mark.parametrize('template_name, key_of_context',
#                          (('index', 'form'),
#                           ('database', 'expressions'),
#                           ('expression_details', 'expression'),
#                           ('delete_expression', 'expression')))
# def test_equality_key_of_context_using_in_template_with_key_using_in_views(template_name, key_of_context):
#     path_to_template = BASE_DIR + f'/calculator/templates/calculator/{template_name}.html'
#     content_of_template = open(path_to_template, 'r')
#     assert key_of_context in content_of_template.read()


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
        assert 'expressions' in response.context

    @pytest.mark.django_db
    def test_key_of_context_of_delete_page(self):
        path = reverse('delete', kwargs={'id': 5})
        print(path)
        response = self.client.get('/calculator/database/5/delete/')
        exp = Exp.expressions.get(id=5)
        print(exp)
        # assert 'expression' in response.context

    # @pytest.mark.django_db
    # def test_key_of_context_of_details_page(self):
    #     path = self.paths['details']
    #     response = self.client.get(path)
    #     assert self.key_of_context_of_detail_page in response.context

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
