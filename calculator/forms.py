from django import forms
from django.core.exceptions import ValidationError
from calculator.models import Exp


class ExpForm(forms.ModelForm):
    exp = forms.CharField(label='Expression', widget=forms.TextInput(attrs={'placeholder': 'Enter expression'}))
    result_of_exp = forms.CharField(label='Result of expression', required=False,
                                    widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Exp
        fields = ['exp', 'result_of_exp']

    def clean_result_of_exp(self):
        exp = self.cleaned_data['exp']
        try:
            result_of_exp = eval(exp)
        except ZeroDivisionError:
            raise ValidationError('You can not division on zero')
        except NameError:
            raise ValidationError('You have entered invalid data')
        except SyntaxError:
            raise ValidationError('You have entered invalid data')
        if result_of_exp % 1 == 0:
            result_of_exp = int(result_of_exp)
        return result_of_exp
