from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings
import requests
from django.views.generic import CreateView

from UserAuth.forms import RegisterForm, LoginForm
from UserAuth.models import BlackList
from main.models import Codes


class MyLoginView(LoginView):
	template_name = "UserAuth/login.html"
	success_url = reverse_lazy('home')

	def get(self, request, *args, **kwargs):
		form = LoginForm()
		return render(request, self.template_name, {"form": form})

	def post(self, request, *args, **kwargs):
		form = LoginForm(request.POST)
		if not form.is_valid():
			messages.error(request, "Your login or password is incorrect")
			return self.get(request, args, kwargs)
		user = authenticate(username=request.POST["username"], password=request.POST["password"])
		if user is not None and self.request.recaptcha_is_valid:
			login(user=user, request=request)
			return redirect('home')
		elif not self.request.recaptcha_is_valid:
			messages.error(request, "Your recaptcha is not correct, try again")
		else:
			messages.error(request, "Your login or password is incorrect")
		return self.get(request, args, kwargs)

	def get_redirect_url(self):
		return self.success_url


class MyRegisterView(CreateView):
	form_class = UserCreationForm
	template_name = "UserAuth/register.html"

	def get(self, request, *args, **kwargs):
		form = RegisterForm()
		by_refer = False
		if request.GET.get("invitedby", "no") != "no":
			form.fields['code'].initial = request.GET.get("invitedby")
			by_refer = True
			form.fields['code'].widget.attrs['readonly'] = True
		return render(request, self.template_name, {"form": form, "by_refer": by_refer})

	def post(self, request, *args, **kwargs):
		form = UserCreationForm(request.POST)
		if form.is_valid() and self.request.recaptcha_is_valid:
			try:
				code = Codes.objects.get(code=request.POST["code"])
				code.is_active = False
				code.save()
			except Exception as f:
				print(f)
				messages.error(request, "Your invite code or invite link is incorrect")
				return self.get(request, args, kwargs)
			user = form.save()
			login(request, user)
			return redirect('home')
		elif not self.request.recaptcha_is_valid:
			messages.error(request, "Your recaptcha is not correct, try again")
		else:
			for _, i in form.errors.items():
				for j in i:
					messages.error(request, j)
		return self.get(request, args, kwargs)


def log_out(request):
	logout(request)
	return redirect('home')


def check_captcha(func):
	def wrap(request, *args, **kwargs):
		request.recaptcha_is_valid = None
		if request.method == 'POST':
			recaptcha_response = request.POST.get('g-recaptcha-response')
			data = {
				'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
				'response': recaptcha_response
			}
			r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
			result = r.json()
			if result['success']:
				request.recaptcha_is_valid = True
			else:
				request.recaptcha_is_valid = False
		return func(request, *args, **kwargs)

	wrap.__doc__ = func.__doc__
	wrap.__name__ = func.__name__
	return wrap
