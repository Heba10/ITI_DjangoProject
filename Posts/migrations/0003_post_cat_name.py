# Generated by Django 3.0.3 on 2020-02-20 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cat_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Posts.Category'),
            preserve_default=False,
        ),
    ]
