# Generated by Django 4.2.2 on 2023-08-03 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_register1_city_register1_country_register1_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='register1',
            name='gender',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
