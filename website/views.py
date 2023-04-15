from django.shortcuts import render, redirect, get_object_or_404
from decouple import config
from django.core.mail import send_mail
from .models import BlogPost
from django.core.paginator import Paginator
import math
from .forms import AddBlogPostForm, UpdateBlogPostForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def home(request):
    blog_posts = BlogPost.objects.order_by('-publish_date')[:3]
    return render(request, 'all.html', {'blog_posts': blog_posts})


def contact(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        message = request.POST['Message']
        # send an email
        send_mail(
            f'New Enquiry from {name}',  # subect
            message,  # message
            email,  # from
            ['adm.bjmn@gamil.com'],  # to email
        )
        return render(request, 'index.html', {'name': name})
    else:
        return render(request, 'index.html', {})


def repair_shop(request):
    return render(request, 'repairs.html', {})


def performance_shop(request):
    return render(request, 'performance.html', {})


def blog_posts(request):
    blog_posts = BlogPost.objects.all().order_by('-publish_date')
    if blog_posts.exists():
        total_blogs = len(blog_posts)
        p_n = Paginator(blog_posts, 3)
        page = request.GET.get('page')
        pages = p_n.get_page(page)
        num_pages = math.ceil((len(blog_posts)/3))
        print(num_pages)
        return render(request, 'blog/blog-posts.html',
                      {'pages': pages, 'num_pages': range(1, num_pages+1)})
    else:
        messages.success(
            request, 'We couldnt find Blog Posts.')
        return render(request, 'blog/blog-posts.html', {'blog_posts': blog_posts})


def blog_details(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    link = str(blog_post.link)
    return render(request, 'blog/blog-detail-view.html', {'blog_post': blog_post, 'link': link})


def create_blog_post(request):
    form = AddBlogPostForm()
    if request.method == 'POST':
        form = AddBlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = BlogPost()
            blog_post.title = form.cleaned_data['title']
            blog_post.content = form.cleaned_data['content']
            blog_post.click_bait = form.cleaned_data['click_bait']
            blog_post.link = form.cleaned_data['link']
            blog_post.image = form.cleaned_data.get("image")

            # new_file = df.to_csv(f'{settings.MEDIA_ROOT}/{date}.csv',
            #            encoding='utf-8', index=False)
            blog_post.save()
            blog_post.topic.add(form.cleaned_data['topic'])
            return redirect('blog')
    else:
        return render(request, 'blog/create-blog-post.html', {'form': form})


def edit_blog_post(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    form = UpdateBlogPostForm(request.POST or None, instance=blog_post)
    if form.is_valid():
        form.save()
        messages.success(
            request, (f'{blog_post.title} has been updated.'))
        return redirect('blog')
    else:
        return render(request, 'blog/edit-blog-post.html', {'form': form})
    return render(request, 'blog/edit-blog-post.html', {'blog_post': blog_post, })


def delete_blog_post(request, post_id):
    post_to_delete = get_object_or_404(BlogPost, id=post_id)
    delete_title = post_to_delete.title
    post_to_delete.delete()
    messages.success(
        request, (f'{delete_title} has been deleted.'))
    return redirect('home')
