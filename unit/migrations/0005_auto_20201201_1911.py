# Generated by Django 3.1.1 on 2020-12-02 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0004_auto_20201128_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airman',
            name='ssn',
            field=models.CharField(max_length=11),
        ),
    ]