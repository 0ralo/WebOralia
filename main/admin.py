from django.contrib import admin
from main.models import People, Posts, Codes


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
	list_display = ('pk', 'title', 'content', 'is_visible', 'date', 'author')
	list_editable = ('is_visible', )


@admin.register(Codes)
class PostAdmin(admin.ModelAdmin):
	list_display = ('pk', 'code', 'author', 'is_active')


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
	list_display = ('pk', 'title', 'image')
	list_editable = ('title',)
