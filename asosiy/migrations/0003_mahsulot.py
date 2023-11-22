# Generated by Django 4.2.7 on 2023-11-22 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_remove_bolim_boss_remove_bolim_ishchilar_soni_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('brend', models.CharField(max_length=20)),
                ('narx', models.CharField(max_length=30)),
                ('batafsil', models.CharField(blank=True, max_length=30, null=True)),
                ('bolim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.bolim')),
            ],
        ),
    ]