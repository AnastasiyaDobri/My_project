from .models import CommentsBook
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsBook
        fields = ('body',)