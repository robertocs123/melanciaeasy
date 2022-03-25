# Generated by Django 2.2.2 on 2020-04-16 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Preco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rgrauda', models.FloatField(default=1.0)),
                ('rmedia', models.FloatField(default=1.0)),
                ('rmiuda', models.FloatField(default=1.0)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('vendedor', models.CharField(default='Roberto', max_length=30)),
                ('tipomelancia', models.CharField(choices=[('rgrauda', 'Redonda Graúda'), ('rmedia', 'Redonda Média'), ('rmiuda', 'Redonda Miúda')], max_length=7)),
                ('logradouro', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('pontoreferencia', models.CharField(max_length=100)),
                ('valor', models.FloatField(default=0.0)),
                ('done', models.CharField(choices=[('doing', 'Doing'), ('done', 'Done')], max_length=5)),
                ('comentario', models.TextField(default='Sem comentário', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]