from django.db import models


# Create your models here.


class Expression(models.Model):
    expression = models.CharField('expression', max_length=150)
    result = models.CharField('result', max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.expression, self.result, self.created_at)
