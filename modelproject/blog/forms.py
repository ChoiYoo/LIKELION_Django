from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'image', 'type']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': '제목'
                    }),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '글 작성하기...'
                    })
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': '댓글을 쓰세요...'
                    })
        }