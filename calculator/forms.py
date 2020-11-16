from django import forms
from django.core.exceptions import ValidationError
from calculator.models import Exp


class ExpForm(forms.ModelForm):
    expression = forms.CharField(label='Expression', widget=forms.TextInput(attrs={'placeholder': 'Enter expression'}))
    result_of_expression = forms.CharField(label='Result of expression', required=False,
                                           widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Exp
        fields = ['expression', 'result_of_expression']

    def clean_result_of_expression(self):
        expression = self.cleaned_data['expression']
        try:
            result_of_expression = eval(expression)
        except ZeroDivisionError:
            raise ValidationError('You can not division on zero')
        except NameError:
            raise ValidationError('You have entered invalid data')
        except SyntaxError:
            raise ValidationError('You have entered invalid data')
        if result_of_expression % 1 == 0:
            result_of_expression = int(result_of_expression)
        return result_of_expression
