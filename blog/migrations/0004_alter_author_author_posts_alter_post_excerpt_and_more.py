# Generated by Django 5.0.3 on 2024-04-23 00:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to='blog.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
