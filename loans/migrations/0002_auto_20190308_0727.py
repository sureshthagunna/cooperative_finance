# Generated by Django 2.1.7 on 2019-03-08 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanaccount',
            old_name='principal',
            new_name='total_principal',
        ),
    ]
