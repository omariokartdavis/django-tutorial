# Generated by Django 2.1 on 2018-11-28 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20181123_1130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
    ]
