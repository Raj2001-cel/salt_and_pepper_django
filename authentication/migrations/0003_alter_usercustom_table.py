# Generated by Django 4.0.3 on 2022-03-18 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_usertable_usercustom'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='usercustom',
            table='UserCustom',
        ),
    ]
