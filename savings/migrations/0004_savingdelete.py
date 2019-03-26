# Generated by Django 2.1.7 on 2019-03-23 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0003_savingaccount_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavingDelete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tran_type', models.CharField(max_length=8)),
                ('amount', models.PositiveIntegerField()),
                ('account', models.CharField(max_length=256)),
            ],
        ),
    ]
