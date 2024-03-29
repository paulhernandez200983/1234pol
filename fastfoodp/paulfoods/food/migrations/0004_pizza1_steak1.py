# Generated by Django 4.1.1 on 2022-09-10 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_drink1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('priceM', models.DecimalField(decimal_places=2, max_digits=4)),
                ('priceL', models.DecimalField(decimal_places=2, max_digits=4)),
                ('zImage', models.URLField()),
                ('loc', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Steak1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('priceM', models.DecimalField(decimal_places=2, max_digits=4)),
                ('priceL', models.DecimalField(decimal_places=2, max_digits=4)),
                ('sImage', models.URLField()),
                ('loc', models.CharField(max_length=120)),
            ],
        ),
    ]
