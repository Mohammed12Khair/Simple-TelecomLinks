# Generated by Django 3.1.6 on 2021-09-15 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_manger', '0002_auto_20210915_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='siteAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=30)),
                ('value', models.IntegerField(blank=True, default='')),
            ],
        ),
    ]
