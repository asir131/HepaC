# Generated by Django 4.1 on 2023-07-19 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_profile_alb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ALP',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ALT',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='AST',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='BIL',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='CHE',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='CHOL',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='CREA',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='GGT',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='PROT',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='comment',
            field=models.TextField(default='', null=True),
        ),
    ]
