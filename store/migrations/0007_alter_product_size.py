# Generated by Django 3.2 on 2021-05-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(blank=True),
        ),
    ]
