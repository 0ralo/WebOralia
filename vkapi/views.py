from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

key: str = "283bdf73"


@csrf_exempt
def root(request):
	if request.POST.get("type", None) == "confirmation" and request.POST.get("group_id", None) == "183943330":
		return HttpResponse(key)
	else:
		rsp = HttpResponse("ERROR")
		rsp.status_code = 404
		return rsp
