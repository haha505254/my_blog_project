# Generated by Django 4.0.6 on 2022-08-03 06:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, max_length=250),
        ),
    ]
