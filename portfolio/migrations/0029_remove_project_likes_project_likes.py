# Generated by Django 4.0.5 on 2022-09-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0028_project_dislikes_project_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='likes',
        ),
        migrations.AddField(
            model_name='project',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
