# Generated by Django 3.2 on 2022-12-14 13:16

from django.db import migrations
import shop.fields
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20221214_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pulsarproduct',
            name='image',
            field=shop.fields.WEBPField(upload_to=shop.models.image_folder, verbose_name='Image'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
