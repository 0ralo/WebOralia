import random
import string

from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
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


class JSView(TemplateView):
	template_name = "main/myjstests.html"


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


def get_random_tag():
	f = ""
	for i in range(random.randint(3, 10)):
		f += string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase) - 1)]
	return f


def hardparse(req: WSGIRequest):
	html = "<{0}>{1}</{0}>".format(get_random_tag(), get_random_tag())
	a = random.randint(0, 60)
	if a % 2 == 0:
		tag = get_random_tag()
		html = f"<{tag} class={random.randint(0, 1000)} hidden='hidden'>{random.randint(0, 2000)}</{tag}>"
		html = f"<{tag} class={get_random_tag()}>{html}</{tag}>"
	if a % 3 == 0:
		tag = get_random_tag()
		html = f"<{tag}>{html}</{tag}>"
		html = f"<{tag} hidden='hidden'>{random.randint(0, 1000)}</{tag}>"
	if a % 4 == 0:
		tag = get_random_tag()
		html = f"<__{tag}__>{html}</__{tag}__>"
	if a % 6 == 0:
		tag = get_random_tag()
		html = f"<{tag} id={random.randint(0, 100)}>{html}</{tag}>"
	html = """
	<!DOCTYPE html>
	<html lang="en">
		<head>
            <meta charset="UTF-8">
            <title>It is impossible to parse this</title>
		</head>
        <body>
        {0}
        </body>
	</html>""".format(html)
	return HttpResponse(html)
