from django.urls import reverse, resolve
import pytest


@pytest.mark.parametrize('view_name, id', [('index', ''), ('database', ''), ('details', '5'), ('delete', '5')])
def test_path_of_page(view_name, id):
    global path
    if not id:
        path = reverse(view_name)
    if id:
        path = reverse(view_name, kwargs={'id': id})
    assert resolve(path).view_name == view_name


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
