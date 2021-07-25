# Generated by Django 3.2.5 on 2021-07-17 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythons_auth', '0003_auto_20210715_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pythonsuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]
