from django.db import models
from datetime import datetime


class Topic(models.Model):
    ''' The Genre model allows Genre objects to be created which can
    then be associated to a book object via a many to many field.
    Each book can have an number of genres 
    associated to it. including None.
    '''
    topic = models.CharField(
        'Topic', max_length=25, unique=True)

    def __str__(self):
        return self.topic


# Create your models here.
class BlogPost(models.Model):
    ''' The book model provides the main object for the synopsis functionality
    Aside from the Obvious critera for a book, the model also includes
    a link to an image online and a link to a destination where 
    the book can be purchased.
    The many to many fields liked_by and seen_by are functionality fields.
    A book that has been liked by a user will apear in thier my books page,
    while a book that has been seen_by a user will not appear in future
    searches unless seen_by is reset on the profile page.
    '''
    title = models.CharField('Title', max_length=25)
    topic = models.ManyToManyField(
        Topic, symmetrical=False, blank=True)
    content = models.TextField('Content', max_length=2200)
    publish_date = models.DateField('Published', auto_now_add=True)
    link = models.URLField('Link', blank=True, null=True)
    image = models.ImageField(
        'Image', null=True, blank=True, upload_to='blog_images/')

    def __str__(self):
        return self.title + ' | ' + str(self.publish_date)
