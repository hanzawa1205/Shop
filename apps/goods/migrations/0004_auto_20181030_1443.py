# Generated by Django 2.1.2 on 2018-10-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20181030_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.CharField(default='', max_length=16, verbose_name='价格'),
        ),
    ]
