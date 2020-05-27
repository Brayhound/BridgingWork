from django import forms
from .models import CV
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('header', 'profile', 'education', 'experience', 'extracurricular', 'skills',)