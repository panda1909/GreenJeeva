# Generated by Django 3.2.4 on 2021-06-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210622_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Method',
            field=models.CharField(blank=True, default=' ', max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Potency',
            field=models.CharField(blank=True, default=' ', max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ProductForm',
            field=models.CharField(blank=True, default=' ', max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Source',
            field=models.CharField(blank=True, default=' ', max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Temperature',
            field=models.CharField(blank=True, default=' ', max_length=512, null=True),
        ),
    ]
