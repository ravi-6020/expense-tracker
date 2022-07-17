# Generated by Django 4.0.6 on 2022-07-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_expense_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='income',
            field=models.FloatField(default=0),
        ),
    ]
