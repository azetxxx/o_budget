# Generated by Django 4.2.7 on 2023-12-18 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='ContractCategory',
        ),
    ]