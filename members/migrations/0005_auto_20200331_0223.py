# Generated by Django 3.0.1 on 2020-03-31 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20200331_0221'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]
