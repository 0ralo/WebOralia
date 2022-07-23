from django import forms
from main.models import Posts


class PostForm(forms.ModelForm):
	class Meta:
		model = Posts
		fields = ['title', 'content', ]
