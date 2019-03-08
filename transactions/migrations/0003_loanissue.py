# Generated by Django 2.1.7 on 2019-03-08 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_auto_20190308_0727'),
        ('transactions', '0002_auto_20190306_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.PositiveIntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.LoanAccount')),
            ],
        ),
    ]