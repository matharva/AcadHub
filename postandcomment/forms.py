from django import forms 
from .models import Comment, Post, Community



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','category','image', 'link']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea( 
    attrs ={ 
        'class':'form-control', 
        'placeholder':'Comment here !', 
        'rows':4, 
        'cols':50
    }))
    class Meta: 
        model = Comment 
        fields =['content']


class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description']