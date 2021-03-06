# Generated by Django 2.2.8 on 2019-12-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191204_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.IntegerField()),
                ('last', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.ManyToManyField(to='api.Price'),
        ),
    ]
