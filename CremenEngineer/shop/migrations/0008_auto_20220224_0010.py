# Generated by Django 3.2.8 on 2022-02-23 18:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_product_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 2, 23, 18, 40, 2, 521322, tzinfo=utc)),
        ),
    ]
