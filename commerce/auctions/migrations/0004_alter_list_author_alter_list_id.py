# Generated by Django 4.1.7 on 2023-03-10 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_list_status_alter_list_url_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='author',
            field=models.ForeignKey(default='auctions.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
