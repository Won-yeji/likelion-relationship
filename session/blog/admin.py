from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    filter_horizontal = ('tag',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
#TODO: Like 추가하기
admin.site.register(Like)