# Generated by Django 4.0.5 on 2022-09-04 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_alter_category_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.category'),
        ),
    ]
