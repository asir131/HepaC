# Generated by Django 4.1 on 2023-07-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_profile_alb_alter_profile_alp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ALB',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ALT',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='AST',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='BIL',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='CHE',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='CHOL',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='CREA',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='GGT',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='PROT',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
