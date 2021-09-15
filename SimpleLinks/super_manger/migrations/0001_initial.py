# Generated by Django 3.1.6 on 2021-09-15 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('customer_rights', 'Global customer rights'), ('vendor_rights', 'Global vendor rights'), ('any_rights', 'Global any rights')),
                'managed': False,
                'default_permissions': (),
            },
        ),
    ]
