from django.contrib.auth.models import User
from django.http import HttpResponseNotFound

from rest_framework.response import Response
from rest_framework.views import APIView

from API.serializers import PostSerializer
from main.models import Posts


class UserExistView(APIView):
	def get(self, request, *args, **kwargs):
		username = request.GET.get('username')
		password = request.GET.get('password')
		try:
			user = User.objects.get(username=username)
			if user.check_password(password):
				return Response(data={'message': True, "passwordHASH": user.password})
			else:
				return Response(data={'message': False})
		except User.DoesNotExist:
			return Response(data={'message': False})


class PostView(APIView):
	def get(self, request, *args, **kwargs):
		username = request.GET.get('username')
		password = request.GET.get('password')
		if username and password:
			try:
				user = User.objects.get(username=username)
				if user.check_password(password):
					data = PostSerializer(Posts.objects.all().filter(is_visible=True), many=True)
					return Response(data.data)
			except User.DoesNotExist:
				return HttpResponseNotFound()
		return HttpResponseNotFound()


class UserById(APIView):
	def get(self, request, *args, **kwargs):
		ident = request.GET.get('id')
		try:
			user = User.objects.get(pk=ident)
		except User.DoesNotExist:
			return Response({"id": ident, "username": "empty"})
		except ValueError:
			return HttpResponseNotFound()
		else:
			return Response({"id": ident, "username": user.username})

