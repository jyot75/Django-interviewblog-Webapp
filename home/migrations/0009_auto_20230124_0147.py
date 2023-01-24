# Generated by Django 3.2.16 on 2023-01-23 20:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_blogpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='company',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='job_offer',
            field=models.CharField(choices=[('Summer Internship', 'Summer Internship'), ('Winter Internship & Job', 'Winter Internship & Job'), ('Job', 'Job'), ('Winter Internship Only', 'Winter Internship Only')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='profile',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]