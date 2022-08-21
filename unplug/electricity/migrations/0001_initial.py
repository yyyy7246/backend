# Generated by Django 4.1 on 2022-08-21 03:29

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.UUIDField(unique=True)),
                ('watt', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 8, 21, 3, 29, 29, 784081))),
            ],
            options={
                'db_table': 'index',
            },
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('average_Kwatt', models.IntegerField()),
            ],
            options={
                'db_table': 'metadata',
            },
        ),
    ]
