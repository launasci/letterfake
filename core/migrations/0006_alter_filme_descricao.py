# Generated by Django 4.0.5 on 2023-02-10 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_filme_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='descricao',
            field=models.CharField(max_length=140),
        ),
    ]