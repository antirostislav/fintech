# Generated by Django 3.2.9 on 2021-12-24 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=63)),
                ('description', models.TextField(max_length=1023)),
                ('datetime', models.DateTimeField()),
                ('value', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('value', models.IntegerField()),
            ],
        ),
    ]
