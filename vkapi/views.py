import loguru
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

key: str = "28bd1796"


@csrf_exempt
def root(request):
	loguru.logger.info(request)
	return HttpResponse(key)
