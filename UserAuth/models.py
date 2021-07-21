from django.contrib.auth.models import User
from django.db import models


class BlackList(models.Model):
	ip = models.CharField(max_length=20)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f"{self.user.username}@{self.ip}"
