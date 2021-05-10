# Generated by Django 3.2 on 2021-05-10 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210510_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('WHITE', 'White'), ('BLACK', 'Black'), ('RED', 'Red'), ('BLUE', 'Blue')], default='WHITE', max_length=20),
        ),
    ]
