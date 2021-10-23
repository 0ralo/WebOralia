from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from API.views import UserExistView, PostView, UserById

urlpatterns = [
	path('panel/', admin.site.urls, name="admin"),
	path('', include('main.urls')),
	path('', include('UserAuth.urls')),
	path('api/exist', UserExistView.as_view()),
	path('api/posts', PostView.as_view()),
	path('api/ideer', UserById.as_view()),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'
