from django.contrib import admin

# Register your models here.

from .models import Loaner

# 将模型注册到admin页面，以让其在admin页面显示.
admin.site.register(Loaner)