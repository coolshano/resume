# Generated by Django 3.2.12 on 2022-03-21 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20220321_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
