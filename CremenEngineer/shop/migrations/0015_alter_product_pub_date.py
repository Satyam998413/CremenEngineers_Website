# Generated by Django 3.2.8 on 2022-02-25 06:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_product_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 2, 25, 6, 8, 6, 216091, tzinfo=utc)),
        ),
    ]
