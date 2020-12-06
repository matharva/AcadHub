from django import forms 
from .models import *

class ProjectPostForm(forms.ModelForm):
    class Meta:
        model = ProjectPost
        fields = ['title','description','requirements','domain','deadline','image','link']

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

class PCommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea( 
    attrs ={ 
        'class':'form-control', 
        'placeholder':'Comment here !', 
        'rows':4, 
        'cols':50
    }))
    class Meta: 
        model = PComment 
        fields =['content']

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description']