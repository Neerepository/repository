# Generated by Django 4.0.5 on 2022-09-04 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_category_subcategory_project_subcategoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='categoria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='portfolio.category'),
            preserve_default=False,
        ),
    ]
