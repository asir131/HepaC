# Generated by Django 4.1 on 2023-07-19 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_profile_alp_alter_profile_alt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ALB',
            field=models.IntegerField(default=0),
        ),
    ]
