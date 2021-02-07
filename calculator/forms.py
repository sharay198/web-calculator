from django import forms
from django.core.exceptions import ValidationError
from calculator.models import Exp
from .calculator import *


class ExpForm(forms.ModelForm):
    expression = forms.CharField(error_messages={'required': 'Please enter your expression'},
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter expression'}),
                                 help_text='Enter expression')
    result_of_expression = forms.CharField(required=False,
                                           widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Exp
        fields = ['expression', 'result_of_expression']

    def clean(self):
        cleaned_data = super(ExpForm, self).clean()
        expression = self.cleaned_data.get('expression')
        try:
            cleaned_data['result_of_expression'] = calculate_expression(expression)
        except ZeroDivisionError:
            raise ValidationError('You can not division on zero')
        except (NameError, SyntaxError, KeyError, IndexError, TypeError):
            raise ValidationError('You have entered invalid data 1')
        else:
            if check_if_floordiv(expression) or check_empty_only_brackets_is_in_expression(expression):
                raise ValidationError('You have entered invalid data')
        return cleaned_data
