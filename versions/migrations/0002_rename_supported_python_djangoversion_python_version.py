# Generated by Django 4.2.4 on 2023-08-19 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('versions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='djangoversion',
            old_name='supported_python',
            new_name='python_version',
        ),
    ]
