# Generated by Django 3.2.4 on 2021-06-03 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=models.TextField(default='Description', max_length=10000, null=True),
        ),
    ]
