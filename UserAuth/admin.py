from django.contrib import admin
from .models import BlackList


@admin.register(BlackList)
class PeopleAdmin(admin.ModelAdmin):
	list_display = ('pk', 'user', 'ip')
	list_display_links = ('pk', 'user')
