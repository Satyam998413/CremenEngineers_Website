# Generated by Django 4.0.2 on 2022-02-28 13:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_alter_product_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 2, 28, 13, 14, 59, 196392, tzinfo=utc)),
        ),
    ]
