# Generated by Django 2.2 on 2019-05-13 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brevisapp', '0014_auto_20190513_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='editingproject',
            old_name='proj_name',
            new_name='name',
        ),
    ]
