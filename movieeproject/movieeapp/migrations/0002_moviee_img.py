# Generated by Django 3.2.12 on 2022-02-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviee',
            name='img',
            field=models.ImageField(default='marjaan', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
