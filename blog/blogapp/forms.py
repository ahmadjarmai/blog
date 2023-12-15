from .models import Comment 
from django import forms

class CommentForm(forms.ModelForm) :
    class Meta :
        models =Comment
        fields =['name','email','body']