from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
	title = models.CharField(max_length=30, verbose_name="Заголовок")
	content = models.TextField(verbose_name="Содержимое")
	is_visible = models.BooleanField(default=False, verbose_name="Показывается")
	date = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
	author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)

	# image = models.ImageField(verbose_name="Фотография", upload_to="%Y/%m/%d/", blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Посты"
		verbose_name_plural = "Пост"
		permissions = (('can_add_post', 'Can add post'),)


class Codes(models.Model):
	code = models.CharField(max_length=16, verbose_name="Код")
	is_active = models.BooleanField(default=True, verbose_name="Активен")
	author = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.author.username}:{self.code}"

	class Meta:
		verbose_name = "Код"
		verbose_name_plural = "Коды"
		permissions = (('can_add_code', 'Can add new code'),
		               ('can_delete_code', 'Can delete code'),
		               ('can_manipulate_code', 'Can manipulate code'))


class People(models.Model):
	image = models.ImageField(upload_to="people/", verbose_name="Люди")
	title = models.CharField(max_length=20, verbose_name="Надпись")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Челик"
		verbose_name_plural = "Люди"
