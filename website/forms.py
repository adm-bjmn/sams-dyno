from django import forms
from .models import BlogPost, Topic
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget


class UpdateBlogPostForm(ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label='Body',
        widget=CKEditorWidget(attrs={'class': 'form-control'})
    )
    click_bait = forms.CharField(
        label='Click Bait',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    link = forms.URLField(
        label='Links',
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'click_bait', 'link',)


class AddBlogPostForm(ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(),  # needs to be multiple choise
                                   label='Topic',
                                   widget=forms.Select(
                                       attrs={'class': 'form-control'})
                                   )
    content = forms.CharField(
        label='Body',
        widget=CKEditorWidget(attrs={'class': 'form-control'})
    )
    click_bait = forms.CharField(
        label='Click Bait',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    link = forms.URLField(
        label='Links',
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    image = forms.ImageField(
        label='Image',
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}))
    publish_date = forms.DateTimeInput()

    class Meta:
        model = BlogPost
        fields = ('title', 'topic', 'content', 'click_bait', 'link', 'image')
