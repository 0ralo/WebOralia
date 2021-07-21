import logging

from django.contrib.auth.models import AnonymousUser, User
from django.db.models import Model
from django.shortcuts import render

from UserAuth.models import BlackList

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[-1].strip()
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip


class BlackListMiddleware:
	def __init__(self, get_response):
		self._get_response = get_response

	def __call__(self, request):
		try:
			if request.user.is_authenticated:
				is_user_banned = BlackList.objects.get(user=request.user)
				return render(request, "UserAuth/banned.html")
			is_banned = BlackList.objects.get(ip=get_client_ip(request))
			return render(request, "UserAuth/banned.html")
		except BlackList.objects.model.DoesNotExist:
			response = self._get_response(request)
		return response
