# Generated by Django 4.0.6 on 2022-07-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_expense_amount_alter_profile_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
