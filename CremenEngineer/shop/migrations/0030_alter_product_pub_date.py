# Generated by Django 4.0.2 on 2022-03-01 12:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_alter_product_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 3, 1, 12, 3, 27, 280942, tzinfo=utc)),
        ),
    ]
