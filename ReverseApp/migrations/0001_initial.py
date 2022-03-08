# Generated by Django 4.0.1 on 2022-03-08 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('TopicId', models.AutoField(primary_key=True, serialize=False)),
                ('TopicContent', models.CharField(max_length=500)),
                ('TotalVote', models.IntegerField(default=0)),
                ('YesVote', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=30)),
                ('UserPassword', models.CharField(max_length=30)),
                ('UserAvatarFileName', models.CharField(max_length=500)),
                ('DateOfJoing', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('CommentsId', models.AutoField(primary_key=True, serialize=False)),
                ('DateOfComment', models.DateField()),
                ('CommentContent', models.CharField(max_length=500)),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReverseApp.users')),
            ],
        ),
    ]
