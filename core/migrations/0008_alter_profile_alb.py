# Generated by Django 4.1 on 2023-07-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_profile_alb_alter_profile_alt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ALB',
            field=models.FloatField(default=0.0),
        ),
    ]
