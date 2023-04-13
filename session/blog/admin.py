from django.contrib import admin
from .models import *

# TODO: BlogAdmin 변경, Comment 등록, Tag 등록
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Tag)