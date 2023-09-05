# Generated by Django 4.2.5 on 2023-09-05 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='books_rental',
            name='rental_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 5, 14, 24, 19, 98488, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='books_rental',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 12, 14, 24, 19, 98488, tzinfo=datetime.timezone.utc)),
        ),
    ]
