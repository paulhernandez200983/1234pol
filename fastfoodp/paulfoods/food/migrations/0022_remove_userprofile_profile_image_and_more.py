# Generated by Django 5.0.2 on 2024-02-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0021_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_image_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
