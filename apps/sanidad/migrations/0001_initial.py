# Generated by Django 5.0.2 on 2024-11-22 01:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('img', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductosControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('compuestoActivo', models.CharField(max_length=20)),
                ('fichaTecnica', models.TextField()),
                ('contenido', models.IntegerField()),
                ('tipoContenido', models.CharField(max_length=10)),
                ('unidades', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoPlaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('img', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TiposControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Afecciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_Plantacion', models.IntegerField()),
                ('fechaEncuentro', models.DateField()),
                ('estado', models.CharField(choices=[('ST', 'ST'), ('EC', 'EC'), ('EL', 'EL')], default='ST', max_length=30)),
                ('fk_Plaga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sanidad.plaga')),
            ],
        ),
        migrations.AddField(
            model_name='plaga',
            name='fk_Tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sanidad.tipoplaga'),
        ),
        migrations.CreateModel(
            name='Controles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fechaControl', models.DateField()),
                ('fk_Afeccion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sanidad.afecciones')),
                ('fk_TipoControl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sanidad.tiposcontrol')),
            ],
        ),
        migrations.CreateModel(
            name='UsoProductosControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadProducto', models.IntegerField()),
                ('fk_Control', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sanidad.controles')),
                ('fk_ProductoControl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sanidad.productoscontrol')),
            ],
        ),
    ]
