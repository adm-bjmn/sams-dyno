from django.shortcuts import render
from decouple import config
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'index.html', {})


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
    return render(request, 'blog-app/blog-posts.html', {})


def blog_details(request):
    return render(request, 'index.html', {})


def create_blog_post(request):
    return render(request, 'index.html', {})


def edit_blog_post(request):
    return render(request, 'index.html', {})


def delete_blog_post(request):
    return render(request, 'index.html', {})
