# Generated by Django 4.0.10 on 2023-08-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='list_blog',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
