# Generated by Django 5.1.6 on 2025-03-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urbanchattelapp', '0012_remove_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=models.ImageField(upload_to='property/'),
        ),
    ]
