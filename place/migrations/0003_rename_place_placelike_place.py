# Generated by Django 5.1.1 on 2024-09-16 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_alter_placeimage_image_placelike_delete_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placelike',
            old_name='Place',
            new_name='place',
        ),
    ]
