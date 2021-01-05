from django import forms
from django.core.exceptions import ValidationError
from calculator.models import Exp
from .validators import *


class ExpForm(forms.ModelForm):
    expression = forms.CharField(error_messages={'required': 'Please enter your expression'},
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter expression'}),
                                 help_text='Enter expression')
    result_of_expression = forms.CharField(required=False,
                                           widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Exp
        fields = ['expression', 'result_of_expression']

    # def clean_result_of_expression(self):
    #     expression = self.cleaned_data['expression']
    #     try:
    #         result_of_expression = eval(expression)
    #     except Exception:
    #         raise ValidationError('Wrong data')
    #     return result_of_expression
    # def clean_expression(self):
    #     expression = self.cleaned_data['expression']
    #     try:
    #         eval(expression, {'__builtins__': {}}, {})
    #     except ZeroDivisionError:
    #         raise ValidationError('You can not division on zero')
    #     except NameError:
    #         raise ValidationError('You have entered invalid data 1')
    #     except SyntaxError:
    #         raise ValidationError('You have entered invalid data 2')
    #     except KeyError:
    #         raise ValidationError('You have entered invalid data 3')
    #     except IndexError:
    #         raise ValidationError('You have entered invalid data 4')
    #     except TypeError:
    #         raise ValidationError('You have entered invalid data 5')
    #     return expression

    # def clean_result_of_expression(self):
    #     result = self.cleaned_data.get('result_of_expression')
    #     if result % 1 == 0:
    #         return int(result)
    #     return result

    # def clean(self):
    # cleaned_data = super().clean()
    # expression = self.cleaned_data.get('expression')
    # result_of_expression = self.cleaned_data.get('result of expression')
    # if expression and result_of_expression = '':
    #     result_of_expression = eval(expression)
    # if not expression:
    #     raise ValidationError('Empty')
