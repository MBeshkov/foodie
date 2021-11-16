# Generated by Django 3.2.9 on 2021-11-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('vegan', models.BooleanField()),
                ('username', models.CharField(max_length=25)),
            ],
        ),
    ]
