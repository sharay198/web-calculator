from django.core.exceptions import ValidationError
from ..forms import ExpForm
import pytest


@pytest.mark.parametrize('param', [{'expression': '1/1'}, {'expression': '(5+5)*(10-5)/5'}, {'expression': '1-1'},
                                   {'expression': '1*1-1'}, {'expression': '10**100+(-1)'}, {'expression': '1/0'},
                                   {'expression': 'asasd asda'}, {'expression': 'a-b'},
                                   {'expression': '()'}, {'expression': '[]'}, {'expression': '{}'},
                                   {'expression': '//'},
                                   {'expression': 'print()'}, {'expression': 'print("world)'}])
def test_form(param):
    f = ExpForm({'expression': param})
    if f.is_valid():
        assert f.clean() == f.cleaned_data
    else:
        with pytest.raises(ValidationError):
            f.clean()
