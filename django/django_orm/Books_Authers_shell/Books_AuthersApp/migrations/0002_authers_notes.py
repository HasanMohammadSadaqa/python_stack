# Generated by Django 2.2.4 on 2022-10-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books_AuthersApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authers',
            name='notes',
            field=models.TextField(default='notes...'),
        ),
    ]