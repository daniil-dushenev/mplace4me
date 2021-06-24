# Generated by Django 3.2.3 on 2021-06-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0012_remove_images_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='count',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='item',
            name='img_count',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]