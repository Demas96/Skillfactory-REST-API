# Generated by Django 4.0.5 on 2022-06-23 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=255)),
                ('ongitude', models.FloatField(max_length=255)),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', main.models.CaseInsensitiveTextField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('N', 'new'), ('P', 'pending'), ('A', 'accepted'), ('R', 'rejected')], default='N', max_length=1)),
                ('beautyTitle', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('other_titles', models.CharField(max_length=255)),
                ('connect', models.TextField(blank=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('level_winter', models.CharField(blank=True, max_length=255)),
                ('level_summer', models.CharField(blank=True, max_length=255)),
                ('level_autumn', models.CharField(blank=True, max_length=255)),
                ('level_spring', models.CharField(blank=True, max_length=255)),
                ('coords_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.coords')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.users')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.BinaryField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('pereval_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.perevaladd')),
            ],
        ),
    ]