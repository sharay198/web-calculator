from django import forms
from django.core.exceptions import ValidationError
from calculator.models import Exp
from .validators import *


class ExpForm(forms.ModelForm):
    expression = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter expression'}))
    result_of_expression = forms.CharField(required=False,
                                           widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Exp
        fields = ['expression', 'result_of_expression']

    # def clean_expression(self):
    #     expression = self.cleaned_data['expression']
    #     for item in expression:
    #         if not isinstance(item, int) or item != '.':
    #             raise ValidationError('You have entered invalid data')
    #     return expression

    def clean_result_of_expression(self):
        expression = self.cleaned_data.get('expression')
        if check_string(expression) and check_string_s_action(expression):

            try:
                result_of_expression = eval(expression, {'__builtins__': {}})
            except ZeroDivisionError:
                raise ValidationError('You can not division on zero')
            except NameError:
                raise ValidationError('You have entered invalid data')
            except SyntaxError:
                raise ValidationError('You have entered invalid data')
            except KeyError:
                raise ValidationError('You have entered invalid data')
            # except TypeError:
            #     raise ValidationError('You have entered invalid data')

            if not isinstance(result_of_expression, (int, float)):
                raise ValidationError('You have entered invalid data')
            if result_of_expression % 1 == 0:
                result_of_expression = int(result_of_expression)
            return result_of_expression
        # else:
        #     raise ValidationError('0')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     expression = self.cleaned_data.get('expression')
    #     result_of_expression = self.cleaned_data.get('result of expression')
    #
    #     if not expression:
    #         raise ValidationError('Empty')
    #     else:
    #         return self.cleaned_data
