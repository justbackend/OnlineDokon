# Generated by Django 4.2.7 on 2023-11-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('ishchilar_soni', models.PositiveIntegerField()),
                ('boss', models.CharField(max_length=80)),
            ],
        ),
    ]
