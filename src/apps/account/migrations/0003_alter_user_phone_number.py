# Generated by Django 4.2.7 on 2023-12-01 17:42

import apps.account.custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, validators=[apps.account.custom_validators.validate_phone_number]),
        ),
    ]
