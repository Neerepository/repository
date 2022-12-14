# Generated by Django 4.0.5 on 2022-09-04 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_subcategory_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='category',
            name='categorias',
            field=models.CharField(choices=[('0', 'Asociadas a una discapacidad'), ('1', 'No asociadas a una discapacidad')], max_length=1, verbose_name='categorias'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcategorias',
            field=models.CharField(choices=[('0', 'Dislexia'), ('1', 'Disortografía'), ('2', 'Digrafía'), ('3', 'Discalculia'), ('4', 'Superdotación'), ('5', 'Altas capacidades'), ('6', 'Talentos'), ('7', 'Trastorno por déficit de atención (TDA)'), ('8', 'TDA con hiperactividad (TDA-H)'), ('9', 'Ceguera total'), ('10', 'Baja Visión'), ('12', 'Sordera'), ('13', 'Hipoacusia'), ('14', 'Musculo esquelético'), ('15', 'Trastorno autista'), ('16', 'Trastorno de Asperger'), ('17', 'Trastorno de Rett'), ('18', 'Trastorno de desintegración infantil')], max_length=2, verbose_name='subcategorias'),
        ),
    ]
