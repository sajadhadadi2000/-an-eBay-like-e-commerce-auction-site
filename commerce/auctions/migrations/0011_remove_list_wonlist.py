# Generated by Django 4.1.7 on 2023-03-19 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_list_wonlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='wonlist',
        ),
    ]
