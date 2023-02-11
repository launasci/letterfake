# Generated by Django 4.0.5 on 2023-02-08 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_activitylog_id_alter_todo_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('descricao', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('categoria', models.TextField(choices=[('terror', 'Terror'), ('comedia', 'Comédia'), ('acao', 'Ação'), ('drama', 'Drama'), ('outros', 'Outros')], null=True)),
                ('imagem', models.URLField(default='https://example.com/filmes/default.jpg')),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
