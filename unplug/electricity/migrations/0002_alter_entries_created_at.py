# Generated by Django 4.1 on 2022-08-16 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electricity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 5, 32, 19, 897634)),
        ),
    ]
