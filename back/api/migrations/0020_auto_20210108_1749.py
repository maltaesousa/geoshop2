# Generated by Django 3.0.8 on 2021-01-08 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20201218_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='link',
            field=models.URLField(default='images/default_product_thumbnail.png', help_text='Please complete the above URL', max_length=2000, verbose_name='link'),
        ),
    ]
