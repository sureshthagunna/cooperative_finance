# Generated by Django 2.1.7 on 2019-06-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0006_auto_20190326_0848'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoanDelete',
        ),
        migrations.AddField(
            model_name='loanissue',
            name='delete_status',
            field=models.CharField(choices=[('False', 'False'), ('True', 'True')], default='False', editable=False, max_length=5),
        ),
        migrations.AddField(
            model_name='loanpayment',
            name='delete_status',
            field=models.CharField(choices=[('False', 'False'), ('True', 'True')], default='False', editable=False, max_length=5),
        ),
    ]