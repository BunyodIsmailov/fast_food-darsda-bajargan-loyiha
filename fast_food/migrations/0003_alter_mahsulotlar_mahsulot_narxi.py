# Generated by Django 4.0.5 on 2022-06-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_food', '0002_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulotlar',
            name='mahsulot_narxi',
            field=models.FloatField(),
        ),
    ]
