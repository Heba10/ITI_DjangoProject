# Generated by Django 3.0.3 on 2020-02-20 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_post_author_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author_id',
            new_name='author',
        ),
    ]
