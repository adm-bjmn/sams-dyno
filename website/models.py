from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class Topic(models.Model):
    topic = models.CharField(
        'Topic', max_length=25, unique=True)

    def __str__(self):
        return self.topic


class BlogPost(models.Model):
    title = models.CharField('Title', max_length=300)
    topic = models.ManyToManyField(
        Topic, symmetrical=False, blank=True,)
    content = RichTextField('Content', max_length=5000)
    click_bait = models.CharField(
        'Click Bait', default='click bait', max_length=300)
    publish_date = models.DateField('Published', auto_now_add=True)
    link = models.URLField('Link', blank=True)
    image = models.ImageField(
        'Image', blank=True, upload_to='blog_images/')

    def __str__(self):
        return self.title + ' | ' + str(self.publish_date)
