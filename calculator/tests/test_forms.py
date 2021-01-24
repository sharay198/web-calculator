from django.core.exceptions import ValidationError
from ..forms import ExpForm
import pytest


# Create your tests here.
class TestForm:

    def setup(self):
        data = {'expression': '10/1'}
        data_1 = {'expression': '10/0'}
        data_2 = {'expression': '(10/(1+1))+5**5-0'}
        data_3 = {'expression': '(10/1+1)+5**5-0 '}
        data_4 = {'expression': 'print()'}
        data_5 = {'expression': '()'}
        data_6 = {'expression': '1//1'}
        data_7 = {'expression': 'asdasda sdfsdf'}
        self.f = ExpForm(data)
        self.f_1 = ExpForm(data_1)
        self.f_2 = ExpForm(data_2)
        self.f_3 = ExpForm(data_3)
        self.f_4 = ExpForm(data_4)
        self.f_5 = ExpForm(data_5)
        self.f_6 = ExpForm(data_6)
        self.f_7 = ExpForm(data_7)

    def test_expform(self):
        assert self.f.is_valid() == True
        assert self.f.cleaned_data['result_of_expression'] == 10
        assert self.f_1.is_valid() == False
        assert self.f_2.is_valid() == True
        assert self.f_2.cleaned_data['result_of_expression'] == 3130
        assert self.f_3.is_valid() == True
        assert self.f_3.cleaned_data['result_of_expression'] == 3136
        assert self.f_4.is_valid() == False
        assert self.f_5.is_valid() == False
        assert self.f_6.is_valid() == False
        with pytest.raises(ValidationError):
            self.f_1.clean()
            self.f_4.clean()
            self.f_5.clean()
            self.f_6.clean()

