# Generated by Django 3.1.6 on 2021-09-18 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20210915_2103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site_map',
            old_name='site_E',
            new_name='impact',
        ),
        migrations.RenameField(
            model_name='site_map',
            old_name='site_Eby',
            new_name='impact_by',
        ),
        migrations.RenameField(
            model_name='site_map',
            old_name='site_lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='site_map',
            old_name='site_long',
            new_name='long',
        ),
        migrations.RenameField(
            model_name='site_map',
            old_name='site_id',
            new_name='siteid',
        ),
        migrations.RenameField(
            model_name='site_map',
            old_name='site_name',
            new_name='sitename',
        ),
        migrations.RenameField(
            model_name='site_map',
            old_name='site_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='site_map',
            old_name='site_weight',
            new_name='weight',
        ),
    ]
