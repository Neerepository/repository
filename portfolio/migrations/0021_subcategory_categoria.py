# Generated by Django 4.0.5 on 2022-09-04 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_alter_project_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.category'),
        ),
    ]
