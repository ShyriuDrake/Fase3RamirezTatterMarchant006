# Generated by Django 3.2.2 on 2021-05-14 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_manga_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('volumen', models.TextField(max_length=200)),
                ('descripcion', models.TextField(max_length=1000)),
            ],
        ),
        migrations.RenameModel(
            old_name='Genero',
            new_name='TipoReceta',
        ),
        migrations.DeleteModel(
            name='Manga',
        ),
    ]
