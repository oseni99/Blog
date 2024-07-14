# Generated by Django 5.0.3 on 2024-04-23 01:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_author_author_posts_alter_post_excerpt_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='author_posts',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to='blog.author'),
        ),
    ]
