# Generated by Django 4.1.3 on 2022-12-12 22:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0006_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='resenia',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=80),
        ),
    ]
