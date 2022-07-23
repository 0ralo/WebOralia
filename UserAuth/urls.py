from django.urls import path
from .views import MyLoginView, MyRegisterView, log_out, check_captcha, MyRegisterViewFromTelegram, Confirmation

urlpatterns = (
	path('login/', check_captcha(MyLoginView.as_view()), name="login"),
	path('register/', check_captcha(MyRegisterView.as_view()), name="register"),
	path('tg_login/', check_captcha(MyRegisterViewFromTelegram.as_view()), name="telegram_auth"),
	path('tg_login/check', Confirmation.as_view(), name="confirm"),
	path('logout/', log_out, name="logout")
)
