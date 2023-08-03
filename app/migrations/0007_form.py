# Generated by Django 4.0.10 on 2023-08-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_list_blog_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('gender', models.CharField(max_length=200, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('program', models.CharField(max_length=200, null=True)),
                ('commite', models.CharField(max_length=200, null=True)),
                ('source', models.CharField(max_length=200, null=True)),
                ('employ', models.CharField(max_length=200, null=True)),
                ('current_employ', models.CharField(max_length=200, null=True)),
                ('tech', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('nationality', models.CharField(max_length=200, null=True)),
                ('option', models.CharField(max_length=300, null=True)),
                ('industry', models.CharField(max_length=200, null=True)),
                ('expectation', models.CharField(max_length=300, null=True)),
                ('hear', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
