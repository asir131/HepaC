# Generated by Django 4.1 on 2023-07-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_profile_alb_alter_profile_alp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ALB',
            field=models.FloatField(default=0, null=True),
        ),
    ]
