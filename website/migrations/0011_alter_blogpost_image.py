# Generated by Django 4.2 on 2023-04-13 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_blogpost_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/', verbose_name='Image'),
        ),
    ]
