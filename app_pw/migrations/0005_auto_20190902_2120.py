# Generated by Django 2.2.4 on 2019-09-02 21:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_pw', '0004_auto_20190902_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]