# Generated by Django 3.2.4 on 2021-06-14 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210614_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='SubCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='core.subcategory'),
        ),
    ]
