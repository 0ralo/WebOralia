from django.urls import path

from main.views import HomeView, PostsView, Summary, NewPostsView, NewCode, SecretView, RandomImage, BestGirl, handler500


urlpatterns = [
	path('', HomeView.as_view(), name="home"),
	path('500/', handler500),
	path('posts/', PostsView.as_view(), name="lent"),
	path('summary/', Summary.as_view(), name="summary"),
	path('secret/', SecretView.as_view(), name="secret"),
	path('newpost/', NewPostsView.as_view(), name="newpost"),
	path('new_code/', NewCode.as_view(), name="get_invite_code"),
	path('pic/', RandomImage.as_view(), name="randomimage"),
	path('bestgirl/', BestGirl.as_view(), name="bestgirl")
]
