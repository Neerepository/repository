# Generated by Django 4.0.5 on 2022-09-04 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_remove_subcategory_categoria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='subcategoria',
        ),
        migrations.AlterField(
            model_name='project',
            name='categoria',
            field=models.CharField(choices=[('0', 'Dislexia'), ('1', 'Disortografía'), ('2', 'Digrafía'), ('3', 'Discalculia'), ('4', 'Superdotación'), ('5', 'Altas capacidades'), ('6', 'Talentos'), ('7', 'Trastorno por déficit de atención (TDA)'), ('8', 'TDA con hiperactividad (TDA-H)'), ('9', 'Ceguera total'), ('10', 'Baja Visión'), ('12', 'Sordera'), ('13', 'Hipoacusia'), ('14', 'Musculo esquelético'), ('15', 'Trastorno autista'), ('16', 'Trastorno de Asperger'), ('17', 'Trastorno de Rett'), ('18', 'Trastorno de desintegración infantil')], max_length=2, verbose_name='categorias'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
