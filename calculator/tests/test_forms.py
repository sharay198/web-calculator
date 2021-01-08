from django.core.exceptions import ValidationError
from ..forms import ExpForm
from django.test import TestCase
import pytest


# Create your tests here.
class TestForms():
    d = {'expression': '1/0'}
    f = ExpForm(d)

    def test_clean(self):
        expression = '1/0'
        pytest.raises(ValidationError, ExpForm.clean, '1/0')
