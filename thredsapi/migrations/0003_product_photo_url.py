# Generated by Django 4.1.3 on 2023-07-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thredsapi', '0002_product_description_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo_url',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]