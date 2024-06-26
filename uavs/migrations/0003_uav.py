# Generated by Django 4.2.2 on 2024-05-11 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uavs', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('image', models.ImageField(upload_to='uavs/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uavs.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uavs.category')),
            ],
        ),
    ]
