from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	from_telegram = models.BooleanField(default=False)
	tg_id = models.PositiveIntegerField(default=0)
