# Generated by Django 3.1.2 on 2020-11-16 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_auto_20200424_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exp',
            old_name='exp',
            new_name='expression',
        ),
        migrations.RenameField(
            model_name='exp',
            old_name='result_of_exp',
            new_name='result_of_expression',
        ),
    ]