# Generated by Django 4.0.5 on 2022-09-03 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_remove_category_tipocategorias_subcategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categorias',
            field=models.CharField(choices=[('0', 'Asociadas a una discapacidad'), ('1', 'No asociadas a una discapacidad')], max_length=1, verbose_name='categorias'),
        ),
    ]