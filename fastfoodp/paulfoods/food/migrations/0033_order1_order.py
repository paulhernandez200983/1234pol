# Generated by Django 5.0.2 on 2024-03-07 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0032_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order1',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items1', to='food.order'),
            preserve_default=False,
        ),
    ]
