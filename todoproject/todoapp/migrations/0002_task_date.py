# Generated by Django 3.2.12 on 2022-03-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1995-12-13'),
            preserve_default=False,
        ),
    ]