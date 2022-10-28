# Generated by Django 4.0.1 on 2022-05-23 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('number', models.CharField(max_length=14)),
                ('mail', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Get in touch',
                'verbose_name_plural': 'Get in touch',
            },
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=200)),
                ('name', models.CharField(max_length=20)),
                ('work', models.CharField(max_length=12)),
                ('image', models.ImageField(upload_to='Developer/%Y/%m')),
            ],
        ),
    ]
