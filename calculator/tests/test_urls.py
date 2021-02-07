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

