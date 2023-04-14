
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('Repair-Shop', views.repair_shop, name='repairs'),
    path('Performance-Shop', views.performance_shop, name='performance'),
    path('contact', views.contact, name='contact'),
    path('blog-home', views.blog_posts, name='blog'),
    path('blog-details/<post_id>', views.blog_details, name='blog_details'),
    path('create-blog', views.create_blog_post, name='create_blog'),
    path('edit-blog//<post_id>', views.edit_blog_post, name='edit_blog'),
    path('delete-blog-post/<post_id>',
         views.delete_blog_post, name='delete_blog_post'),
]
