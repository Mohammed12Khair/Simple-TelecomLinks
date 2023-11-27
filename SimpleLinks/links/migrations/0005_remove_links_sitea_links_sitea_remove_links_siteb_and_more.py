# Generated by Django 4.0.3 on 2022-04-17 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0004_links'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='siteA',
        ),
        migrations.AddField(
            model_name='links',
            name='siteA',
            field=models.ManyToManyField(related_name='SiteA', to='links.site_map'),
        ),
        migrations.RemoveField(
            model_name='links',
            name='siteB',
        ),
        migrations.AddField(
            model_name='links',
            name='siteB',
            field=models.ManyToManyField(related_name='SiteB', to='links.site_map'),
        ),
    ]