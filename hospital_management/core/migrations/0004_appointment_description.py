# Generated by Django 5.0.1 on 2024-03-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]