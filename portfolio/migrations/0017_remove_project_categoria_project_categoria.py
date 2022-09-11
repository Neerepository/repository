# Generated by Django 4.0.5 on 2022-09-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_alter_category_categorias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='categoria',
        ),
        migrations.AddField(
            model_name='project',
            name='categoria',
            field=models.ManyToManyField(to='portfolio.subcategory'),
        ),
    ]