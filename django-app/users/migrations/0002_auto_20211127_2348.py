# Generated by Django 3.2.9 on 2021-11-27 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='spouse_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='degree_programme',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
