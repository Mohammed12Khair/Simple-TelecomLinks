# Generated by Django 3.1.6 on 2021-09-15 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super_manger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permissionmaster',
            options={'default_permissions': (), 'managed': False, 'permissions': (('AddSite', 'Add New Site'), ('vendor_rights', 'Global vendor rights'), ('any_rights', 'Global any rights'))},
        ),
    ]
