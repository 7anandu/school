# Generated by Django 4.1 on 2022-10-23 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0003_remove_person_materials_delete_material'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='district',
            new_name='department',
        ),
    ]