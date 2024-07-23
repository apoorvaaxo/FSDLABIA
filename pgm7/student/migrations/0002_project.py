# Generated by Django 5.0.7 on 2024-07-23 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=70)),
                ('language_used', models.CharField(max_length=200)),
                ('duration', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]