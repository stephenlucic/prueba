# Generated by Django 4.2.1 on 2023-07-13 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appGrupoZero', '0009_alter_artista_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
