# Generated by Django 4.1 on 2023-07-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_profile_alb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ALB',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ALP',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
