# Generated by Django 2.2 on 2019-05-21 15:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_merge_20190521_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalcustomuser',
            name='bio',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='bio'),
        ),
        migrations.AlterField(
            model_name='historicalorganization',
            name='description',
            field=tinymce.models.HTMLField(default='', verbose_name='Activity description'),
        ),
    ]
