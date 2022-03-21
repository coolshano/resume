# Generated by Django 3.2.12 on 2022-03-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20220321_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification1', models.CharField(max_length=100, null=True)),
                ('certification2', models.CharField(max_length=100, null=True)),
                ('certification3', models.CharField(max_length=100, null=True)),
                ('certification4', models.CharField(max_length=100, null=True)),
                ('certification5', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100, null=True)),
                ('hnd', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
