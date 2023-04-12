# Generated by Django 4.2 on 2023-04-12 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='purchase_link',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/image/', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(max_length=2200, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Published'),
        ),
    ]