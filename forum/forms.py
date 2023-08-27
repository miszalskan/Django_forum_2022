from .models import Comment, Post
from django import forms
Options = [
            ('1', 'Snowboard'),
            ('2', 'Skiing'),
            ('3', 'Ice skates')
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'content': forms.TextInput(attrs={'class': 'text'})
        }


class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'is_important')
        category = forms.ChoiceField(choices=Options),
        widgets = {
            'content': forms.TextInput(attrs={'class': 'text'}),
        }
