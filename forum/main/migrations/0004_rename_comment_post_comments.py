# Generated by Django 4.0.5 on 2022-06-21 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_reply_comment_post_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='comment',
            new_name='comments',
        ),
    ]