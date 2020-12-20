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

    # def clean_expression(self):
    #     expression = self.cleaned_data['expression']
    #     for item in expression:
    #         if not isinstance(item, int) or item != '.':
    #             raise ValidationError('You have entered invalid data')
    #     return expression

    def clean_result_of_expression(self):
        expression = self.cleaned_data.get('expression')
        # if check_string(expression) and check_string_s_action(expression):

        try:
            result_of_expression = eval(expression, {'__builtins__': {}}, {})
        except ZeroDivisionError:
            raise ValidationError('You can not division on zero')
        except NameError:
            raise ValidationError('You have entered invalid data 1')
        except SyntaxError:
            raise ValidationError('You have entered invalid data 2')
        except KeyError:
            raise ValidationError('You have entered invalid data 3')
        except IndexError:
            raise ValidationError('You have entered invalid data 4')
        except TypeError:
            raise ValidationError('You have entered invalid data 5')

        if not isinstance(result_of_expression, (int, float)):
            raise ValidationError('You have entered invalid data 6')
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
