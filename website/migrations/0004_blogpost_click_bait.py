# Generated by Django 4.2 on 2023-04-12 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_blogpost_image_alter_blogpost_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='click_bait',
            field=models.CharField(default='click bait', max_length=330, verbose_name='Click Bait'),
        ),
    ]
