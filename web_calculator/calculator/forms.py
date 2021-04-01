from django import forms
from django.core.exceptions import ValidationError
from calculator.models import Expression
from .calculator import *


class ExpForm(forms.ModelForm):
    expression = forms.CharField(error_messages={'required': 'Please enter your expression'},
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter expression'}),
                                 help_text='Enter expression')
    result = forms.CharField(required=False,
                             widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Expression
        fields = ['expression', 'result']

    def clean(self):
        cleaned_data = super(ExpForm, self).clean()
        expression = self.cleaned_data.get('expression')
        try:
            cleaned_data['result'] = calculate_expression(expression)
        except ZeroDivisionError:
            raise ValidationError('You can not division on zero')
        except (NameError, SyntaxError, KeyError, IndexError, TypeError):
            raise ValidationError('You have entered invalid data')
        else:

            if check_if_floordiv(expression) or check_empty_only_brackets_is_in_expression(expression):
                raise ValidationError('You have entered invalid data')
        return cleaned_data
