# Generated by Django 4.2.1 on 2023-06-29 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appGrupoZero', '0003_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_ingresado', models.DateField(null=True)),
                ('foto', models.ImageField(null=True, upload_to='obra')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appGrupoZero.tipo')),
            ],
        ),
    ]
