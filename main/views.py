import random

from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.utils.decorators import method_decorator
import numpy
from PIL import Image
import uuid

from .forms import PostForm
from .models import Posts, Codes, People


class HomeView(TemplateView):
	template_name = "main/main.html"


class Summary(TemplateView):
	template_name = "main/summary.html"


class PostsView(ListView):
	template_name = "main/lenta.html"
	model = Posts
	context_object_name = 'posts'


class NewPostsView(CreateView):
	form_class = PostForm
	template_name = "main/newpost.html"

	@method_decorator(permission_required("main.can_add_post"))
	def get(self, request, *args, **kwargs):
		return super(NewPostsView, self).get(request, args, kwargs)

	@method_decorator(permission_required("main.can_add_post"))
	def post(self, request, *args, **kwargs):
		form = PostForm(request.POST)
		if form.is_valid():
			model = form.save(commit=False)
			model.author = request.user
			model.save()
			return redirect('home')
		else:
			messages.error(request, "Error while  creating post")
			return self.get()


class NewCode(TemplateView):
	template_name = "main/code.html"

	@method_decorator(permission_required("main.can_add_code"))
	def get(self, request, *args, **kwargs):
		try:
			code = Codes.objects.get(author=request.user, is_active=True).code
			return render(request, "main/code.html", {"code": code})
		except:
			pass
		rnd = random.randint(16, 32)
		code = uuid.uuid4().hex[rnd - 16:rnd]
		Codes.objects.create(code=code, is_active=True, author=request.user)
		return render(request, "main/code.html", {"code": code})


class SecretView(ListView):
	template_name = "main/secret.html"
	model = People
	context_object_name = 'people'

	def get_context_data(self, *, object_list=None, **kwargs):
		qs = super(SecretView, self).get_context_data(**kwargs)
		for n, i in enumerate(qs['people']):
			i.number = n
		return qs

	@method_decorator(login_required)
	def get(self, *args, **kwargs):
		return super(SecretView, self).get(*args, **kwargs)


class RandomImage(TemplateView):
	template_name = "main/randompic.html"

	def post(self, request):
		imarray = numpy.random.rand(200, 200, 3) * 255
		im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
		im.save("media/image.png")
		return render(request, self.template_name)

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)


def handler404(request: WSGIRequest, exception=None):
	request.status_code = 404
	return render(request, "errors/404.html")


def handler500(request: WSGIRequest, exception=None):
	request.status_code = 500
	return render(request, "errors/500.html")


class BestGirl(TemplateView):
	template_name = "main/bestgirl.html"

	def get(self, request: WSGIRequest, *args, **kwargs):
		if request.GET.get("password", "1") == "elana":
			return super().get(request, *args, **kwargs)
		else:
			return handler404(request)
