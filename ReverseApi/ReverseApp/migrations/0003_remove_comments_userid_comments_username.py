# Generated by Django 4.0.1 on 2022-03-08 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReverseApp', '0002_rename_commentsid_comments_commentid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='UserId',
        ),
        migrations.AddField(
            model_name='comments',
            name='Username',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]