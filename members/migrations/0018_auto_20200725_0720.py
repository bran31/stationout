# Generated by Django 3.0.3 on 2020-07-25 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0017_auto_20200522_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact_city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_street_address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='unit',
            field=models.CharField(choices=[('33W', '33W'), ('33A', '33A'), ('43V', '43V'), ('43H', '43H'), ('33D', '33D'), ('43G', '43G'), ('33Z', '33Z'), ('43A', '43A'), ('33F', '33F'), ('43C', '43C'), ('33C', '33C'), ('43D', '43D'), ('33E', '33E'), ('C43', 'C43'), ('B43', 'B43'), ('VR', 'VR')], max_length=3),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]