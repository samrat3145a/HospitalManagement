# Generated by Django 3.2.4 on 2021-06-23 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginSystem', '0002_alter_userdata_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospitaldata',
            old_name='name',
            new_name='Hospital_Name',
        ),
    ]
