# Generated by Django 5.0.6 on 2024-06-27 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_zapato_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapato',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='zapatos/'),
        ),
    ]
