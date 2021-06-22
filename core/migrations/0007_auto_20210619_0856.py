# Generated by Django 3.2.4 on 2021-06-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_blog_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Image',
            field=models.ImageField(default='blog_images/default.png', upload_to='blog_images'),
        ),
        migrations.AddField(
            model_name='blog',
            name='Title',
            field=models.CharField(default='Title', max_length=5000),
        ),
    ]