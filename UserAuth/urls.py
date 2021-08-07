from django.urls import path
from .views import MyLoginView, MyRegisterView, log_out, check_captcha

urlpatterns = (
	path('login/', check_captcha(MyLoginView.as_view()), name="login"),
	path('register/', check_captcha(MyRegisterView.as_view()), name="register"),
	path('logout/', log_out, name="logout")
)
