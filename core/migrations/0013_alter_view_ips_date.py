# Generated by Django 3.2.4 on 2021-07-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210729_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view_ips',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
