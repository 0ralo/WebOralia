from django.forms import ModelForm
from main.models import Posts


class PostForm(ModelForm):
	class Meta:
		model = Posts
		fields = ['title', 'content', ]
