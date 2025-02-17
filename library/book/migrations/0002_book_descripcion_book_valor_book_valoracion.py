# Generated by Django 5.1.2 on 2024-10-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='descripcion',
            field=models.TextField(default='un gran libro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='valor',
            field=models.DecimalField(decimal_places=2, default='08', max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='valoracion',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default='2'),
            preserve_default=False,
        ),
    ]
