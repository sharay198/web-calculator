import pytest
from django.core.exceptions import ValidationError
from django.test import Client
from django.urls import reverse, resolve
from settings import BASE_DIR
from calculator.views import *
from ..forms import ExpForm


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

    def test_path_of_detail_page(self):
        path = reverse('details', kwargs={'id': 5})
        print(resolve(path).view_name)
        assert resolve(path).view_name == 'details'

    def test_path_of_delete_page(self):
        path = reverse('delete', kwargs={'id': 5})
        print(resolve(path).view_name)
        assert resolve(path).view_name == 'delete'


class TestViews:
    client = Client()
    paths = {'index': reverse('index'),
             'database': reverse('database'),
             'delete': reverse('delete', kwargs={'id': 15}),
             'details': reverse('details', kwargs={'id': 15})}
    key_of_context_of_index_page = 'form'
    key_of_context_of_database_page = 'expressions'
    key_of_context_of_detail_page = 'expression'
    key_of_context_of_delete_page = 'expression'

    def test_equlity_key_of_context_of_index_page_with_template(self):
        index_page = open(BASE_DIR + '/calculator/templates/calculator/index.html', 'r')
        assert self.key_of_context_of_index_page in index_page.read()

    def test_equlity_key_of_context_of_database_page_with_template(self):
        database_page = open(BASE_DIR + '/calculator/templates/calculator/database.html', 'r')
        assert self.key_of_context_of_database_page in database_page.read()

    def test_equlity_key_of_context_of_exp_detail_page_with_template(self):
        exp_detail_page = open(BASE_DIR + '/calculator/templates/calculator/expression details.html', 'r')
        assert self.key_of_context_of_detail_page in exp_detail_page.read()

    def test_equlity_key_of_context_of_exp_delete_page_with_template(self):
        exp_delete_page = open(BASE_DIR + '/calculator/templates/calculator/delete expression.html', 'r')
        assert self.key_of_context_of_delete_page in exp_delete_page.read()

    def test_key_of_context_of_index_page(self):
        path = self.paths['index']
        response = self.client.get(path)
        assert self.key_of_context_of_index_page in response.context

    @pytest.mark.django_db
    def test_key_of_context_of_database_page(self):
        path = self.paths['database']
        response = self.client.get(path)
        print(response.context)
        assert self.key_of_context_of_database_page in response.context

    # @pytest.mark.django_db
    # def test_key_of_context_of_delete_page(self):
    #     path = self.paths['delete']
    #     response = self.client.get(path)
    #     print(path)
    #     print(response.context)
    #     assert self.key_of_context_of_delete_page in response.context
    #
    # @pytest.mark.django_db
    # def test_key_of_context_of_details_page(self):
    #     path = '/calculator/database/15/'
    #     #path = self.paths['details']
    #     print(path)
    #     response = self.client.get(path)
    #     print(response.context)
    #     assert self.key_of_context_of_detail_page in response.context

    def test_template_using_of_index_page(self):
        path = self.paths['index']
        response = self.client.get(path)
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
        assert 'calculator/expression details.html' in [template.name for template in response.templates]


class TestForm:

    def setup(self):
        data = {'expression': '10/1'}
        data_1 = {'expression': '10/0'}
        data_2 = {'expression': '(10/(1+1))+5**5-0'}
        data_3 = {'expression': '(10/1+1)+5**5-0 '}
        data_4 = {'expression': 'print()'}
        self.f = ExpForm(data)
        self.f_1 = ExpForm(data_1)
        self.f_2 = ExpForm(data_2)
        self.f_3 = ExpForm(data_3)
        self.f_4 = ExpForm(data_4)

    def test_expform(self):
        assert self.f.is_valid() == True
        assert self.f.cleaned_data['result_of_expression'] == 10
        assert self.f_1.is_valid() == False
        assert self.f_2.is_valid() == True
        assert self.f_2.cleaned_data['result_of_expression'] == 3130
        assert self.f_3.is_valid() == True
        assert self.f_3.cleaned_data['result_of_expression'] == 3136
        assert self.f_4.is_valid() == False
        with pytest.raises(ValidationError):
            self.f_1.clean()
            self.f_4.clean()
