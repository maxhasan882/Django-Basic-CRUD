# Generated by Django 2.2.8 on 2019-12-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191204_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.ManyToManyField(related_name='product_price', to='api.Price'),
        ),
    ]
