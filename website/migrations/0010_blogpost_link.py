# Generated by Django 4.2 on 2023-04-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_blogpost_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
    ]
