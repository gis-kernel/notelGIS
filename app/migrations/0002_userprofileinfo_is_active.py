# Generated by Django 2.2.1 on 2019-06-28 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
